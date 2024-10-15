import pydash
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app import middlewares
from app.core.config.settings import settings

def custom_generate_unique_id(route: APIRoute):
    tags = pydash.uniq(route.tags)
    group = '-'.join(tags[:3]) if len(tags) > 0 else "App"
    return f"{group}-{route.name}"

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    servers=[{
        "url": settings.base_url
    }],
    docs_url="/docs" if settings.enable_doc else None,
    redoc_url="/redoc" if settings.enable_doc else None,
    generate_unique_id_function=custom_generate_unique_id
 )

app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
middlewares.setup_middlewares(app)

@app.get("/health")
async def health():
    return "It's worked"
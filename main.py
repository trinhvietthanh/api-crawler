import uvicorn
from app.server import app

__all__ = ['app']
def run():
    """Entry point for run debug app."""
    uvicorn.run(
        'app:app',
        host="127.0.0.1",
        port=8080,
        reload=True,
    )


if __name__ == '__main__':
    run()
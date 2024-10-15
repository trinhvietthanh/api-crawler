from pathlib import Path
from sys import modules
from pydantic_settings import BaseSettings
from .environ import env

BASE_DIR = Path(__file__).resolve()
ROOT_DIR = Path(BASE_DIR).parent.parent


class Settings(BaseSettings):
    @property
    def app_name(self):
        return env('APP_NAME')
    
    @property
    def host(self):
        return env('HOST')
    
    @property
    def port(self):
        return env.int('PORT')
    
    @property
    def debug(self):
        return env.bool("DEBUG")
    
    @property
    def base_url(self):
        return env.url("BASE_URL")

    @property
    def allowed_hosts(self):
        allowed_hosts = env("ALLOWED_HOST").split(",")
        allowed_hosts = map(str.strip, allowed_hosts)
        allowed_hosts = filter(lambda host: len(host) > 0, allowed_hosts)
        allowed_hosts = list(allowed_hosts)
        if len(allowed_hosts) == 0:
            return ["*"]
        return allowed_hosts
    
    @property
    def enable_doc(self):
        return env.bool("DISABLE_DOCS")
    
    @property
    def api_key(self):
        return env.str("API_KEY")
    
    @property
    def db_url(self):
        return env("SQLALCHEMY_DATABASE_URI")

class TestSettings(Settings):
    pass

settings = TestSettings() if "pytest" in modules else Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file: ".env"

settings = Settings()
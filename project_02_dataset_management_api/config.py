from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    IS_DB_CREATED : bool = False

    model_config = SettingsConfigDict()

settings = Settings()
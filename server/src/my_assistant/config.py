from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    anthropic_api_key: str
    agent_engine_mcp_url: str
    agent_engine_mcp_token: str | None = None
    app_bearer_token: str

    model: str = "anthropic:claude-haiku-4-5-20251001"


settings = Settings()

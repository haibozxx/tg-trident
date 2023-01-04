from pydantic import BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    API_ID: str
    API_HASH: str

    
    class Config:
        case_sensitive = False 
    
env_file = "/Users/haiboz/work/oke/tg-trident/.env"
settings = Settings(_env_file=env_file)
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    db_password: str
    db_name: str
    db_user: str


    class Config:
        env_file = '.env'



settings = Settings()
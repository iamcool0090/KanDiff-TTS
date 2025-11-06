from pydantic_settings import BaseSettings

class Config(BaseSettings):
    DATASET_PATH: str = "data/dataset.csv"
    AZURE_API_KEY: str = ""



    # load environment variables from .env.local
    model_config = {
        "env_file": ".env.local",
        "env_file_encoding": "utf-8",
    }

config = Config()
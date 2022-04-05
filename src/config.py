from pydantic import BaseModel
import json

class Settings(BaseModel):
    nbr_keys: int
    multiplicator: float

def load_settings() -> Settings:
    with open('settings.json', 'r') as settings_file:
        settings = Settings(**json.load(settings_file))
    return settings
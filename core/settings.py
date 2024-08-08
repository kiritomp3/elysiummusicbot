from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(patch: str):
    env = Env()
    env.read_env(patch)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN_API"),
            admin_id=env.int("ADMIN_ID")
        )
    )

settings = get_settings('input')
print(settings)
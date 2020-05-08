from envvarconf import BaseSettings
from envvarconf.loaders import environ


class Settings(BaseSettings):
    SENTRY_DSN: str
    LOGGING_LEVEL: str = 'debug'

    HOST: str = "aaaakehgeiuhgiweurhiuerhf"*200
    PORT: int


if __name__ == "__main__":
    settings = Settings()
    settings.load(loader=environ.Loader())

    print("OK!")
    print(settings)

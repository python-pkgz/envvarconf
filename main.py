from decimal import Decimal

from envvarconf import BaseSettings
from envvarconf.loaders import environ
from envvarconf.mixins.logger import LoggingMixin


class Settings(LoggingMixin, BaseSettings):
    SENTRY_DSN: str

    HOST: str = "aaaakehgeiuhgiweurhiuerhf"*200
    PORT: int
    RATE: float
    AMOUNT: Decimal


if __name__ == "__main__":
    settings = Settings()
    settings.load(loaders=[environ.Loader(), ])
    settings.print_detailed_settings()

    print("OK!")
    print(settings)

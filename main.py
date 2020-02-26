from envvarconf import BaseSettings


class Settings(BaseSettings):
    SENTRY_DSN: str
    LOGGING_LEVEL: str = 'debug'

    HOST: str = "aaaakehgeiuhgiweurhiuerhf"*200
    PORT: int


if __name__ == "__main__":
    settings = Settings(envvar_prefix='EVC')
    settings.load()

    print("OK!")
    print(settings)

from envvarconf import BaseSettings


class Settings(BaseSettings):
    SENTRY_DSN: str
    LOGGING_LEVEL: str = 'debug'

    HOST: str = "aaaakehgeiuhgiweurhiuerhf"*200
    PORT: int


def test_settings_invalid():
    settings = Settings(envvar_prefix="EVC_TEST", appname="evc_tests")
    settings.load(failfast=False)
    errors = settings.validation_errors()
    assert len(errors) == 2
    assert errors == ['SENTRY_DSN is not defined', 'PORT is not defined']


def test_settings_valid(monkeypatch):
    monkeypatch.setenv("EVC_TEST_SENTRY_DSN", "123")
    monkeypatch.setenv("EVC_TEST_PORT", "123")

    settings = Settings(envvar_prefix="EVC_TEST", appname="evc_tests")
    settings.load()
    errors = settings.validation_errors()
    assert len(errors) == 0
    assert settings.SENTRY_DSN == "123"
    assert settings.PORT == 123

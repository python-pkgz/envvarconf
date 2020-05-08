from typing import Type

from envvarconf import BaseSettings, ALLOWED_TYPES


class BaseLoader:
    """
    Abstract base loader class
    """

    @staticmethod
    def set_var(settings: BaseSettings, varname: str, raw_value: str, vartype: Type):
        assert vartype in ALLOWED_TYPES, f"Wrong type for {varname}: {vartype}"
        try:
            varvalue = vartype(raw_value)
        except ValueError as ex:
            raise ValueError(f"There is error converting {varname}'s value '{raw_value}' to {vartype}'") from ex
        setattr(settings, varname, varvalue)

    def load(self, settings: BaseSettings) -> BaseSettings:
        raise NotImplementedError

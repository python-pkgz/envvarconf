import os

from envvarconf import BaseSettings
from envvarconf.loaders.base import BaseLoader


class Loader(BaseLoader):
    def load(self, settings: BaseSettings):
        for varname, vartype in settings.__annotations__.items():
            if varname in os.environ:
                self.set_var(settings, varname, raw_value=os.environ[varname], vartype=vartype)

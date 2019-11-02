from cached_property import cached_property
from configparser import ConfigParser
from os.path import abspath
from os.path import dirname
from os.path import exists
from os.path import join

PERMISSIONS_CHOICES = ('rw', 'co', 'ro')

class TouchGoogleDoc(object):

    CONFIG_FILENAME = "setup.cfg"
    CONFIG_SECTION_NAME = "touchgdoc"
    CONFIG_KEYS = ("timezone",)
    def __init__(self,):
        self.config = TouchGoogleDoc._load_config()

    @staticmethod
    def _load_config():
        parser = ConfigParser()
        here = abspath(dirname(dirname(__file__)))
        parser.read(join(here, TouchGoogleDoc.CONFIG_FILENAME))
        config = parser[TouchGoogleDoc.CONFIG_SECTION_NAME]
        TouchGoogleDoc._check_config(config)
        return config

    @staticmethod
    def _check_config(config):
        keys = TouchGoogleDoc.CONFIG_KEYS
        if not all([key in config for key in keys]):
            msg = (f"{keys} must all be defined in setup.cfg[touchgdoc].")
            raise KeyError(msg)
        if any([key not in keys for key in config.keys()]):
            msg = "setup.cfg[github_reporter] contains an undefined key."
            msg += f"Allowed keys are:\n{CONFIG_KEYS}"
            raise KeyError(msg)

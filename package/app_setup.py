from configparser import ConfigParser
from os.path import abspath, dirname, exists, join

CONFIG_FILENAME = "setup.cfg"
CONFIG_SECTION_NAME = "<my_project>"
CONFIG_KEYS = (
    "timezone",
)
HERE = abspath(dirname(dirname(__file__)))


def load_config():
    parser = ConfigParser()
    parser.read(join(HERE, CONFIG_FILENAME))
    config = parser[CONFIG_SECTION_NAME]
    check_config(config)
    return config


def check_config(config):
    if not all([key in config for key in CONFIG_KEYS]):
        msg = (
            f"{CONFIG_KEYS} must all be defined in setup.cfg[<my_project>]."
        )
        raise KeyError(msg)
    if any([key not in CONFIG_KEYS for key in config.keys()]):
        msg = "setup.cfg[<my_project>] contains an undefined key."
        msg += f"Allowed keys are:\n{CONFIG_KEYS}"
        raise KeyError(msg)

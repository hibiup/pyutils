import configparser
import os
import sys
import logging


class Properties:
    __config = configparser.ConfigParser()

    def __init__(self, path="conf/application.cfg"):
        config_path = os.path.join(os.path.abspath(''), path)
        if os.path.exists(config_path) is False:
            config_path = os.path.join(os.path.abspath(os.path.dirname(sys.modules['__main__'].__name__)), path)
            logging.debug("Checking configuration file " + config_path)
        if os.path.exists(config_path) is False:
            try:
                python_home = os.environ['PYTHONHOME']
                config_path = os.path.join(os.path.abspath(python_home), path)
            except:
                config_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(sys.executable))), path)
            logging.debug("Checking configuration file " + config_path + path)
        if os.path.exists(config_path) is False:
            config_path = os.path.join("/", path)
            logging.debug("Checking configuration file " + config_path + path)
        if os.path.exists(config_path) is False:
            raise FileNotFoundError("Configuration file " + config_path + " does not exist.")
        self.__config.read(config_path)
        logging.debug("Configuration file has been loaded from " + config_path)

    def getString(self, key: str) -> str:
        return self.__config['DEFAULT'][key]

    def getInt(self, key: str) -> int:
        return self.__config['DEFAULT'].getint(key)

    def getEnv(self, key: str):
        return os.getenv(key)

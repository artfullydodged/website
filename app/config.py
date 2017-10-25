import os

class BaseConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
	DEBUG = True


class ProdConfig(BaseConfig):
	DEBUG = False



# export APP_SETTINGS=config.DevConfig
# export DATABASE_URL="postgresql://localhost/flightbase"
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base config, uses staging database server."""

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    """Uses production database server."""

    DEBUG = False


class DevelopmentConfig(Config):
    """Uses local database server."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class TestingConfig(Config):
    """Uses testing database server."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


settings = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

# import os

# class Config:
#     DEBUG = False
#     DEVELOPMENT = False
#     SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

# class ProductionConfig(Config):
#     pass

# class StagingConfig(Config):
#     DEBUG = True

# class DevelopmentConfig(Config):
#     DEBUG = True
#     DEVELOPMENT = True



# app.py
# import os

# from flask import Flask

# app = Flask(__name__)
# env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
# app.config.from_object(env_config)


# @app.route("/")
# def index():

# secret_key = app.config.get("SECRET_KEY")
# https://flask.palletsprojects.com/en/2.1.x/
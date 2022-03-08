
import os


class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    APP_ID = os.environ.get('APP_ID', None)
    API_HASH = os.environ.get('API_HASH', None)
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
    ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'

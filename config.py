import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()
    DEBUG = os.environ.get("DEBUG", 'False').lower() == 'true'
    TESTING = os.environ.get("TESTING", 'False').lower() == 'true'
    URL_PREFIX = os.environ.get("URL_PREFIX", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", 'False').lower() == 'true'
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DB = os.environ.get("MYSQL_DB")
    MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", 3306)
    MYSQL_CHARSET = os.environ.get("MYSQL_CHARSET", "utf8mb4")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=%s' % (
        MYSQL_USERNAME,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DB,
        MYSQL_CHARSET
    )
    SQLALCHEMY_ECHO = True
    AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
    AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN", None)
    AWS_REGION = os.environ.get("AWS_REGION", None)
    QUEUE_OWNER_ACCOUNT_ID = os.environ.get("QUEUE_OWNER_ACCOUNT_ID", None)
    CRON_JOB_QUEUE_NAME = os.environ.get("CRON_JOB_QUEUE_NAME", None)
    LINE_TOKEN = os.environ.get("LINE_TOKEN", None)

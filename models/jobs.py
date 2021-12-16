import datetime

from utils.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Jobs(db.Model):
    __tablename__ = "jobs"
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    func_name = db.Column(db.String(128))
    cron = db.Column(db.String(128), comment='排程時間')
    params = db.Column(db.String, comment='參數')
    status = db.Column(db.Integer, nullable=False, comment='狀態（0:disable 1:enable）')
    execute_at = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP, default=lambda:datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.TIMESTAMP, default=lambda:datetime.datetime.now(datetime.timezone.utc),
                           onupdate=lambda:datetime.datetime.now(datetime.timezone.utc))
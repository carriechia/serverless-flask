import datetime

from utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy.dialects.mysql import INTEGER

class Accounts(db.Model):
    __tablename__ = "accounts"
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    account_roles = db.relationship("AccountRole", primaryjoin="Accounts.id == AccountRole.account_id", lazy='dynamic')
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(512))
    phone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP, default=lambda:datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.TIMESTAMP, default=lambda:datetime.datetime.now(datetime.timezone.utc),
                           onupdate=lambda:datetime.datetime.now(datetime.timezone.utc))


class Accounts(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ('id', 'name', 'email')

accounts_schema = Accounts(many=True)
from flask import Flask
from utils.database import db, ma
from config import Config

from services import accounts


app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
ma.init_app(app)


@app.route("/", methods=['GET'])
def get_accounts():
    print(123)
    exit()
    data = accounts.get_accounts()
    return data


if __name__ == '__main__':
    app.run(debug=True)
from models.accounts import Accounts, accounts_schema

def get_accounts():
    data = Accounts.query.all()
    return accounts_schema.dump(data)
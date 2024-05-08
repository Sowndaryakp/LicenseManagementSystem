from pony.orm import Database, Required

db = Database()

class User(db.Entity):
    # _table_ = ("machines", "user")
    username = Required(str)
    password = Required(str)
    company = Required(str)
    email = Required(str)
    is_admin = Required(bool)

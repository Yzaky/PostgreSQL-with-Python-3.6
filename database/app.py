from user import User
from database import Database

Database.init()

user=User('test@test.com','test1','test2',None)

user.save_to_db()

user_from_db=User.load_from_db_by_email('test@test.com')

print(user_from_db)
from user import User

my_user=User('test@test.com','Rolf','Test',None)

my_user.save_to_db()

user_from_db=User.load_from_db_by_email('test@test.com')

print(user_from_db)

my_user.save_to_db()
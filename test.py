import db
from models import User,Balance

users = db.session.query(User).all()
print(users)
#balance = db.session.query(Balance).filter(Balance.user==users[0].id).first()
#db.session.delete(balance)
#db.session.commit()
print(db.session.query(Balance).all())


import db
from sqlalchemy import Column,Integer,String,ForeignKey

class User(db.Base):
    
    __tablename__ = 'Users'
    
    id = Column(Integer,primary_key=True)
    userTelegramId = Column(Integer)
    username = Column(String)
    name = Column(String)
    
    def __init__(self,**kwargs) -> None:
        self.userTelegramId = kwargs.get('userTelegramId')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
    
    def __str__(self) -> str:
        return self.userTelegramId
    
    def __repr__(self) -> str:
        return f"<User: {self.userTelegramId}>"

class Balance(db.Base):
    
    __tablename__ = 'Balances'
    
    id = Column(Integer,primary_key=True)
    user = Column(Integer,ForeignKey('Users.userTelegramId'),unique=True)
    balance = Column(Integer,default=0)
    
    def __init__(self,user) -> None:
        self.user = user
    
    def __str__(self) -> str:
        return f"{self.user.username if self.user.username else self.user.name}: {self.balance}"
    
    def __repr__(self) -> str:
        return f"<Balance: {self.user} : {self.balance}>"

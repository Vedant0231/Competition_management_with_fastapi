from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date
from datetime import datetime
#model for user table

class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key = True,index = True, autoincrement=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
 
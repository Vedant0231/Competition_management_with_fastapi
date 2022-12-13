from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey
from app.models.user_model import User
from datetime import datetime
#Model for competition table

class Competition(Base):
    __tablename__ = "competition_table"
    id = Column(Integer, primary_key = True,index = True)
    name = Column(String)
    status = Column(String)
    is_active = Column(Boolean,default=True )
    is_delete = Column(Boolean , default=False)
    created_at = Column(DateTime, default = datetime.utcnow)
    update_at = Column(DateTime , default = datetime.utcnow)
    description = Column(String)
    user_id=Column(Integer,ForeignKey(User.id))
 
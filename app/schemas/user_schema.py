from pydantic import BaseModel , Field
from typing import Optional
from datetime import date
class Users(BaseModel):
    id: int
    name: str
    birth_date: date
    gender: str
    created_at: date
    update_at: date
    is_active: bool
    is_delete: bool
 
class CreateUsers(BaseModel):
    name:Optional[str]=None
    birth_date:Optional[date] = Field(default_factory=date(2022 , 12 , 12))
    gender:Optional[str]



class DisplayUsers(BaseModel):
    id:int
    name:str
    birth_date:date
    gender:str

    class Config:
        orm_mode = True    

from pydantic import BaseModel
from datetime import date


#demo schema for developer to unserstand the structure of entry table
class Entrys(BaseModel):
    id: int
    title: str 
    topic: str 
    state: str
    country: str
    is_delete: bool
    created_at: date
    updated_at: date
    competition_id: int


#schema for taking input and show the response 
class CreateEntry(BaseModel):
    id: int
    title: str 
    topic: str 
    state: str
    country: str
    competition_id: int    

    class Config():
        orm_mode = True
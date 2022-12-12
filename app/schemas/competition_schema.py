from pydantic import BaseModel
from datetime import date
from typing import Optional

class Competitions(BaseModel):
    id: int
    name: str
    status: str
    is_active: bool 
    is_delete: bool
    created_at: date
    update_at: date
    description: str
    user_id: int

class CreateCompetition(BaseModel):
    id:int
    name:str
    status:str
    user_id:int
    description:str

    class Config:
        orm_mode = True


        
 
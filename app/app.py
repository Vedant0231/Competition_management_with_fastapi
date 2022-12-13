#import all routes 

from fastapi import FastAPI
from app.routes.competition_route import competition
from app.routes.entry_route import entry
from app.routes.user_route import userdata

app = FastAPI()

app.include_router(competition)
app.include_router(entry)
app.include_router(userdata)
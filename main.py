import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # uvicorn.run("app.app:app", host="127.0.0.1", port=8000, log_level="info" , reload= True)
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    uvicorn.run("app.app:app", host= HOST , port= int(PORT) , reload= True)


    
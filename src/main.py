from fastapi import FastAPI
from routes.routes import User 

app = FastAPI(
    title="GainGrub API",
    version="1.0"
)


app.include_router(User, prefix="/api/user")


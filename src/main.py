from fastapi import FastAPI
from routes.routes import User 
from db.db import init_db

app = FastAPI(
    title="GainGrub API",
    version="1.0"
)

# ✅ Create tables in the database before the app starts
init_db()

app.include_router(User, prefix="/api/user")


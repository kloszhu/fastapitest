# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import Optional

from fastapi import Cookie, FastAPI,APIRouter
from dao.usercontroller import router as userrouter
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# 路由
app.include_router(userrouter)
# CORS
origins = [
    "http://localhost:8000",
    "http://localhost:8000",
    "http://localhost:8000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}

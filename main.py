# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import Optional

from fastapi import Cookie, FastAPI,APIRouter
from dao.usercontroller import router as userrouter
from fastapi.middleware.cors import CORSMiddleware

from authoize.authcontroller import app as authorrouter


app = FastAPI(title="我的工作台",
              description="这是一个信息发布工具",
              version='1.0.0')
# 路由
app.include_router(userrouter)
app.include_router(authorrouter)
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
async def read_items(ads_id:Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}

## 依赖关系
### 生成依赖关系：
pip freeze > requirements.txt
### 还原依赖关系：
pip install -r requirements.txt
## 安装核心依赖
pip install fastapi
pip install uvicorn
## 启动
uvicorn main:app --reload
## CORS
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
## 创建随机hash
openssl rand -hex 32


## jwt无法提交的问题
### 源码中出现了问题，OAuth2PasswordRequestForm=Depend()有问题，
修改为下面的逻辑，为何要这么做，因为fastapi 处理请求和返回请求都是
使用pydantic模块，修改为基于此模块方式，使用正常：
from pydantic import BaseModel, ValidationError

class OAuth2PasswordRequestForm(BaseModel):

# 表单提交账号与密码

from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')  # 文件夹说明，说明此文件夹用来存放模版文件


@app.post('/user/')
async def create_upload_files(request: Request, username: str = Form(...), password: str = Form(...)):
    print('username', username)
    print('password', password)
    return templates.TemplateResponse('index.html', {'request': request, 'username': username, 'password': password})


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post.html', {'request': request, 'hello': 'HI...'})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

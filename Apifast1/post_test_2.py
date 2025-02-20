# _file上传文件
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.post("/files/")
async def files(
        request: Request,
        files_list: List[bytes] = File(...),  # (...)表示这个参数为必传且没有设置默认值
        files_name: List[UploadFile] = File(...),  # (...)表示这个参数为必传且没有设置默认值
):
    return templates.TemplateResponse("index2.html",
                                      {
                                          "request": request,  # 请求参数
                                          "file_sizes": [len(file) for file in files_list],  # 上传多个文件
                                          "filenames": [file.filename for file in files_name],  # 上传多个文件
                                      })


@app.post("/create_file/")
async def create_file(
        request: Request,
        file: bytes = File(...),
        fileb: UploadFile = File(...),
        notes: str = Form(...),
):
    return templates.TemplateResponse("index2.html",
                                      {
                                          "request": request,
                                          "file_size": len(file),
                                          "notes": notes,
                                          "fileb_contest_type": fileb.content_type,
                                      })


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post2.html', {'request': request})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello': 'HI...'})


@app.get("/{items_id}/")
async def item_id(request: Request, items_id):
    return templates.TemplateResponse('index.html', {'request': request, 'items_id': items_id})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import io
import os
from PIL import Image

# Add root to sys path
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# Scripts
import settings
from api.utils.filesystem import make_dir, file_from_bytes
from detect import detect
from fastapi.responses import FileResponse

app = FastAPI()
# ! DEPLOY USING THIS https://dev.to/shuv1824/deploy-fastapi-application-on-ubuntu-with-nginx-gunicorn-and-uvicorn-3mbl
@app.post("/detect/")
async def create_files(file: UploadFile = File(...)):
    '''
    Receives a list of files and saves them to model paths
    '''
    dir_path =  make_dir(dir_path=f'{os.getenv("UPLOADS_PATH")}/model/tmp/')
    
    file_path =  file_from_bytes(file.file, dir_path, 'tmp.jpeg')
    print(file_path)

    output_path = make_dir(dir_path=f'{os.getenv("MODEL_OUTPUTS")}')
    config= {
                'weights':'yolov5s.pt',
                'source':str(dir_path),
                'output':str(output_path),
                'img_size':640,
                'conf_thres':0.4,
                'iou_thres':0.5,
                'device': 'cpu', # or gpu number: 0,1,2,3
                'view_img':False,
                'save_txt':'store_true',
                'classes':'',
                'agnostic_nms':'store_true',
                'augment':'store_true',
                'update':False
            }
    detect(config)
    output_path = make_dir(dir_path=f'{os.getenv("MODEL_OUTPUTS")}')
    return FileResponse(str(output_path/'tmp.jpeg'))

@app.get("/")
async def main():
    content = """
<body>
<form action="/detect/" enctype="multipart/form-data" method="post">
<input name="file" type="file">
<input type="submit">
</form>

<form action="/show_img/" method="get">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

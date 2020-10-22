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
from api.utils.filesystem import make_dir
from detect import detect
from fastapi.responses import FileResponse

app = FastAPI()

# Detect endpoint
@app.post("/detect/")
async def create_files(file: UploadFile = File(...)):
    '''
    Receives a list of files and saves them to model paths
    '''
    # Create uploads directory if not exists
    dir_path =  make_dir(dir_path=f'{os.getenv("UPLOADS_PATH")}/model/tmp/')

    # Create outputs directory if not exists
    output_path = make_dir(dir_path=f'{os.getenv("MODEL_OUTPUTS")}')

    # Yolo Config Dict
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
    # Yolo Detect Objects
    detect(config)

    # Image with objects path
    output_path = make_dir(dir_path=f'{os.getenv("MODEL_OUTPUTS")}')
    # Return image with objects as response
    return FileResponse(str(output_path/'tmp.jpeg'))

# Home endpoint, returns simple html  
@app.get("/")
async def main():
    content = """
<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">

<body>
<form class="text-center border border-light p-5" action="/detect/" enctype="multipart/form-data" method="post">
<h1>Detecta Objetos en Imágenes</h1>
<p> Esta demo usa yolov5 y fastapi</p>
<div>
  <label for="files" class="btn ">Seleccionar Imagen</label>
  <input name="file" id="files" style="visibility:hidden;" type="file">
  <label for="btnUpload" class="btn btn-primary">Detectar Objetos!</label>
  <input name="btnUpload" id="btnUpload" style="visibility:hidden;" type="submit">
</div>
    """
    return HTMLResponse(content=content)

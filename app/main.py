from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pandas as pd
from typing import List
import os

app = FastAPI(title="AI BOQ Comparison", version="1.0.0")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-boq")
async def upload_boq(files: List[UploadFile] = File(...)):
    """อัปโหลดและเปรียบเทียบไฟล์ BOQ"""
    if len(files) != 2:
        return {"error": "กรุณาอัปโหลดไฟล์ 2 ไฟล์"}
    
    # TODO: ประมวลผลไฟล์ BOQ
    return {"message": "ไฟล์ถูกอัปโหลดเรียบร้อย", "files": [f.filename for f in files]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
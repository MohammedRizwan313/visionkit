from fastapi import FastAPI, UploadFile, File
from ocrmac import ocrmac

app = FastAPI()

def perform_ocr(image):
    annotations = ocrmac.OCR(image).recognize()
    arr=[]
    text = ""
    for annotation in annotations:
        text += annotation[0] + "\n"
        
    return text

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file locally
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    # Perform OCR on the uploaded file
    recognized_text = perform_ocr(file.filename)
    return {"recognized_text": recognized_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

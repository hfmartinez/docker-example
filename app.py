import io
import pickle
import PIL.Image
import PIL.ImageOps
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
def root():
    return {"App": "ML-fastapi-test"}


@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    pil_image = PIL.Image.open(io.BytesIO((contents))).convert("L")
    pil_image = pil_image.resize((28, 28), PIL.Image.LANCZOS)
    img_array = np.array(pil_image).reshape(1, -1)
    prediction = model.predict(img_array)
    return {"prediction": int(prediction[0])}

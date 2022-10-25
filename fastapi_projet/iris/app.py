from fastapi import FastAPI 
from pydantic import BaseModel 
import uvicorn
from fastapi.responses import JSONResponse

import numpy as np

app = FastAPI()
class iris(BaseModel): 
    a:float 
    b:float 
    c:float 
    d:float
    
from sklearn.linear_model import LogisticRegression 
import pandas as pd 
import pickle #we are loading the model using pickle 
model = pickle.load(open('model_iris', 'rb'))
@app.get("/") 
def home(): 
    return {'ML model for Iris prediction'} 

@app.post('/predictions') 
async def make_predictions(features:iris):
    return {"prediction":str(model.predict(features)[0])}


if __name__ == "__main__": 
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
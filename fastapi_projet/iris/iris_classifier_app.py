from fastapi import FastAPI
from fastapi.responses import JSONResponse
from iris_classifier_object import Iris_Classifier
from pydantic import BaseModel

#create the application
app = FastAPI(
    title = "Iris Classifier API",
    version = 1.0,
    description = "Simple API to make predict class of iris plant."
)

#creating the classifier
classifier = Iris_Classifier("model_iris")

#Model
class Iris(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

@app.get("/") 
def home(): 
    return {'ML model for Iris prediction'} 

@app.post("/prediction",tags = ["iris_classifier"])
def get_prediction(features:Iris):
    species_pred = classifier.make_prediction(features.dict())
    return JSONResponse({"species":species_pred})
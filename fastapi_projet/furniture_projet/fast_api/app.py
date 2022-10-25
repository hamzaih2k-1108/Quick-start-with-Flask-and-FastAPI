from unittest import result

from fastapi import FastAPI,Request
#from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import uvicorn

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

model = pickle.load(open('model.pkl', 'rb'))

@app.get("/") 
def home(request:Request): 
    result=""
    return templates.TemplateResponse("index.html",{"request":request,"result":result})

@app.post('/')
def predict(request:Request):
    result=""
    '''
    pour l'affichage sur html
    '''
    features = request.query_params._dict
    print(features)
    features = list(features.values())
    #print(features)
    features = list(map(int, features))
    #print(features)
    final_features = np.array(features).reshape(1,6)
    #print(features)
    prediction = model.predict(final_features)
    
        #select = request.form.get('category')
    result = round(prediction[0], 2)
    return templates.TemplateResponse("index.html",{"request":request,"result":"The price of the furniture: ${}".format(result)})
    
if __name__ == "__main__": 
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
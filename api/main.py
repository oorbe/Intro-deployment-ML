from fastapi import FastAPI
from  app.models import *
from  app.views import *  
# import  .app.models 
# import  .app.views

app = FastAPI(docs_url='/')

@app.post('/v1/prediction')
def make_model_predicion(reques: PredictionsRequest):
    return PredictionResponse(wordwide_gross = get_predicition(reques))

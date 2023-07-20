# primero creamos el servicio
from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(docs_url = '/') # "'/'" Es para que la UI de la documetación que se genera con FasApi este en el origen y podamos probar nuestro modelo.

# Creamos endpoint
@app.post('/v1/prediction') # v1: la vesión de nuestro modelo, evetualmente las versiones pueden cambiar
def make_mode_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross = get_prediction(request))
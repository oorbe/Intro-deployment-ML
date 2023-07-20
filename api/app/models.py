# Aqui las caracteristica para hacer une predicción o inferencia y el target del world Wide gross

from pydantic import BaseModel # Para serializar los json que dentran y sales de nuestra app.

class PredictionRequest(BaseModel): # Herada de BaseModel
    # estas son las características-features equivaletes que utilizamos para entrenar el modelo
    # los ontuve con la función : "data.dtypes", del archivo "borrador.ipynb".
    opening_gross     : float
    screens           : float
    production_budget : int
    title_year        : float
    aspect_ratio      : float
    duration          : float
    budget            : float
    imdb_score        : float

# ['opening_gross', 'screens', 'production_budget', 'title_year','aspect_ratio', 'duration', 'budget', 'imdb_score']

class PredictionResponse(BaseModel): # Here da BaseModel.
    # Entregamos el world wide gross
    worldwide_gross: int
    

from pydantic import BaseModel # serializar los json que ingresar y salen de la app

class PredictionsRequest(BaseModel):
    opening_gross: float
    screens : float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float
    
class PredictionResponse(BaseModel):
    worlwide_gross: float

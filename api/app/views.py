from .models import PredictionRequest
from .utils  import  get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, prediction) # nunca se debe entregar predicciones crudas a un usuario final, pues el modelo puede tener algún erro o falla en su inferencias, por esto mejor tratarl antes de entregarla, por eso la predicción debe ser mayor que cero, pues no puede ser menor que cero.


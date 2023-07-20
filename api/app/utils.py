
# What is Type Hints in Python
# Type hints is a feature of Python that allows you to explicitly declare the data type of a variable when declaring it. They are only available in Python 3.5 and later.
# 
# Type hints provide two benefits. First, they help people reading your code to know what types of data to expect. Second, they can be used by the Python interpreter to check your code for errors at runtime, saving you from some frustrating bugs.
from joblib  import load # con esto cargamos el modelo
from joblib import load
from sklearn.pipeline import Pipeline # type hint
from pydantic import BaseModel # type hint
from pandas import DataFrame # type hint
import os
from io import BytesIO

# cargamos el modelo:
def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH', 'model/model.pkl') # podemos especifiar dónde esta el modelo para q la Api lo use.
    with open(model_path, 'rb') as model_file: # Se leeran Bytes
        model = load(BytesIO(model_file.read())) # Instanciamos el modelo en Bytes y lo entregamos
    return model

# para hacer la predicción:
def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key: [value] for key, value in class_model.dict().items()}
    data_frame =  DataFrame(transition_dictionary)
    return data_frame
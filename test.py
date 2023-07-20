# Importo el cliente para testing 
from fastapi.testclient import TestClient
# importamos la instancia de fast API en nuestro main
from api.main import app

# Para inicializar se crea un cliente, y con esto se pueden crear las funciones para el testeo
client = TestClient(app)

# Primero el null prediction, i.e. con las características en cero:
def test_null_prediction():
    response = client.post('/v1/prediction', json = {
                                                    "opening_gross": 0,
                                                    "screens": 0,
                                                    "production_budget": 0,
                                                    "title_year": 0,
                                                    "aspect_ratio": 0,
                                                    "duration": 0,
                                                    "budget": 0,
                                                    "imdb_score": 0
                                                    }
                           )
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] >= 0
    
# Ahora para valores diferentes de cero:
def tets_random_prediction():
    response = client.post('/v1/prediction', json = {
                                                    "opening_gross": 8330681,
                                                    "screens": 2271,
                                                    "production_budget": 13000000,
                                                    "title_year": 1999,
                                                    "aspect_ratio": 1.85,
                                                    "duration": 97,
                                                    "budget": 1600000,
                                                    "imdb_score": 7.2
                                                    }
                           )
    
    assert response.status_code == 200
    assert response.json()['worlwide_gross'] != 0
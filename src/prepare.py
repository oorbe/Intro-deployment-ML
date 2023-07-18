from dvc import api # Para conección == cosola-bash
import pandas as pd
from io import StringIO # PAra cuando descarguemos los archivos
import sys
import logging # Para creación de logger

# Creamos configuración basica del loggin:
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)
logging.info('Fetching data..')

movie_data_path     = api.read('dataset/movies.csv', remote='dataset-track', encoding='utf8') 
financial_data_path = api.read('dataset/finantials.csv', remote='dataset-track', encoding='utf8') 
opening_data_path   = api.read('dataset/opening_gross.csv', remote='dataset-track', encoding='utf8')

movie_data = pd.read_csv(StringIO(movie_data_path)) 
fin_data = pd.read_csv(StringIO(financial_data_path)) 
opening_data = pd.read_csv(StringIO(opening_data_path)) 
  
numeric_columns_mask = (movie_data.dtypes == float) | (movie_data.dtypes == int)
numeric_columns = [columns for columns in numeric_columns_mask.index if numeric_columns_mask[columns]]
movie_data = movie_data[numeric_columns + ['movie_title']]

fin_data = fin_data[['movie_title', 'production_budget', 'worldwide_gross']]

final_movie_data = pd.merge(fin_data, movie_data, on = 'movie_title', how = 'left')
full_movie_data  = pd.merge(opening_data, final_movie_data, on = 'movie_title', how = 'left')

full_movie_data = full_movie_data.drop(['gross', 'movie_title'], axis = 1)

final_movie_data.to_csv('dataset/data_wordwide_gross.csv', index=False)
full_movie_data.to_csv('dataset/full_data.csv', index = False)

logger.info('Data Fetched and prepared...')
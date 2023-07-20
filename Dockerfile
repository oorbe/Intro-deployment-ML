# La "imagen base" es la version de pyton que utilicé.   ¿qué es slim-buster?
FROM python:3.11.4-slim-buster

# Nuestro directorio de trabajo es app de ahora en adelante
WORKDIR /app

# Traemos los requerimientos de la api a la carpeta .==app
COPY api/requirements.txt .

# -U actualiza -U pip y luego 
RUN pip install -U pip && pip install -r requirements.txt

# copiamos todos los archivos de api a una carpeta que se llame api
COPY api/ ./api

# copiamos el modelo. recuerda ./==app
COPY model/model.pkl ./model/model.pkl

# Creamos un initializer. pues es la manera de desplgar api's de modulo fastapi
COPY initializer.sh .

# Damos los permisos de ejecución al archivo
RUN chmod +x initializer.sh

# Para documentación se crea en el puesto 8000, que por defecto de la exposición de la api de fasapi.
EXPOSE 8000

# Finalmente:
ENTRYPOINT [ "./initializer.sh" ]
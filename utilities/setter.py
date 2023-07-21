# Vamos a realizar un path para google apication credentials

# para leer varibles de ambiente
import os 

# el json dl secret esta codificado con base 64 y hay que decodearlo
from base64 import b64decode

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open('path.json', 'w') as json_file:
        # aqui se decode
        json_file.write(b64decode(key).decode())
        # en testing.yaml está esperando una salida por esto hacemos:
    print(os.path.realpath('path.json'))


if __name__ == '__main__':
    main()

"""
@author C. Salazar
@since 2022-05-10
@descrip Ejercicio de Flask
"""
#Inclusion de modulos
from flask import Flask

app = Flask('__main__')

@app.route('/', methods=['GET'])
def go_home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug = True, port=5000, host='0.0.0.0')
from flask import Flask, render_template

app = Flask(__name__)

# Lista de diccionarios de los países y capitales:
paises = [
   {'pais': 'Argentina', 'capital': 'Buenos Aires'},
   {'pais': 'Brasil', 'capital': 'Brasilia'},
   {'pais': 'Chile', 'capital': 'Santiago de Chile'},
   {'pais': 'Colombia', 'capital': 'Bogotá'},
   {'pais': 'Costa Rica', 'capital': 'San José'},
   {'pais': 'Paraguay', 'capital': 'Asunción'},
   {'pais': 'Perú', 'capital': 'Lima'}
]

# La ruta principal:
@app.route('/')
def mostrar_tabla():
    return render_template('tabla.html', paises=paises)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form.get('profesion')
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    nombre = session.get('nombre')
    lugar = session.get('lugar')
    numero = session.get('numero')
    comida = session.get('comida')
    tipo_prediccion = random.choice(['buena', 'mala'])

    if tipo_prediccion == 'buena': #Se agrego clases a los textos para poder agregarles diseño y color:
        mensaje = (
            f"Soy el adivino del Dojo, "
            f"<span class='nombre'>{nombre}</span> tendrá un viaje muy largo dentro de "
            f"<span class='numero'>{numero}</span> años a "
            f"<span class='lugar'>{lugar}</span> y estará el resto de sus días preparando "
            f"<span class='comida'>{comida}</span> para todas las personas que quiere."
        )
    else: #Mensaje que se puede dar de manera aleatoria:
        mensaje = (
            f"Soy el adivino del Dojo, "
            f"<span class='nombre'>{nombre}</span> tendrá "
            f"<span class='numero'>{numero}</span> años de mala suerte, nunca conocerá "
            f"<span class='lugar'>{lugar}</span> y jamás volvió a comer "
            f"<span class='comida'>{comida}</span>."
        )
    
    if session.get('profesion'):
        mensaje += f" Cambió de profesión y ahora es {session['profesion']}."

    return render_template('futuro.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

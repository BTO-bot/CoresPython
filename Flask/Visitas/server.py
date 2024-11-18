from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # La clave secreta para la sesión

@app.route('/')
def index():
    # Esto verifica si existe la sesión de visitas; si no es asi, la iniciara en 0
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1
    return render_template('index.html', visitas=session['visitas'])

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()  
    return redirect('/')  

@app.route('/incrementar_visitas')
def incrementar_visitas():
    if 'visitas' in session:
        session['visitas'] += 2
    else:
        session['visitas'] = 2  
    return redirect('/')

@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    try:
        incremento = int(request.form['incremento'])
    except ValueError:
        incremento = 1  

    if 'visitas' in session:
        session['visitas'] += incremento
    else:
        session['visitas'] = incremento
    return redirect('/')

@app.route('/reiniciar_visitas')# Cada vez que se reinicia el contador va incrementa el contador de los reinicios 
def reiniciar_visitas():

    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1

    session['visitas'] = 0  # Reiniciara el contador a 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template, Request
from firebase import firebase
from datetime import datetime

app = Blueprint('rutas', __name__, url_prefix='/')
bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)


@app.get('/')
def login():
    return render_template('login.html')

@app.get('/tuto')
def login_tutor():
    return render_template('vistaTutor.html')

@app.get('/alumn')
def login_alumn():
    return render_template('permissions_alumno.html')

@app.get('/error')
def error():
    return render_template('sin_conexion.html')

@app.get('/respaldo')
def respaldo():
    try:
        respaldo = bd.get('/treecko', '')
        fecha = datetime.now()
        fecha = fecha.strftime("%d-%m-%Y-%H:%M:%S")
        print(fecha)
        resultado = bd.put('/respaldo', fecha, respaldo)
        return 'Respaldo hecho satisfactoriamente'
    except Exception:
        return redirect('/error')
    
@app.route('/prueba')
def prueba():
    return render_template('vistaTutor.html')

@app.route('/admin/panel')
def panel_control():
    return render_template('panel_control.html')

@app.route('/actualizar/periodo')
def actualizar_periodo():
    ahora = datetime.now()
    mes = ahora.month
    año = ahora.year
    print(mes)
    if mes >= 1 and mes <= 4:
        bd.put('treecko', 'periodo', f'{año}-A')
    elif mes >= 5 and mes <= 8:
        bd.put('treecko', 'periodo', f'{año}-B')
    elif mes >= 9 and mes <= 12:
        bd.put('treecko', 'periodo', f'{año}-C')
    return 'Periodo actualizado'

@app.route('/respaldos')
def restaurar():
    respaldos = bd.get("/respaldo", "")
    data=[]
    for id in respaldos:
        datos = {
            "id": id,
            "boton": f'''<button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#eliminar">Restaurar</button>
                                    <div class="modal fade" id="eliminar" tabindex="-1" aria-labelledby="eliminarLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="eliminarLabel">¿Desea cargar este respaldo?</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <p>Estos datos sobreescribiran a los datos actuales</p>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-warning" data-bs-dismiss="modal"  onclick="location.href=``">Cancelar</button>
                                            <button type="submit" class="btn btn-success"  onclick="location.href=``">Restaurar</button>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                    '''
        }
        data.append(datos)
    return jsonify({"datos": data})
    # return data

# @app.route('/pruebaA')
# def prueba():
#     return render_template('header_alumno.html')

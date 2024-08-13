from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'u2jsmodvktmxthwk'
app.config['MYSQL_PASSWORD'] = 'JTSZ6HR3AMgW3HDo7ykz'
app.config['MYSQL_HOST'] = 'bwpeifpsxajflfti7mrf-mysql.services.clever-cloud.com' 
app.config['MYSQL_DB'] = 'bwpeifpsxajflfti7mrf'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/partidos')
def partidos():
    return render_template('partidos.html')

@app.route('/contacto')
def contacto():
    return render_template('contact.html')

@app.route('/podio/<deporte>')
def podio(deporte):
    cur = mysql.connection.cursor()
    query = """
        SELECT Equipo, Colegio, SCORE
        FROM Copa_renault
        WHERE Deporte = %s
        ORDER BY SCORE DESC
        LIMIT 3
    """
    cur.execute(query, (deporte,))
    top_teams = cur.fetchall()
    cur.close()
    return jsonify(top_teams)


# --------------SECCION ADMINS----------------

#cargar tabla1
@app.route('/ADMIN')
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Inscripcion')
    data1 = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault')
    data2 = cur.fetchall()
    cur.close()
    return render_template('ADMIN.html', Table1_inf = data1, Table2_inf = data2)



#agregar un equipo
@app.route('/add_team', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        # Código para manejar el formulario cuando se envía
        Equipo = request.form['Equipo']
        Colegio = request.form['Colegio']
        Deporte = request.form['Deporte']
        Categoria = request.form['Categoria']
        Telefono = request.form['Telefono']
        DNI = request.form['DNI']
        Correo = request.form['Correo']
        Miembros = request.form['Miembros']
        Acompañantes = request.form['Acompañantes']
        Vegetariano = request.form['Vegetariano']
        Celiaco = request.form['Celiaco']
        Diabetico = request.form['Diabetico']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Inscripcion (Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))
    else:
        # mostrar el formulario
        return render_template('add-team.html')


#TABLA DE EQUIPOS PRE_INCRIPCION

#cargar un equipo de la DB para modificacion de valores
@app.route('/edit/<string:id>')
def get_team(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Inscripcion WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit-team.html', team = data[0])

#actualizar un equipo de la DB
@app.route('/update/<string:id>', methods=['POST'])
def update_team(id):
    if request.method == 'POST':
        Equipo = request.form['Equipo']
        Colegio = request.form['Colegio']
        Deporte = request.form['Deporte']
        Categoria = request.form['Categoria']
        Telefono = request.form['Telefono']
        DNI = request.form['DNI']
        Correo = request.form['Correo']
        Miembros = request.form['Miembros']
        Acompañantes = request.form['Acompañantes']
        Vegetariano = request.form['Vegetariano']
        Celiaco = request.form['Celiaco']
        Diabetico = request.form['Diabetico']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Inscripcion 
            SET Equipo = %s,
                Colegio = %s,
                Deporte = %s,
                Categoria = %s,
                Telefono = %s,
                DNI = %s,
                Correo = %s,
                Miembros = %s,
                Acompañantes = %s,
                Vegetariano = %s,
                Celiaco = %s,
                Diabetico = %s
            WHERE id = %s
        """, (Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))
    else:
        # mostrar el formulario
        return render_template('edit-team.html')

#eliminar un equipo de la DB
@app.route('/delete/<string:id>')
def delete_team(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Inscripcion WHERE id = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))


#confirmacion de inscripcion VALIDA

@app.route('/cargar/<string:id>')
def cargar_team(id):
    cur = mysql.connection.cursor()
    
    # Obtener todos los datos necesarios de la tabla de origen utilizando el ID
    cur.execute('SELECT Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico FROM Inscripcion WHERE id = %s', [id])
    data = cur.fetchone()
    
    if data:
        # Insertar los datos en la nueva tabla
        cur.execute('INSERT INTO Copa_renault (Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', data)
        mysql.connection.commit()
        
        # Eliminar el equipo de la tabla de origen
        cur.execute('DELETE FROM Inscripcion WHERE id = %s', [id])
        mysql.connection.commit()
    
    cur.close()
    return redirect(url_for('admin'))


#TABLA DE EQUIPOS INSCRIPTOS

#dar puntos a un equipo
@app.route('/add/<string:id>')
def get_pts(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault WHERE id = %s', [id])
    SCORE = cur.fetchall()
    cur.close()
    return render_template('add-pts.html', score = SCORE[0])


@app.route('/add/<string:id>', methods=['POST'])
def add_pts(id):
    if request.method == 'POST':
        SCORE = request.form['SCORE']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Copa_renault 
            SET SCORE = %s
            WHERE id = %s
        """, (SCORE, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))
    
    
#trae la infomacion del equipo basado en el ID
@app.route('/get_info/<string:id>')
def get_team2(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault  WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('final-config.html', team = data[0])

#envia la informacion al formulario de edicion
@app.route('/config/<string:id>', methods=['POST'])
def config_team(id):
    if request.method == 'POST':
        Equipo = request.form['Equipo']
        Colegio = request.form['Colegio']
        Deporte = request.form['Deporte']
        Categoria = request.form['Categoria']
        Telefono = request.form['Telefono']
        DNI = request.form['DNI']
        Correo = request.form['Correo']
        Miembros = request.form['Miembros']
        Acompañantes = request.form['Acompañantes']
        Vegetariano = request.form['Vegetariano']
        Celiaco = request.form['Celiaco']
        Diabetico = request.form['Diabetico']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Copa_renault 
            SET Equipo = %s,
                Colegio = %s,
                Deporte = %s,
                Categoria = %s,
                Telefono = %s,
                DNI = %s,
                Correo = %s,
                Miembros = %s,
                Acompañantes = %s,
                Vegetariano = %s,
                Celiaco = %s,
                Diabetico = %s
            WHERE id = %s
        """, (Equipo, Colegio, Deporte, Categoria, Telefono, DNI, Correo, Miembros, Acompañantes, Vegetariano, Celiaco, Diabetico, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))
    else:
        # mostrar el formulario
        return render_template('final-config.html')

#eliminar un equipo de la DB
@app.route('/delete/<string:id>', methods=['POST'])
def eliminar_team(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Copa_renault WHERE id = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))





if __name__ == '__main__':
    app.run(port=2500, debug=True)

from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/inscripcion')
def inscripcion():
    return render_template('inscripcion.html')

#fin de rutas general

@app.route('/ADMIN')
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault')
    data = cur.fetchall()
    cur.close()
    return render_template('ADMIN.html', teams=data)

#agregar un equipo
@app.route('/add_team', methods=['POST'])
def add_team():
    if request.method == 'POST':
        Equipo = request.form['Equipo']
        Colegio = request.form['Colegio']
        Deporte = request.form['Deporte']
        Categoria = request.form['Categoria']
        Telefono = request.form['Telefono']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Copa_renault (Equipo, Colegio, Deporte, Categoria, Telefono) VALUES (%s, %s, %s, %s, %s)',
                    (Equipo, Colegio, Deporte, Categoria, Telefono))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))

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




#cargar un equipo de la DB para modificacion de valores
@app.route('/edit/<string:id>')
def get_team(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Copa_renault WHERE id = %s', [id])
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
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Copa_renault 
            SET Equipo = %s,
                Colegio = %s,
                Deporte = %s,
                Categoria = %s,
                Telefono = %s
            WHERE id = %s
        """, (Equipo, Colegio, Deporte, Categoria, Telefono, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))

#eliminar un equipo de la DB
@app.route('/delete/<string:id>')
def delete_team(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Copa_renault WHERE id = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(port=2500, debug=True)

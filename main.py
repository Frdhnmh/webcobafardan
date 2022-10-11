from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#koneksi ke db
app.secret_key = 'bebasya'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQLPASSWORD'] = ''
app.config['MYSQL_DB'] = 'kempinski'
mysql = MySQL(app)



@app.route('/')
def home():
    return render_template('index.html')

#TAMPILDATACUSTOMER
@app.route('/admin')
def tampildatacustomer():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer ORDER BY  id DESC")
    datatampil = cur.fetchall()
    cur.close()
    return render_template('admin.html', datapemesan = datatampil)


#insert into
@app.route('/', methods=['POST'])
def customerinsert():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        phone = request.form['phone']
        tipe = request.form['tipe']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        jml = request.form['jml']
        ket = request.form['ket']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer (nama, email, phone, tipe, checkin, checkout, jml, ket) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (nama, email, phone, tipe, checkin, checkout, jml, ket))
        mysql.connection.commit()
        flash("Data Berhasil Dikirim dan Tersimpan")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
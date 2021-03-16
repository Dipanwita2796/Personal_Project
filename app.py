from flask import Flask, render_template, request, redirect, url_for, session 
from flask_mysqldb import MySQL 
import MySQLdb.cursors
import re 


app = Flask(__name__) 
app.config['DEBUG'] = True
app.secret_key = 'mithu'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'system'
app.config['MYSQL_PASSWORD'] = 'dipanwita'
app.config['MYSQL_DB'] = 'logindemo'

mysql = MySQL(app) 

@app.route('/') 
@app.route('/login', methods =['GET', 'POST']) 
def login(): 
	msg = '' 
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form: 
		email = request.form['email'] 
		password = request.form['password'] 
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
		cursor.execute('SELECT * FROM cust WHERE email = % s AND password = % s', (email, password )) 
		cust = cursor.fetchone() 
		if cust: 
			session['loggedin'] = True
			session['email'] = cust['email'] 
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg) 
		else: 
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg) 

@app.route('/logout') 
def logout(): 
	session.pop('loggedin', None)
	session.pop('email', None) 
	return redirect(url_for('login')) 

@app.route('/register', methods =['GET', 'POST']) 
def register(): 
	msg = '' 
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form: 
		email = request.form['email'] 
		password = request.form['password'] 
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
		cursor.execute('SELECT * FROM cust WHERE email = % s', (email, )) 
		account = cursor.fetchone() 
		if account: 
			msg = 'Account already exists !'
		else: 
			cursor.execute('INSERT INTO cust VALUES (% s, % s)', (email, password )) 
			mysql.connection.commit() 
			msg = 'You have successfully registered !'
	elif request.method == 'POST': 
		     msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg) 
if __name__ == '__main__':
    app.run()

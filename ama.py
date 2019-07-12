from flask import Flask,render_template,request,redirect,url_for,session


app=Flask(__name__)
app.secret_key='hello'

@app.route('/')

def home():

	return render_template('home1.html',title='home')

@app.route('/about')
def about():

	return render_template('about.html',title='about')
@app.route('/contact')
def contact():

	return render_template('contact.html',title='contact')
@app.route('/login',methods=['GET','POST'])
def login():
	users={'user1':'123','user2':'234','user3':'345','user4':'456'}
	username = request.form['username']
	password = request.form['password']

	if username not in users:
		return 'user does not exist,go back and enter a valid username'
	if users[username]!=password:
		return 'password does not match,go back and enter a valid password'

	session['username'] = username

	#return render_template('home1.html',signin=True)
	return redirect(url_for('home'))

@app.route('/logout')
def logout():

	session.clear()
	return redirect(url_for('home'))

app.run(debug=True)
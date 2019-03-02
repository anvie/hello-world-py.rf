from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

CURRENT_USER = None

@app.route("/")
def hello():
    return render_template("index.html", name=CURRENT_USER)

# <% if param.with_auth %>
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    global CURRENT_USER
    name = request.form['name']
    password = request.form['password']

    if password == "123":
        CURRENT_USER = name
        return redirect("/", code=302)
    else:
        return render_template("login.html", error="Invalid password, try: 123")
    
    

def show_the_login_form():
    return render_template("login.html")

@app.route('/logout')
def logout():
    global CURRENT_USER
    CURRENT_USER = None
    return redirect("/", code=302)
# <% endif %>

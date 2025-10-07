from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def index ():
    return'Главная страница'
@app.route('/user/<username>')
def user_profile(username):
    return render_template ("hello.html",hame=username)
@app.route('/men')
def about():
    return"мужчины"
@app.route('/women')
def catalog ():
    return"женщины"
@app.route('/children')
def shop_now():
    return'о нас'
@app.route('/contact')
def contact():
    return"contact"

if __name__=='__main__': #точка входа нашей программы
    print("привет, мир")
    app.run (debug=True)

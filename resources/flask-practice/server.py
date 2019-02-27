from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html')

#/users => "This is user list"
@app.route('/user/<string:name>')
def user(name=None):
    return "Hello, {name}!".format(name=name)

@app.route('/about')
def about():
    return render_template('about.html')

# if error change host to 127.0.0.1
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

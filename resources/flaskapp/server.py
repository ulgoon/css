from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# users
@app.route('/users')
def show_user():
    result = 1 + 2
    return str(result)

# signup
@app.route('/signup')
def signup():
    return "under construction!!"

@app.route('/admin')
def admin():
    return "You shouldn't be here."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

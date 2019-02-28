from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET','POST'])
def users(msg="Failed"):
    if request.method == 'GET':
        conn = lite.connect('./data/users.db')
        conn.row_factory = lite.Row
        cur = conn.cursor()

        cur.execute('SELECT * FROM users;')
        rows = cur.fetchall()
        conn.close()
        print(rows)
        return render_template('users.html', rows=rows)
    elif request.method == 'POST':
        try:
            input_username = request.form["username"]
            input_password = request.form["userpw"]
            input_gender = request.form["gender"]
            input_email = request.form["usermail"]
            print(input_username)
            with lite.connect('./data/users.db') as conn:
                cur = conn.cursor()
                cur.execute("""
                        INSERT INTO users(username, password, gender, email)
                        VALUES(?,?,?,?)
                        """, (input_username, input_password, input_gender, input_email))
                conn.commit()
                msg = "Success"
        except:
            conn.rollback()
            msg = "Failed"
        finally:
            return render_template("users.html", msg=msg)
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

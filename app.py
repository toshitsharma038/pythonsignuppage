from flask import Flask,request,render_template
from datetime import datetime
import psycopg2 

app = Flask(__name__)

#cooncection to database

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="signup_db",
        user="postgres",
        password="cdac"
 )



@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week =day_of_week,current_time = current_time)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')    
    email = request.form.get('email')   
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO users (name,email) VALUES(%s,%s)",(name,email))

    conn.commit()
    cur.close()
    conn.close()
    return  "Registraton sucessfull"

@app.route("/view")
def get_Data():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()

    for item in data:
        print(item[1])
        print(item[2])

    conn.commit()
    cur.close()
    conn.close()
    return "All registered user data"  

if __name__ == '__main__':
    app.run(debug=True);    
   
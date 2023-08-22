from flask import Flask,render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD']="Sandhya@2001"
app.config['MYSQL_DB']="cv"
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == "POST":
      username=request.form['name']
      subject=request.form['subject']
      email=request.form['email']
      message=request.form['message']
      cur = mysql.connection.cursor()
      cur.execute("Insert into data(name,subject,email,message) values(%s,%s, %s,%s)",(username,subject,email,message))
      mysql.connection.commit()
      cur.close()
      return "success"
   return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True)
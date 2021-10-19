from flask import Flask
from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ec24*01/01_20'
app.config['MYSQL_DB'] = 'bankDB'

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('homepage.html')

@app.route('/customer')       
def example(): 
   cur = mysql.connection.cursor()
   result = cur.execute("SELECT * FROM customer") 
   if result > 0:
       customer = cur.fetchall()
       return render_template("customer.html", customer=customer)

@app.route("/transferhistory")
def transhistory():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM history")
    if result > 0:
        history = cur.fetchall()
        return render_template('transhistory.html', history=history)


@app.route("/transfer",methods=['GET','POST'])
def transaction():
    if request.method == 'POST':
        sacc = request.form.get('sacc')
        racc = request.form.get('racc')
        amt = request.form.get('amt')
        sname = request.form.get('sname')
        rname = request.form.get('rname')
        amount = request.form.get('amount')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET balance = balance - %s WHERE  account = %s" , (amt,sacc))
        cur.execute("UPDATE customer SET balance = balance + %s WHERE  account = %s" , (amt,racc))
        cur.execute("INSERT INTO history (sender ,  receiver ,  amount) VALUES (%s,%s,%s)" , (sname,rname,amount))
        mysql.connection.commit()
        cur.close()
        print("success")
    else:
        print("did not insert")
    return render_template('transfer.html' )

        


    
if __name__ == "__main__":
    app.debug = True
    app.run()
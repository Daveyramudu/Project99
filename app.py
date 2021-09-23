from logging import debug
from flask import Flask, render_template, redirect, request
import sqlite3
import os 

app = Flask(__name__)
picFolder = os.path.join("static", "pics")
app.config["UPLOAD_FOLDER"] = picFolder




#c.execute("SELECT * FROM value")
#print(c.fetchall())

@app.route('/', methods=['GET',"POST"])
def home():

    nature2 = os.path.join(app.config["UPLOAD_FOLDER"] , "nature2.jpg")



    conn = sqlite3.connect("windows.db")
    c = conn.cursor()



    if request.method == "POST":
        num1 = request.form.get('num1')
        #c.execute("INSERT INTO plugins(num1) VALUES(?)",[num1])
        #conn.commit
        num2 = request.form.get('num2')
        #c.execute("INSERT INTO plugins(num2) VALUES(?) ",[num2])
        #conn.commit
        
        add = int(num1) + int(num2)
        conn = sqlite3.connect("windows.db")    
        c = conn.cursor()
        #um1 = 100
        #um2 = 56
        #ult = 105
        c.execute("INSERT INTO plugins(num1,num2,result) VALUES(?,?,?)",(num1,num2, add))
        conn.commit()  
        c.close()

        return render_template('result.html', add=add, user_image = nature2 )
        #c.execute("INSERT INTO plugins(result) VALUES(?)",[result])
        #conn.commit
        
    return render_template('index.html',user_image = nature2 )
    


if __name__ == "__main__":
    app.run(debug=True) 
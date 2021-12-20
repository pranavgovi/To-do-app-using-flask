
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import todo
# from forms import delete
import sqlite3

conn = sqlite3.connect('rest.db',check_same_thread=False)
cursor = conn.cursor()



from datetime import datetime
yyy=0
l=[]
d={}
x=[]
sachin=[]
pranav=[]
copy={}
hello={}
r=[]


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db = SQLAlchemy(app)
# @app.route('/')
# def basic():
#     return render_template("samp.html")
@app.route('/',methods=['GET','POST'])

def form():
    form=todo()
    l=[]



    if(request.method=='POST'):
        command1 = """CREATE TABLE IF NOT EXISTS
               user(username TEXT ,task TEXT)"""


        cursor.execute(command1)
        cursor.execute("INSERT INTO user VALUES(?,?)", (request.form['username'],request.form['task']))

        cursor.execute("SELECT * from user LIMIT 1000")
        conn.commit()

        r = cursor.fetchall()
        print(r)




        for i in range(len(r)):
            if (r[i][0] not in d):
                x = []
                x.append(r[i][1])
                d[r[i][0]] = x
            else:
                if(r[i][1] not in d[r[i][0]]):
                    d[r[i][0]].append(r[i][1])

        # if(request.form['username'] not in d):
        #     r=[]
        #     r.append(request.form['task'])
        #     d[request.form['username']] = r
        # else:
        #     d[request.form['username']].append(request.form['task'])
        #
        # l.append(request.form['username'])
        # l.append(request.form['task'])
        # if(request.form['username']=='PRANAV'):
        #     pranav.append(request.form['task'])
        # if(request.form['username']=='SACHIN'):
        #     sachin.append(request.form['task'])



    return render_template('samp.html',form=form,l=l,xx=len(l),pra=len(pranav),sac=len(sachin),pranav=pranav,sachin=sachin)




@app.route("/display",methods=['GET','POST'])
def display():
    if(len(d))==0:

        for i in range(len(r)):
            if (r[i][0] not in d):
                x = []
                x.append(r[i][1])
                d[r[i][0]] = x
            else:
                if(r[i][1] not in d[r[i][0]]):
                    d[r[i][0]].append(r[i][1])

        return render_template('display.html', dictt=d)
    else:
        print("hellllllloo")
        print(d)
        return render_template('display.html', dictt=d)








@app.route("/update.html",methods=['GET','POST'])
def update():
    return render_template("update.html")
@app.route("/delete.html",methods=['GET','POST'])
def delete():
    return render_template('delete.html')
@app.route("/display_delete.html",methods=['GET','POST'])
def disp():
    username = request.form.get("username")
    task = request.form.get("task")
    print(username)
    print(task)


    command = """ DELETE FROM user
                       WHERE username=username
                        AND task=task;
                   """

    cursor.execute("SELECT * from user LIMIT 1000")

    # com = """ DELETE FROM user
    #        WHERE username=yyy """
    #
    # cursor.execute(com)
    # conn.commit()

    f = cursor.fetchall()
    for i in range(len(f)):
        if (f[i][0] not in d):
            x = []
            x.append(f[i][1])
            d[f[i][0]] = x
        else:
            if (f[i][1] not in d[f[i][0]]):
                d[f[i][0]].append(f[i][1])
    for key in d.keys():
        if key == username:
            print("enrty 1")
            for i in d[key]:
                if i == task:
                    print("entry 2")
                    d[key].remove(i)





    return render_template('display_delete.html',dictt=d)





if __name__ == "__main__":
    app.run(debug=True)








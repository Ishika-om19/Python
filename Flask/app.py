from flask import Flask,render_template

from flask import request
app=Flask(__name__) #creating the Flask class object

@app.route('/')   #If you Put @ before any Name it
#becomes a Decorator
def home():
    return("<Center><H3>Welcome To Our Website</Center></H3>")

@app.route('/welcome') #Decorator being Used to add URL
def showmessage():
    return("<B><Font Color=Brown Face='sans serif'>New Courses</Font>")

@app.route('/lab')
def lab():
    return render_template("lab.html")

@app.route('/home/<uname>')
def home1(uname):
    return ("<Marquee width=100% Size=14 BgColor=Pink><Font Color=Red>Welcome To Orange</Font></Marquee><Br><Br><B><Font Size=6 Color=Orange>Welcome : "+uname+"</Font></B>")

if __name__=='__main__':
    app.run(debug=True) #Flask Application will be Started

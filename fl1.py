from flask_sqlalchemy import SQLAlchemy
from flask import  request,  url_for, redirect, render_template
from passlib.hash import sha256_crypt
from flask import Flask,session
app = Flask(__name__)
app.secret_key = '6565hhgrrerre=='
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/testingflaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class registration(db.Model):
    id= db.Column('studentid',db.Integer,primary_key=True)
    name= db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    add = db.Column(db.String(100))
    pincode=db.Column(db.String(100))
    dateofbirth=db.Column(db.String(100))

    def __init__(self,name,email,password,add,dateofbirth,pincode):
        self.name=name
        self.email=email
        self.password=password
        self.add=add
        self.dateofbirth=dateofbirth
        self.pincode=pincode









employee=[
    {"name":"vipin",
     "experience":"fresher",
     "education":"BCA" ,
     },
     {"name":"ritik",
     "experience":"2years",
     "education":"BCA",
     },

    {
    "name":"sid",
     "experience":"fresher",
     "education":"BCA",
    }
]

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html",employee=employee)


@app.route("/blog/<int:score>/<string:author>")
def blogs(score,author):
    return render_template("blog.html",score=score,author=author)

@app.route("/registrationform")
def register():
    return render_template("regis.html",name="this is contact form")


@app.route("/createreg", methods=['GET','POST'])
def getreg():
    if(request.method == 'POST'):
        secure_password=sha256_crypt.encrypt(str(request.form['password']))
        reg=registration(request.form['name'],request.form['email'],secure_password,request.form['dateofbirth'],request.form['add'],request.form['pincode'])
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('showdata'))

@app.route("/showdata")
def showdata():
    if not session.get("isLogin"):
        return redirect(url_for('login'))
    else:

        return render_template("showdatabase.html", registration=registration.query.all())

@app.route("/login")
def login():
    if not session.get("isLogin"):
        return render_template("loginform.html", name="Hello about me page")
    else:
        return redirect(url_for('showdata'))







@app.route("/loginforms",methods=['GET','POST'])
def loginforms():
    if (request.method=='POST'):
        username=request.form['email']
        password= request.form['password']
        reguser=registration.query.filter_by(email=username).first()
        if sha256_crypt.verify(password,reguser.password):
            session['isLogin']=True
            return redirect(url_for('showdata'))
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session['isLogin'] = None
    return redirect(url_for("login"))


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)


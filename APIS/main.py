from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#-------------------------------SQL___________--------------------------------------
#SQL caller--- database file name
#sqlite3 Appointments.db
class Appointments(db.Model):
    id = db.Column(db.Integer,autoincrement=True ,primary_key=True,unique=True)
    name = db.Column(db.String(80))
    contact=db.Column(db.String(80))
    clinic=db.Column(db.String(80))
    doctor=db.Column(db.String(80))
    date=db.Column(db.String(80))
    time=db.Column(db.String(80))
    
    def __repr__(self):
        return f"{self.name} -- {self.contact}--{self.clinic}--{self.doctor}--{self.date}--{self.time}"

#from main import db
@app.route('/index')
@app.route('/')
def index():
        # Handle POST Request heres
    return render_template("index.html")

@app.route("/view")  
def view():  
    con = sqlite3.connect("Appointments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Appointments")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)   

#Get List Of All Appointments
@app.route('/appointments')
def get_list_of_All_Appointments():
    appointments = Appointments.query.all()

    output=[]
    for appointment in appointments:
        appoinments_data = {'Id':appointment.id,'Patient Name':appointment.name,'Contact-No':appointment.contact,'Clinic':appointment.clinic,'Doctor Name':appointment.doctor,'Date':appointment.date,'Time':appointment.time}

        output.append(appoinments_data)
    return {"Appointments":output}

#---------------------------------------------
#Get list of Appointments By ID
@app.route('/appointments/<id>')
def get_appointment_by_id(id):
    appointment=Appointments.query.get_or_404(id)
    return {'ID':appointment.id,'Patient Name':appointment.name,'Contact-No':appointment.contact,'Clinic':appointment.clinic,'Doctor Name':appointment.doctor,'Date':appointment.date,'Time':appointment.time}

#______________-------------------------------
#Post Appointments
@app.route('/appointment',methods=['POST'])
def add_appointment():
    appointment= Appointments(name=request.json['Name'],clinic=request.json['Clinic'],doctor=request.json['Doctor'],date=request.json['Date'],time=request.json['Time'],contact=request.json['Contact'])
    db.session.add(appointment)
    db.session.commit()
    return {'statusCode':200,
            'headers':{'Content-Type':'application/json'},
      'body':{'ID':appointment.id,'Patient Name':appointment.name,'Contact-No':appointment.contact,'Clinic':appointment.clinic,'Doctor Name':appointment.doctor,'Date':appointment.date,'Time':appointment.time}
            }


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
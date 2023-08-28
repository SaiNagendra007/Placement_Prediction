import util
#import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)
global result
@app.route('/')
def home():
   return render_template('home.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':

       name=str(request.form['namec'])
       Internships=int(request.form['Internships'])
       Age=int(request.form['Age'])
       CGPA=int(request.form['CGPA'])
       hostel=int(request.form['hostel'])
       hob=int(request.form['hob'])
       branch=str(request.form['branch'])
       print(name,Internships,Age,CGPA,hostel,hob,branch)
       ans=util.prediction(Internships,Age, CGPA, hostel, hob, branch)

       print(ans)
       if int(ans)==0:
           s='Not Placed'
       else:
           s='Placed'''
       return render_template('result.html',name=name, ans=s)
   

if __name__ == '__main__':
   util.load_artifacts()
   app.run()

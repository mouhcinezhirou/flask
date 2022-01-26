from flask import Flask, request , render_template , flash
from utils import Methode_Coutmin,Methode_NordOuest,f_reg
import pandas as pd
import numpy as np
import json, os

app = Flask(__name__)
app.secret_key = "Devops_ESTEM"
from flask import render_template


def CopyFileToDirectory(file_data):
    try :
        file_data.save(os.path.join("./", file_data.filename))
        abs_path = os.path.abspath(file_data.filename)
        os.rename(abs_path,os.path.abspath("D.xlsx"))
        return True
    except Exception as e:
        print("Could not copy the file the Directory")
        return False

@app.route('/upload',methods=['POST'])
def hello():
    #print("request", request)
    #""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return json.dumps({'code': '402','message': 'No file to upload'})

        
        f = request.files['file']
        if CopyFileToDirectory(f):
            #print(f)
            name_f = "D.xlsx"
            n = int(request.form.get('n'))
            m = int(request.form.get('m'))
            method = request.form.get('method')

           
            if method == str(0):
                result = Methode_Coutmin(n,m,name_f)
            elif method == str(1):
                print("in ---")
                result = Methode_NordOuest(n,m,name_f)
            elif method == str(2):
                result = f_reg(n,m,name_f)

        return render_template('index.html', name=result )
    #"""

@app.route('/')
def start():
    return render_template('start.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('Steel_Industry_Energy_Consumption.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    lagcurrentrp = float(request.form.get('lagcurrentrp'))
    leadcurrentrp = float(request.form.get('leadcurrentrp'))
    lagcurrentpf = float(request.form.get('lagcurrentpf'))
    leadcurrentpf = float(request.form.get('leadcurrentpf'))
    nsm = float(request.form.get('nsm'))
    weekstatus = float(request.form.get('weekstatus'))
    dayofweek = float(request.form.get('dayofweek'))
    loadtype = float(request.form.get('loadtype'))
    month = request.form.get('month')


    result = model.predict(np.array([lagcurrentrp,leadcurrentrp,lagcurrentpf,leadcurrentpf,nsm,weekstatus,dayofweek,loadtype,month]).reshape(1, 9))

    return render_template('result.html', result=float(result))



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('hiv.pkl', 'rb'))

@app.route('/')
def home():
    res = ''
    return render_template('index.html', **locals())
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    age = int(request.form['age'])
    std = int(request.form['std'])
    past = int(request.form['past'])
    aids = int(request.form['aids'])
    partner = int(request.form['partner'])
    sexuality = int(request.form['sexuality'])
    drugs = int(request.form['drugs'])
    result = model.predict([[age,std,past,aids,partner,sexuality,drugs]])
    if(result[0]==1):
        res = 'Please Consult your Doctor!! You may have HIV'
    else:
        res = 'Relax!! You dont have chances of HIV for Now'
    return render_template('index.html', **locals())
if __name__ == '__main__':
    app.run(debug=True)
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import sklearn
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open('./Save_Model/model.pkl', 'rb'))
print(model)

@cross_origin()
@app.route('/', methods=['GET'])
def home():
    print("Inside home page")
    return render_template('./index.html')

@cross_origin()
@app.route('/home/info', methods=['GET'])
def info():
    return render_template('./infopage.html')

@cross_origin()
@app.route('/home/developer', methods=['GET'])
def Developer():
    return render_template('./Developerpage.html')

@cross_origin()
@app.route('/home/contact', methods=['GET'])
def Contact():
    return render_template('./Contactpage.html')

@cross_origin()
@app.route('/index',methods=['GET'])
def index_page():
    print("Inside Index Page")
    return render_template('./index1.html')

@cross_origin()
@app.route('/index/predict',methods=['POST','GET'])
def predict():
    print("Inside model")
    if request.method == 'POST':
        print("inside model")
        area = float(request.form['Area'])
        perimeter = float(request.form['Perimeter'])
        compactness = float(request.form['Compactness'])
        Length_Kernel = float(request.form['Length Of Kernel'])
        Kernel_Width = float(request.form['Width Of Kernel'])
        asym_co = float(request.form['Asymmetry Coefficient'])
        Kernel_coeff_len = float(request.form['Len.Kernel Groove'])
        print(area)

        cols = ([[area, perimeter, compactness, Length_Kernel, Kernel_Width, asym_co, Kernel_coeff_len]])
        cols = np.array(cols)
        print(area)
        feat = cols
        print(feat)
        predictions = model.predict(feat)

        output = predictions

        print(output)

        if output == 1:
            return render_template('./index2.html', Prediction_text="It is Endosperm")
        elif output == 2:
            return render_template('./index2.html', Prediction_text="It is Germ")
        else:
            return render_template('./index2.html', Prediction_text="It is Bran")

    else:
        return render_template('./index.html')



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from UtterenceModel import predictUtterence
from DeepLearntFeatures import featureMean,feature20BinMeans

app = Flask(__name__)

@app.route("/",methods = ['POST'])
def UtterenceEmotionPrediction():
        file = request.files['audio']
        prediction = predictUtterence()
        print(prediction)
        return prediction

if __name__ == "__main__":
        app.run(host='0.0.0.0')

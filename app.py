from flask import Flask
from UtterenceModel import predictUtterence
from DeepLearntFeatures import featureMean,feature20BinMeans
from ConversationModel import predictConversationOffline

app = Flask(__name__)

@app.route("/")
def home():
        return "success"

@app.route("/utterence",methods = ['POST'])
def utterenceEmotionPrediction():
        file = request.files['audio']
        prediction = predictUtterence()
        print(prediction)
        return prediction

@app.route("/conversation/offline",methods = ['POST'])
def conversationEmotionPredictionOffline():
        #file = request.files['audio']
        prediction = predictConversationOffline("test")
        return ""

if __name__ == "__main__":
        app.run(host='0.0.0.0')

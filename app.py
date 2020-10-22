from flask import Flask, request
from UtterenceModel import predictUtterence
from DeepLearntFeatures import featureMean,feature20BinMeans
from ConversationModel import predictConversationOffline

app = Flask(__name__)

utterence_folder = './utterences/'

@app.route("/")
def home():
		return "success"

@app.route("/utterence",methods = ['POST'])
def utterenceEmotionPrediction():
		file = request.files['audio']
		utterence_path = utterence_folder+'utt.wav'
		file.save(utterence_path)
		prediction = predictUtterence(utterence_path)
		print(prediction)
		return str(prediction)

@app.route("/conversation/offline",methods = ['POST'])
def conversationEmotionPredictionOffline():
		#file = request.files['audio']
		prediction = predictConversationOffline("test")
		return ""

if __name__ == "__main__":
		app.run(host='0.0.0.0')

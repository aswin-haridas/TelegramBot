import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import json
import random
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn 
import tensorflow
import pickle
#nltk.download("punkt")
tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)

class Trainer():
    def __init__(self,threshold=0.7,ignore=['?','.',',']):
        self.stemmer = LancasterStemmer()
        self.intents = json.loads(open('intents.json').read())
        self.threshold = threshold
        self.training = []
        self.output = []
        self.model = None
        self.ignore = ignore
        self.words = []
        self.labels = []
        try:
            with open("data.pickle","rb") as f:
                self.words,self.labels,self.training,self.output = pickle.load(f)
        except:
            print("Failed to load pickle")
            return
        self.modeler()
    def modeler(self):
        tensorflow.compat.v1.reset_default_graph()
        net = tflearn.input_data(shape=[None,len(self.training[0])])
        net = tflearn.fully_connected(net,8)
        net = tflearn.fully_connected(net,8)
        net = tflearn.fully_connected(net,len(self.output[0]),activation="softmax")
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net)
        try:
            self.model.load("model.tflearn")
        except:
            self.model = tflearn.DNN(net)
            self.model.fit(self.training, self.output, n_epoch=1000, batch_size=8,show_metric=True)
            self.model.save("model.tflearn")

    def worder(self,s,words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words=[self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i]=1
        return numpy.array(bag)

main = Trainer()

def chat(text):
    results = main.model.predict([main.worder(text,main.words)])[0]
    results_index=numpy.argmax(results)
    if results[results_index] > main.threshold:
        tag = main.labels[results_index]
        for t in main.intents["intents"]:
            if t["tag"] == tag:
                responses= t["responses"]
        return random.choice(responses)
    return "I didn't get that"

#Add below on main code 
"""
def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = chat(text)
    update.message.reply_text(response)
"""
from flask import Flask, render_template, request
import pickle

tokenizer=pickle.load(open("models/cv.pkl", "rb"))
model=pickle.load(open("models/clf.pkl", "rb"))

app = Flask(__name__)

'''@app.route("/", methods=["GET", "POST"])
def home():
    #return "Hello World ! J'espère que ça va bien !"
    text=""
    if request.method=="POST":
        text=request.form.get("email-content")
    return render_template("index.html", text=text) '''

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():
    if request.method=="POST":
        email_text=request.form.get("email-content")
    tokenize_email=tokenizer.transform([email_text])
    prediction=model.predict(tokenize_email)
    prediction=1 if prediction==1 else -1
    return render_template("index.html", prediction=prediction, email_text=email_text)




if __name__ == "__main__":
    app.run(debug=True)
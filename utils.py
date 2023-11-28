import pickle

tokenizer=pickle.load(open("models/cv.pkl", "rb"))
model=pickle.load(open("models/clf.pkl", "rb"))


def make_prediction(email_text):
    tokenize_email=tokenizer.transform([email_text])
    prediction=model.predict(tokenize_email)
    prediction=1 if prediction==1 else -1
    return prediction
import joblib

model = joblib.load('linear_svm_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

label_mapping = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}
def predict_emotion(texts):
    num_instances = dict()
    vectors = vectorizer.transform(texts)
    preds = model.predict(vectors)
    for pred in preds:
        if label_mapping[pred] in num_instances:
            num_instances[label_mapping[pred]] += 1
        else:
            num_instances[label_mapping[pred]] = 1
    return num_instances
    # return [label_mapping[pred] for pred in preds]
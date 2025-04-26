import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC, LinearSVC



#data = pd.read_csv('tweet_sentiment.csv')
data = pd.read_parquet('tweet_data.parquet')

label_mapping = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}

tweets = data['text'].values
labels = data['label'].values

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tweets)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)


#model = RandomForestClassifier(n_estimators=100, random_state=42)
#model = SVC(kernel='linear', random_state=42) 
model = LinearSVC(C = 0.1, random_state=42)



model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_labels = [label_mapping[pred] for pred in y_pred]
y_test_labels = [label_mapping[true] for true in y_test]
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test_labels, y_pred_labels))



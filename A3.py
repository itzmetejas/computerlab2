import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import re

data = pd.read_csv('emails.csv')
data

X = data['text']
y = data['spam']

vectorizer = TfidfVectorizer()
X_Vectorized = vectorizer.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X_Vectorized,y,test_size=0.2,random_state=42)

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train,y_train)

y_pred = svm_classifier.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

class_report = classification_report(y_test,y_pred,target_names=['Not Spam','Spam'])
print(class_report)

def classify_email(subject):
  subject_vectorized = vectorizer.transform([subject])
  prediction = svm_classifier.predict(subject_vectorized)
  if prediction[0]==1:
    return "Spam"
  else:
    return "Not Spam"

user_input = input("Enter Subject: ")
result = classify_email(user_input)
print(result)


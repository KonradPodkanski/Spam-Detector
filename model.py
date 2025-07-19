import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "spam.csv")
    df = pd.read_csv(file_path, encoding="latin-1")[['v1', 'v2']]
    df.columns = ['label', 'message']
    df['label'] = df['label'].map({'spam': 1, 'ham': 0})
    return df


    # Debug – ile wiadomości spam vs ham
    print(df['label'].value_counts())
    return df

def train_and_predict(text):
    df = load_data()
    X = df['message']
    y = df['label']

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(class_weight='balanced', max_iter=1000))
    ])

    model.fit(X, y)


    return model.predict([text])[0]

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from load_test_data import load
from sklearn.metrics import classification_report

def classify(vectors, labels, train_text, task, type):
    # Random Splitting With Ratio 3 : 1
    train_vectors, test_vectors, train_labels, test_labels = train_test_split(vectors, labels, test_size=0.333)
    test_vectors, test_labels = load(train_text, task)

    
    # Initialize Model
    classifier = None
    if(type=="MNB"):
        classifier = MultinomialNB(alpha=0.7)
        classifier.fit(train_vectors, train_labels)
    elif(type == "GNB"):
        classifier = GaussianNB()
        classifier.fit(train_vectors, train_labels)
    elif(type == "CoNB"):
        classifier = ComplementNB(alpha=0.7)
        classifier.fit(train_vectors, train_labels)
    elif(type == "BNB"):
        classifier = BernoulliNB(alpha=0.7)
        classifier.fit(train_vectors, train_labels)
    elif(type=="KNN"):
        classifier = KNeighborsClassifier(n_neighbors=5)
        classifier.fit(train_vectors, train_labels)
    elif(type=="DT"):
        classifier = DecisionTreeClassifier()
        classifier.fit(train_vectors, train_labels)
    elif(type=="RF"):
        classifier = RandomForestClassifier(max_depth=50, random_state=0)
        classifier.fit(train_vectors, train_labels)
    elif(type=="LR"):
        classifier = LogisticRegression(multi_class='auto', solver='newton-cg',)
        classifier.fit(train_vectors, train_labels)

    else:
        print("Wrong Classifier Type!")
        return

    accuracy = accuracy_score(train_labels, classifier.predict(train_vectors))
    print("Training Accuracy:", accuracy)
    test_predictions = classifier.predict(test_vectors)
    #accuracy = accuracy_score(test_labels, test_predictions)
    report = classification_report(test_labels, test_predictions)
    print("Classifier report:", report)
    print("Confusion Matrix:", )
    print(confusion_matrix(test_labels, test_predictions))

import pickle
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, y = fetch_openml(name="mnist_784", version=1, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_jobs=-1)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

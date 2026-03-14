from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from src.duckdb.duckdb_processing import yield_training_batches
import numpy as np

scaler = StandardScaler()
model = SGDClassifier(loss="log_loss")

classes = np.array([0,1,2])
first = True

for X, y in yield_training_batches("sdss.duckdb", 10000):

    scaler.partial_fit(X)
    X = scaler.transform(X)

    if first:
        model.partial_fit(X, y, classes=classes)
        first = False
    else:
        model.partial_fit(X, y)

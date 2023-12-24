import numpy as np
import optuna
import pandas as pd
from sklearn.metrics import mean_squared_error, roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# import xgboost as xgb

from mlflow.tracking import MlflowClient
import mlflow


mlflow.set_tracking_uri("http://localhost:8080")


EXPERIMENT_NAME = "IRIS dataset classification"


data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print(df.head())

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=42)

mlflow_client = MlflowClient()

experiment_details = mlflow_client.get_experiment_by_name(EXPERIMENT_NAME)

if experiment_details is not None:
    experiment_id = experiment_details.experiment_id
else:
    experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)


with mlflow.start_run(experiment_id=experiment_id, run_name="iris dataset rf run") as run:
    # Log parameters
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("random_state", 0)
    mlflow.log_param("n_estimators", 100)
    clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=0)
    clf.fit(X_train, y_train)
    iris_predict_y = clf.predict(X_test)
    
    roc_auc_score_val = roc_auc_score(y_test, clf.predict_proba(X_test), multi_class='ovr')
    mlflow.log_metric("test roc_auc_score", roc_auc_score_val)
    
    accuracy_score = accuracy_score(y_test, iris_predict_y)
    mlflow.log_metric("test accuracy_score", accuracy_score)


    # Log model
    mlflow.sklearn.log_model(clf, artifact_path="model")

run_id = run.info.run_id
print('Run ID: {}'.format(run_id))

model_uri = "runs:/{}/sklearn-model".format(run_id)
mv = mlflow.register_model(model_uri, "RandomForestIrisModel")

mlflow.sklearn.save_model(clf, "model_clf_randomforest")

print("Name: {}".format(mv.name))
print("Version: {}".format(mv.version))

# logged_model = './mlruns/491607878003452865/{}/artifacts/model'.format(run_id)
logged_model = 'runs:/{}/model'.format(run_id)

# Load model as a PyFuncModel.
import pdb; pdb.set_trace()
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
predictions = loaded_model.predict(X_test)
print(predictions)
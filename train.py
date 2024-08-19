import pandas as pd
from pprint import pprint
import mlflow
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('bank.csv',sep= ";" )

# experiment name
mlflow.set_experiment('MLOPS')

X = df.drop("y", axis=1)
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(exclude=['object']).columns

# pprint(categorical_cols)
# pprint(numerical_cols)

with mlflow.start_run():
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', "passthrough", numerical_cols),
            ('cat', OneHotEncoder(handle_unknown= "ignore"), categorical_cols)
        ])
    model = RandomForestClassifier(random_state=42)
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
        ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    precision = precision_score(y_test, y_pred, pos_label='yes')
    recall = recall_score(y_test, y_pred, pos_label='yes')
    mlflow.log_metric("accuracy", str(accuracy_score(y_test, y_pred)))
    mlflow.log_metric("precision", str(precision))
    mlflow.log_metric("recall", str(recall))
    
    mlflow.sklearn.log_model(pipeline, "pipeline_random_forest")
    
    
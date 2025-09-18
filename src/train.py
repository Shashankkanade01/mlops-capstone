import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import mlflow
import mlflow.sklearn

def main():
    # Set experiment name (instead of "Default")
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("housing_price_prediction")

    # Read data
    df = pd.read_csv("data/housing.csv")
    X = df[["area"]]
    y = df["price"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Dummy params (for logging)
    learning_rate = 0.01
    epochs = 100

    with mlflow.start_run():
        # Log params
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Evaluate
        r2_score = model.score(X_test, y_test)
        mse = mean_squared_error(y_test, model.predict(X_test))

        print("Model R^2 Score:", r2_score)
        print("Model MSE:", mse)

        # Log metrics
        mlflow.log_metric("r2_score", r2_score)
        mlflow.log_metric("mse", mse)

        # Save model locally
        joblib.dump(model, "model.pkl")

        # Input example for MLflow (fixes warning)
        input_example = pd.DataFrame({"area": [1000]})

        # Log model artifact to MLflow (with signature)
        mlflow.sklearn.log_model(
            model,
            name="linear_regression_model",
            input_example=input_example
        )

if __name__ == "__main__":
    main()

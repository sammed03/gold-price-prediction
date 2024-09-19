# gold_price_prediction.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, confusion_matrix, ConfusionMatrixDisplay
import io

def load_data(start, end):
    data = yf.download('GC=F', start=start, end=end)
    data.reset_index(inplace=True)
    return data

def preprocess_data(data):
    data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    data.fillna(method='ffill', inplace=True)
    data['MA7'] = data['Close'].rolling(window=7).mean()
    data['MA30'] = data['Close'].rolling(window=30).mean()
    data['Price_Change'] = data['Close'].pct_change()
    data['Price_Volatility'] = data['Price_Change'].rolling(window=30).std()
    data.dropna(inplace=True)
    return data

def train_models(X_train, y_train):
    gbr_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    gbr_model.fit(X_train, y_train)
    rf_model.fit(X_train, y_train)
    return gbr_model, rf_model

def evaluate_models(gbr_model, rf_model, X_train, X_test, y_train, y_test):
    gbr_train_predict = gbr_model.predict(X_train)
    gbr_test_predict = gbr_model.predict(X_test)
    rf_train_predict = rf_model.predict(X_train)
    rf_test_predict = rf_model.predict(X_test)

    r2_train_gbr = r2_score(y_train, gbr_train_predict)
    r2_test_gbr = r2_score(y_test, gbr_test_predict)
    r2_train_rf = r2_score(y_train, rf_train_predict)
    r2_test_rf = r2_score(y_test, rf_test_predict)

    mae_gbr = mean_absolute_error(y_test, gbr_test_predict)
    mse_gbr = mean_squared_error(y_test, gbr_test_predict)
    mae_rf = mean_absolute_error(y_test, rf_test_predict)
    mse_rf = mean_squared_error(y_test, rf_test_predict)

    return r2_train_gbr, r2_test_gbr, r2_train_rf, r2_test_rf, mae_gbr, mse_gbr, mae_rf, mse_rf


def plot_correlation_heatmap(data):
    plt.figure(figsize=(10, 8))
    correlation = data.drop('Date', axis=1).corr()
    sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':8}, cmap='coolwarm')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

def plot_actual_vs_predicted(y_test, predictions, model_name):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(y_test, predictions, alpha=0.5, label=model_name)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    ax.set_xlabel('Actual Price')
    ax.set_ylabel('Predicted Price')
    ax.set_title(f'Actual vs Predicted Gold Price ({model_name})')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

def predict_future_price(model, X):
    return model.predict(X.iloc[-1:])[0]

def plot_gold_price_over_time(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Adj Close'], label='Adj Close')
    plt.xlabel('Date')
    plt.ylabel('Gold Price')
    plt.title('Gold Price Over Time')
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf



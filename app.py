# app.py
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
from gold_price_prediction import (load_data, preprocess_data, train_models, 
                                    evaluate_models, plot_correlation_heatmap, 
                                    plot_actual_vs_predicted, predict_future_price, 
                                    plot_gold_price_over_time)

# Streamlit app title
st.title("Gold Price Prediction App")

# Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f0f5;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for user input
with st.sidebar:
    st.header("User Input")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if start_date >= end_date:
        st.error("End date must be after start date.")
        st.stop()

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)

# Display instructions
st.write("### Instructions")
st.write("1. Select the start and end dates for which you want to analyze gold prices.")
st.write("2. Click the 'Predict' button to generate predictions and view results.")

# Predict button
if st.button("Predict"):
    # Validate date input
    if start_date >= end_date:
        st.error("Please ensure the end date is after the start date.")
    else:
        # Load and preprocess data
        gold_data = load_data(start_date, end_date)
        processed_data = preprocess_data(gold_data)

        # Display historical data
        st.write("### Historical Gold Data")
        st.dataframe(processed_data.tail())

        # Display key insights (statistics)
        st.write("### Key Insights")
        st.write(processed_data.describe())

        # Plot correlation heatmap
        st.write("### Correlation Heatmap")
        heatmap_buf = plot_correlation_heatmap(processed_data)
        st.image(heatmap_buf)

        # Prepare data for models
        X = processed_data.drop(['Date', 'Adj Close'], axis=1)
        y = processed_data['Adj Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train models
        gbr_model, rf_model = train_models(X_train, y_train)

        # Evaluate models
        r2_train_gbr, r2_test_gbr, r2_train_rf, r2_test_rf, mae_gbr, mse_gbr, mae_rf, mse_rf = evaluate_models(gbr_model, rf_model, X_train, X_test, y_train, y_test)

        # Display R-squared scores and metrics
        st.write(f"### Gradient Boosting Regressor Metrics")
        st.write(f"Train R-squared: {r2_train_gbr:.4f}")
        st.write(f"Test R-squared: {r2_test_gbr:.4f}")
        st.write(f"Test Mean Absolute Error: {mae_gbr:.4f}")
        st.write(f"Test Mean Squared Error: {mse_gbr:.4f}")

        st.write(f"### Random Forest Regressor Metrics")
        st.write(f"Train R-squared: {r2_train_rf:.4f}")
        st.write(f"Test R-squared: {r2_test_rf:.4f}")
        st.write(f"Test Mean Absolute Error: {mae_rf:.4f}")
        st.write(f"Test Mean Squared Error: {mse_rf:.4f}")

        
        # Plot actual vs predicted prices
        st.write("### Actual vs Predicted Prices")
        gbr_plot_buf = plot_actual_vs_predicted(y_test, gbr_model.predict(X_test), 'Gradient Boosting')
        rf_plot_buf = plot_actual_vs_predicted(y_test, rf_model.predict(X_test), 'Random Forest')

        st.image(gbr_plot_buf, caption='Gradient Boosting')
        st.image(rf_plot_buf, caption='Random Forest')

        # Predict future price
        gbr_future_price = predict_future_price(gbr_model, X)
        rf_future_price = predict_future_price(rf_model, X)

        st.write(f"### Predicted Gold Price for the next day")
        st.write(f"Gradient Boosting: ${gbr_future_price:.2f}")
        st.write(f"Random Forest: ${rf_future_price:.2f}")

        # Plot gold price over time
        st.write("### Gold Price Over Time")
        price_plot_buf = plot_gold_price_over_time(processed_data)
        st.image(price_plot_buf)

st.markdown('</div>', unsafe_allow_html=True)
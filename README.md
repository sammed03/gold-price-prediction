<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gold Price Prediction App</title>
</head>
<body>
    <div class="container">
        <header>
            <h1>Gold Price Prediction App</h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/15/Gold_bars.jpg" alt="Gold Bars" class="header-image">
        </header>
        <section>
            <h2>Why Gold as a Hedging Instrument?</h2>
            <p>Gold has been a trusted asset for centuries, often considered a safe haven during economic instability. Here are a few reasons why gold is widely recognized as a hedging instrument:</p>
            <ul>
                <li><strong>Inflation Protection:</strong> Gold tends to retain its value even as inflation rises, making it a reliable hedge against currency devaluation.</li>
                <li><strong>Market Volatility:</strong> In times of economic uncertainty, investors flock to gold, driving its prices up when other markets decline.</li>
                <li><strong>Diversification:</strong> Adding gold to a portfolio can reduce overall risk due to its low correlation with other asset classes, like stocks and bonds.</li>
            </ul>
        </section>
        <section>
            <h2>Project Features</h2>
            <ul>
                <li><strong>Real-time Gold Price Analysis:</strong> Get insights into historical gold prices and trends.</li>
                <li><strong>Predictive Modeling:</strong> Utilizes advanced algorithms to forecast future gold prices.</li>
                <li><strong>Interactive Visualizations:</strong> Analyze data through intuitive graphs and charts.</li>
            </ul>
        </section>
        <section>
            <h2>Algorithms Used</h2>
            <ul>
                <li><strong>Gradient Boosting Regressor:</strong> A powerful ensemble method that builds models sequentially to improve accuracy.</li>
                <li><strong>Random Forest Regressor:</strong> A robust method that combines multiple decision trees to enhance prediction reliability.</li>
            </ul>
        </section>
        <section>
            <h2>Project Pipeline</h2>
            <ol>
                <li>Data Collection: Historical gold price data is fetched using the <code>yfinance</code> library.</li>
                <li>Data Preprocessing: Data is cleaned and features like moving averages and price volatility are calculated.</li>
                <li>Model Training: The data is split into training and testing sets, and models are trained using Gradient Boosting and Random Forest algorithms.</li>
                <li>Evaluation: Model performance is assessed using metrics like R-squared and Mean Absolute Error.</li>
                <li>Prediction: Future gold prices are predicted based on the latest data.</li>
            </ol>
        </section>
        <section>
            <h2>Tech Stack</h2>
            <ul>
                <li><strong>Frontend:</strong> Streamlit</li>
                <li><strong>Backend:</strong> Python, Scikit-learn</li>
                <li><strong>Data Handling:</strong> Pandas, NumPy</li>
                <li><strong>Visualization:</strong> Matplotlib, Seaborn</li>
                <li><strong>Deployment:</strong> Render.com</li>
            </ul>
        </section>
        <section>
            <h2>Live Demo</h2>
            <p>You can explore the live application <a href="https://gold-price-prediction-hvab.onrender.com" target="_blank">here</a>.</p>
            <p><strong>Note:</strong> The site may experience request delays of 50 seconds or more. Please be patient while waiting for the response.</p>
        </section>
        <section>
            <h2>Getting Started</h2>
            <pre><code>git clone https://github.com/yourusername/gold-price-prediction.git
cd gold-price-prediction
pip install -r requirements.txt
streamlit run app.py</code></pre>
        </section>
        <footer>
            <p>&copy; 2024 Gold Price Prediction App. Licensed under the MIT License.</p>
        </footer>
    </div>
</body>
</html>

# Air Quality Time Series Analysis

## Overview
This repository contains a complete Time Series Analysis workflow applied to the **Air Quality UCI Dataset**. The project explores historical concentration levels of Carbon Monoxide (`CO(GT)`) to build and compare predictive models, focusing on identifying underlying seasonal patterns and testing different forecasting approaches.

## Workflow & Methodology
The analysis was conducted in `time_series_analysis.ipynb` and followed these main steps:

1. **Data Cleaning & Loading:** Replaced missing data placeholders (`-200`) with `NaN` and interpolated the missing values using time-based methods. Evaluated data on a daily frequency.
2. **Exploratory Data Analysis (EDA):** Visualized rolling means and observed variance patterns (e.g., winter peaks vs. summer drops).
3. **Transformations:** Applied Box-Cox and Logarithmic transformations to stabilize the variance. Followed by double differentiation (lag 7 and lag 1) to remove stochastic trends and the weekly seasonality.
4. **Stationarity Checks:** Verified the successful stationarity of the series using the Augmented Dickey-Fuller (ADF) test.
5. **Autocorrelation (ACF & PACF):** Analyzed autocorrelation and partial autocorrelation to estimate lag parameters for the autoregressive models, verifying results with the Ljung-Box test.
6. **Decomposition:** Extracted and visualized the series' Trend, Seasonal, and Residual components.
7. **Modeling:**
   - **Baseline OLS:** A simplistic linear regression model using calendar dummy variables to capture the basic "weekend vs. weekday" effect.
   - **AR(p) + Seasonal Dummies:** A custom Autoregressive model dynamically adapting to recent lags, guided by the PACF.
   - **SARIMA(3,1,1)(1,1,1,7):** A comprehensive Seasonal Autoregressive Integrated Moving Average model.
8. **Model Evaluation & Findings:** Models were evaluated using Mean Absolute Percentage Error (MAPE). We compared predictions over two horizons:
   - **Long-term (28 days):** All models tended to converge around a ~30% MAPE. This demonstrated the "**Memory Decay**" effect, where autoregressive models lose their recent momentum over time and collapse into flat seasonal averages.
   - **Short-term (3 days):** We observed a fascinating "**Inertia vs. Variance**" phenomenon. The complex SARIMA model performed poorly initially because it dragged the "inertia" of anomalous low values recorded at the end of the training set. Conversely, the simplistic OLS baseline ignored recent anomalies, capturing the immediate historical "normal" average and drastically outperforming the others.

## Dataset
- **Name:** Air Quality
- **Source:** UCI Machine Learning Repository
- **URL:** [Air Quality Dataset](https://archive.ics.uci.edu/dataset/360/air+quality)

**Citation:**
> Vito, S., Masseroli, M., Piga, M., & Pennazza, G. (2008). Air Quality. UCI Machine Learning Repository. [https://doi.org/10.24432/C59K5F](https://doi.org/10.24432/C59K5F)

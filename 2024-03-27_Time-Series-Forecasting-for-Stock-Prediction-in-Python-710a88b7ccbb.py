# Description: Short example for Time Series Forecasting for Stock Prediction in Python.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import yfinance as yf

tesla = yf.Ticker("TSLA")
df = tesla.history(period="5y")
df.head(10)

plt.figure(figsize=(17, 8))
plt.plot(df["Close"])
plt.title("Closing price of Tesla")
plt.ylabel("Closing price ($)")
plt.xlabel("Trading day")
plt.show()


def plot_moving_average(series, window, plot_intervals=False, scale=1.96):

    rolling_mean = series.rolling(window=window).mean()
    plt.figure(figsize=(17, 8))
    plt.title(f"Moving average\n window size = {window}")
    plt.plot(rolling_mean, "g", label="Rolling mean trend")
    # Plot confidence intervals for smoothed values
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bound, "r--", label="Upper bound / Lower bound")
        plt.plot(lower_bound, "r--")

    plt.plot(series[window:], label="Actual values")


plot_moving_average(df["Close"], 5)

plot_moving_average(df["Close"], 30)

plot_moving_average(df["Close"], 90, plot_intervals=True)


def exponential_smoothing(series, alpha):

    result = [series[0]]  # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])
    return result


def plot_exponential_smoothing(series, alphas):

    plt.figure(figsize=(17, 8))
    for alpha in alphas:
        plt.plot(exponential_smoothing(series, alpha), label=f"Alpha {alpha}")
    plt.plot(series.values, "c", label="Actual")
    plt.title("Exponential Smoothing")


plot_exponential_smoothing(df["Close"], [0.05, 0.3])


def double_exponential_smoothing(series, alpha, beta):

    result = [series[0]]
    for n in range(1, len(series) + 1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        value = np.where(n >= len(series), result[-1], series[n])
        last_level, level = level, alpha * value + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        result.append(level + trend)
    return result


def plot_double_exponential_smoothing(series, alphas, betas):

    plt.figure(figsize=(17, 8))
    for alpha in alphas:
        for beta in betas:
            plt.plot(
                double_exponential_smoothing(series, alpha, beta),
                label=f"Alpha {alpha}, beta {beta}",
            )
    plt.plot(series.values, label="Actual")
    plt.title("Double Exponential Smoothing")


plot_double_exponential_smoothing(df["Close"], alphas=[0.9, 0.02], betas=[0.9, 0.02])


def tsplot(y, lags=None, figsize=(12, 7), syle="bmh"):

    if not isinstance(y, pd.Series):
        y = pd.Series(y)

    with plt.style.context(style="bmh"):
        plt.figure(figsize=figsize)
        layout = (2, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        y.plot(ax=ts_ax)
        p_value = sm.tsa.stattools.adfuller(y)[1]
        ts_ax.set_title(f"Time Series Analysis Plots\n Dickey-Fuller: p={p_value:.5f}")
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax)


tsplot(df["Close"], lags=30)

data_diff = df["Close"] - df["Close"].shift(1)
tsplot(data_diff[1:], lags=30)

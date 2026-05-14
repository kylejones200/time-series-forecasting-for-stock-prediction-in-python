# Time Series Forecasting for Stock Prediction in Python

This project introduces common techniques to manipulate time series and make predictions using an example of a stock price. This project...

### Time Series Forecasting for Stock Prediction in Python 

This project introduces common techniques to manipulate time series and make predictions using an example of a stock price. This project is just an example, it is not financial advice. :)


<figcaption>Photo by <a class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Charles Jackson</a> on <a class="markup--anchor markup--figure-anchor"


#### Time series for financial forecasting
Motivation: I was asked to forecast corporate earnings based on different pricing scenarios for commodities next 5 years the challenge was how to have something that was Dynamic and could take into account various combination price changes including fluctuations in crude or natural gas price overall demand and investment Capital expenditures. The solution also needed to account for different Financial metrics and cost basis.

Data: The data is a sample the last 5 years of stock price for Tesla. You can easily change this to the company of your choice.

Analysis: Time series is not like normal data because the order of the data matters. We use different methods to look at the data so we can keep the order. There is a lot of volatility in the data which can be smoothed by looking at the data over longer time frames instead of daily values.

We can use quantitative forecasting methods when past information about the variable being forecast is available, the information can be quantified, and it is reasonable to assume that the pattern of the past will continue into the future.

We begin by importing the tools we need.


I'm using YFinance to get the data. There are other APIs that provide stock data. But this one is easy to use and free.


#### Exploratory data analysis (EDA)
A useful first step in selecting an appropriate forecasting method is to construct a time series plot. A time series plot is a graphical presentation of the relationship between time and the time series variable. Time is on the horizontal axis, and the time series values are shown on the vertical axis.

So, let's plot the data for the past five years.



The objective of time series analysis is to discover a pattern in the historical data or time series and then extrapolate the pattern into the future.

The forecast is based solely on past values of the variable and/or past forecast errors.

#### Moving average
We use the term *moving* because every time a new observation becomes available for the time series, it replaces the oldest observation in the equation. As a result, the average will change, or move, as new observations become available.

To use moving averages to forecast, we must first select the order *k*, or number of time series values, to be included in the moving average. A smaller value of *k* will track shifts in a time series more quickly than a larger value of *k*. If more past observations are considered relevant, then a larger value of *k* is better.


#### Smooth by the previous 5 days (by week)


#### Smooth by the previous month (30 days)


#### Smooth by previous quarter (90 days)


#### Exponential smoothing
This method is a special case of a weighted moving averages method; we select only the weight for the most recent observation.

The weights for the other data values are computed automatically and become smaller as the observations grow older.

The exponential smoothing forecast is a weighted average of all the observations in the time series.

The term *exponential smoothing* comes from the exponential nature of the weighting scheme for the historical values.



#### Double exponential smoothing
The time series is still noisy. We can apply double exponential smoothing to remove more noise.



#### Stationarity
Time series data can contain patterns that we want to identify and remove so we can create a "stationary" series.





#### Extensions
This could be extended using other time series techniques such as Amazon Web Services Deep AR algorithm or using simulation such as a Monte Carlo. The Monte Carlo takes account at the intrinsic variability volatility and the movements of the time series to predict that in the future.

#### Forecasting future values
There are several methods for forecasting future values including Bayesian Time Series that I demonstrate in this project.

[Time series for unemployment and natural gas using Prophet and Plotly\ *This simple project uses Bayesian time series to predict unemployment in the US. We visualize the data using Plotly...*medium.com](https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f "https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f")[](https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f)
### Related Stories
- [[Monte Carlo simulation using Black-Scholes for stock price in Python](https://medium.com/@kylejones_47003/monte-carlo-simulation-using-black-scholes-for-stock-price-in-python-808574935473)]
- [[Visualizing the normal distribution with Python and Matplotlib](https://medium.com/@kylejones_47003/visualizing-the-normal-distribution-with-python-and-matplotlib-c501e3c594f8)]
- [[Building a Recommendation Engine using Association Rules for item to item similarity in R](https://medium.com/@kylejones_47003/association-rules-for-item-to-time-personalization-in-r-9d6de7d6db8e)]

### In Plain English 🚀
*Thank you for being a part of the* [*In Plain English*](https://plainenglish.io) *community! Before you go:*

- Be sure to clap and follow the writer ️👏️️
- [Follow us: [X](https://twitter.com/inPlainEngHQ) \| [LinkedIn](https://www.linkedin.com/company/inplainenglish/) \| [YouTube](https://www.youtube.com/channel/UCtipWUghju290NWcn8jhyAw) \| [Discord](https://discord.gg/in-plain-english-709094664682340443) \| [Newsletter](https://newsletter.plainenglish.io/)]
- [Visit our other platforms: [Stackademic](https://stackademic.com/) \| [CoFeed](https://cofeed.app/) \| [Venture](https://venturemagazine.net/) \| [Cubed](https://blog.cubed.run)]
- [More content at [PlainEnglish.io](https://plainenglish.io)]

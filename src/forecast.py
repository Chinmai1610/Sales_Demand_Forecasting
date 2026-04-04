import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

class SalesForecaster:
    def __init__(self, data, target_column='sales'):
        self.data = data
        self.target_column = target_column
        self.model_fit = None
        self.metrics = {}

    def train_arima(self, order=(5, 1, 0)):
        """Trains the model and calculates accuracy metrics on the training set."""
        series = self.data[self.target_column].astype(float)
        model = ARIMA(series, order=order)
        self.model_fit = model.fit()
        
        # Calculate performance metrics
        predictions = self.model_fit.fittedvalues
        self.metrics['RMSE'] = np.sqrt(mean_squared_error(series, predictions))
        self.metrics['MAPE'] = mean_absolute_percentage_error(series, predictions) * 100
        return self.model_fit

    def generate_forecast(self, steps=30):
        if self.model_fit is None:
            self.train_arima()
        
        forecast_values = self.model_fit.forecast(steps=steps)
        last_date = self.data['date'].max()
        forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=steps, freq='D')
        
        return pd.DataFrame({'date': forecast_dates, self.target_column: forecast_values})
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(series):

    model = ARIMA(series, order=(5,1,0))

    model_fit = model.fit()

    return model_fit
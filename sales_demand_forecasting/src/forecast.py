import pandas as pd

def forecast_sales(model, steps=30):

    forecast = model.forecast(steps=steps)

    forecast_df = pd.DataFrame({
        "forecast_sales": forecast
    })

    return forecast_df
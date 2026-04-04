# Import required modules
from src.data_loader import load_data
from src.model_training import train_arima_model
from src.forecast import forecast_sales
from src.save_plot import save_forecast_plot

import pandas as pd


def main():

    print("Sales Demand Forecasting Project Started")

    # Load dataset
    data = load_data("data/sales_data.csv")

    # Set date column as index
    data.set_index("date", inplace=True)

    # Train ARIMA model
    print("Training forecasting model...")
    model = train_arima_model(data["sales"])

    # Forecast next 30 days
    print("Generating forecast...")
    forecast_df = forecast_sales(model, steps=30)

    # Generate future dates
    last_date = data.index[-1]
    forecast_dates = pd.date_range(start=last_date, periods=31, freq="D")[1:]

    forecast_df.index = forecast_dates

    # Save forecast results
    forecast_df.to_csv("outputs/forecast_results.csv")

    print("Forecast results saved to outputs/forecast_results.csv")

    # Save forecast visualization
    save_forecast_plot(data, forecast_df)

    print("Forecast plot saved to outputs/forecast_plot.png")

    print("Project completed successfully")


# Run program
if __name__ == "__main__":
    main()
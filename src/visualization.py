import matplotlib.pyplot as plt

def plot_forecast(df, forecast):

    plt.figure(figsize=(10,5))

    plt.plot(df["date"], df["sales"], label="Historical Sales")

    plt.plot(forecast.index, forecast["forecast_sales"], label="Forecast Sales")

    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.title("Sales Demand Forecast")

    plt.legend()

    plt.grid(True)

    plt.show()
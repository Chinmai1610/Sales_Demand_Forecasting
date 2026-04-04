import matplotlib.pyplot as plt

def save_forecast_plot(df, forecast):

    plt.figure(figsize=(10,5))

    plt.plot(df.index, df["sales"], label="Historical Sales")

    plt.plot(forecast.index, forecast["forecast_sales"], label="Forecast")

    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.title("Sales Demand Forecast")

    plt.legend()

    plt.grid(True)

    plt.savefig("outputs/forecast_plot.png")

    plt.close()

    print("Forecast plot saved to outputs/forecast_plot.png")
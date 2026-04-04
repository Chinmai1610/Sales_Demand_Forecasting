from sklearn.metrics import mean_absolute_error

def evaluate_model(actual, predicted):

    mae = mean_absolute_error(actual, predicted)

    print("Model Evaluation")
    print("----------------")
    print("Mean Absolute Error:", mae)
from sklearn.metrics import mean_squared_log_error


y_true = [3, 5, 2.5, 7]
y_pred = [7, 5.5, 2.6, 7]
msle = mean_squared_log_error(y_true, y_pred)  
print(msle)

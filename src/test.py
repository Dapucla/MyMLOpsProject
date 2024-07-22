import joblib

# Загрузите модель
model = joblib.load('models/model.pkl')

# Проверка, что модель загружена и может делать предсказания
assert model is not None
print("Model loaded successfully")

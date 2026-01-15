# keras.api.keras.models
from keras.models import load_model
file_path = 'model/facenet_keras.h5'
model = load_model(file_path)
print("Loaded")
print(model)

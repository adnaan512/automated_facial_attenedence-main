# # import numpy as np
# # import tensorflow as tf
# # from tensorflow.keras.models import Sequential
# # from tensorflow.keras.layers import Dense

# # # Generate random data
# # np.random.seed(0)
# # X_train = np.random.random((1000, 20))  # 1000 samples, 20 features each
# # y_train = np.random.randint(2, size=(1000, 1))  # Binary target

# # # Define a simple sequential model
# # model = Sequential([
# #     Dense(64, input_dim=20, activation='relu'),
# #     Dense(32, activation='relu'),
# #     Dense(1, activation='sigmoid')
# # ])

# # # Compile the model
# # model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# # # Train the model
# # model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# # # Save the model in H5 format
# # model.save('my_model.h5')


# import h5py
# file_path = 'model/facenet_keras.h5'

# try:
#     with h5py.File(file_path, 'r') as f:
#         print("File is a valid HDF5 file.")
        
# except OSError as e:
#     print(f"File is not a valid HDF5 file: {e}")

# import tensorflow as tf
# import keras

# print("TensorFlow version:", tf.__version__)
# print("Keras version:", keras.__version__)

# import h5py
# print("h5py:",h5py.__version__)


# import sys

# print("Python version:", sys.version)

import h5py
from tensorflow.keras.models import load_model

file_path = 'model/facenet_keras.h5'
new_file_path = 'model/modelx.h5'

# Verify the file is a valid HDF5 file
try:
    with h5py.File(file_path, 'r') as f:
        print("File is a valid HDF5 file.")
except Exception as e:
    print(f"Error: {file_path} is not a valid HDF5 file. Exception: {e}")
    exit()

# Load the model using Keras
try:
    model = load_model(file_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Save the model to a new file
try:
    model.save(new_file_path)
    print(f"Model saved successfully as {new_file_path}.")
except Exception as e:
    print(f"Error saving the model: {e}")

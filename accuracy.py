# import os
# import random
# import pickle
# from tensorflow.keras.models import load_model

# from Integrate import load_image, generate_DB
# from Recognize import recognize_face

# def calculate_accuracy():
#     # Generate the database
#     # generate_DB()

#     # Load the database from the pickle file
#     with open('database.pkl', 'rb') as pkl_file:
#         loaded_database = pickle.load(pkl_file)

#     # Load the model
#     model_path = 'model/facenet_keras.h5'
#     model = load_model(model_path)

#     # Get a list of all folders in the dataset
#     dataset_path = "new_105_classes_pins_dataset"
#     folders = os.listdir(dataset_path)

#     # Extract individual names from folder names
#     # individuals = [name.split("_")[-1].title() for name in folders]

#     # Initialize counters
#     total_images = 0
#     correct_predictions = 0

#     # Load 50 random images and predict their names
#     for _ in range(100):
#         # Randomly select a folder
#         folder = random.choice(folders)
#         folder_path = os.path.join(dataset_path, folder)

#         # Get a list of images in the folder
#         images = os.listdir(folder_path)

#         if images:
#             # Randomly select an image
#             image_name = random.choice(images)
#             image_path = os.path.join(folder_path, image_name)

#             # Load the image
#             img = load_image(image_path)

#             # Predict the name
#             predicted_name = recognize_face(model, img, loaded_database)

#             # Check if the predicted name matches the folder name
#             name = folder.split("_")[-1].title()
#             print("predicted_name: ",predicted_name," | name:", name)
#             if predicted_name == name:
#                 correct_predictions += 1

#             total_images += 1

#     # Calculate accuracy
#     accuracy = (correct_predictions / total_images) * 100 if total_images > 0 else 0

#     print(f"Total images: {total_images}")
#     print(f"Correct predictions: {correct_predictions}")
#     print(f"Accuracy: {accuracy:.2f}%")

# # Example usage
# calculate_accuracy()




import os
import random
import pickle
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from Integrate import load_image, generate_DB
from Recognize import recognize_face
from sklearn.metrics import confusion_matrix
import seaborn as sns

def calculate_confusion_matrix():
    # Load the database from the pickle file
    with open('database.pkl', 'rb') as pkl_file:
        loaded_database = pickle.load(pkl_file)

    # Load the model
    model_path = 'model/facenet_keras.h5'
    model = load_model(model_path)

    # Get a list of all folders in the dataset
    dataset_path = "new_105_classes_pins_dataset"
    folders = os.listdir(dataset_path)

    # Initialize confusion matrix
    num_classes = len(folders)
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)

    # Initialize counters
    total_images = 0
    correct_predictions = 0

    # Load random images and populate confusion matrix
    for _ in range(200):
        # Randomly select a folder
        actual_name = random.choice(folders)
        actual_index = folders.index(actual_name)

        # Randomly select an image from the folder
        folder_path = os.path.join(dataset_path, actual_name)
        images = os.listdir(folder_path)
        if images:
            image_name = random.choice(images)
            image_path = os.path.join(folder_path, image_name)

            # Load the image
            img = load_image(image_path)

            # Predict the name
            predicted_name = recognize_face(model, img, loaded_database)

            # Check if the predicted name is in the list of class names
            name = [name.split("_")[-1].title() for name in folders]

            if predicted_name in name:
                predicted_index = name.index(predicted_name)

                # Update confusion matrix
                confusion_matrix[actual_index][predicted_index] += 1

                # Update counters for accuracy calculation
                total_images += 1
                actual_name = actual_name.split("_")[-1].title()
                if actual_name == predicted_name:
                    correct_predictions += 1

    # Calculate accuracy
    accuracy = (correct_predictions / total_images) * 100 if total_images > 0 else 0

    return confusion_matrix, folders, accuracy

def plot_confusion_matrix(conf_matrix, classes):
    classes = [name.split("_")[-1].title() for name in classes]

    plt.figure(figsize=(12, 9))
    sns.set(font_scale=1)
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d", xticklabels=classes, yticklabels=classes)
    plt.xlabel("Predicted labels")
    plt.ylabel("Actual labels")
    plt.title("Confusion Matrix")
    plt.xticks(rotation=45)
    # plt.yticks(rotation=45)
    plt.show()

# Example usage
confusion_matrix, classes, accuracy = calculate_confusion_matrix()
plot_confusion_matrix(confusion_matrix, classes)
print(f"Accuracy: {accuracy:.2f}%")

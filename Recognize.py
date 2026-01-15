# from Integrate import load_image
import numpy as np
from tensorflow.keras.models import load_model

def image_to_embedding(image: np.ndarray, model) -> np.ndarray:   
    # Obtain image encoding
    embedding = model.predict(image[np.newaxis,...])
    
    # Normalize bedding using L2 norm.
    embedding /= np.linalg.norm(embedding, ord=2)
    
    # Return embedding
    return embedding


def compare_embeddings(embedding_1: np.ndarray, embedding_2: np.ndarray, threshold: float = 0.8) -> int:
    # Calculate the distance between the embeddings
    embedding_distance = embedding_1 - embedding_2

    # Calculate the L2 norm of the distance vector
    embedding_distance_norm = np.linalg.norm(embedding_distance)

    # Return 1 if the distance is less than the threshold, else 0
    return embedding_distance_norm if embedding_distance_norm < threshold else 0

model_path = 'model/facenet_keras.h5'
model = load_model(model_path)


def recognize_face(model, image: np.ndarray, database: dict, threshold: float = 1.0) -> str:   
    # Generate embedding for the new image
    image_emb = image_to_embedding(image, model)
    # Store distances
    distances = []
    names = []
    
    # Loop over database
    for name, embed in database.items():
        
        # Compare the embeddings
        dist = compare_embeddings(embed, image_emb, threshold=threshold)
        
        if dist > 0:
            # Append the score
            distances.append(dist)
            names.append(name)
    
    # Select the min distance
    if distances:
        min_dist = min(distances)
    
        return names[distances.index(min_dist)].title().strip()
    
    return "No Match Found"


# path = "new_105_classes_pins_dataset/pins_amber heard/amber heard4_367.jpg"
# img = load_image(path)


# # Load the database from the pickle file
# with open('database.pkl', 'rb') as pkl_file:
#     loaded_database = pickle.load(pkl_file)

# # Quick Look at loaded embeddings
# print(loaded_database["Adriana Lima"])

# model = load_model(model_path)
# x = recognize_face(model, img, loaded_database)
# print("Name: ",x)
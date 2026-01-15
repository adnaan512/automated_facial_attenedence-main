# Common
import os,pickle
import cv2 as cv
import numpy as np
from tqdm import tqdm
from glob import glob
# import plotly.express as px
import matplotlib.pyplot as plt



# Define the image dimensions
IMG_W, IMG_H, IMG_C = (160, 160, 3)



# Select all the file paths : 50 images per person.
# filepaths = [path  for name in dir_names for path in glob(root_path + name + '/*')[:50]]
# np.random.shuffle(filepaths)
# print(f"Total number of images to be loaded : {len(filepaths)}")



def load_image(image_path: str, IMG_W: int = IMG_W, IMG_H: int = IMG_H) -> np.ndarray:
    image = plt.imread(image_path)
    
    # Resize the image
    image = cv.resize(image, dsize=(IMG_W, IMG_H))
    
    # Convert image type and normalize pixel values
    image = image.astype(np.float32) / 255.0
    
    return image

def image_to_embedding(image: np.ndarray, model) -> np.ndarray:
    embedding = model.predict(image[np.newaxis,...])
    # Normalize bedding using L2 norm.
    embedding /= np.linalg.norm(embedding, ord=2)
    
    # Return embedding
    return embedding
    
def generate_avg_embedding(image_paths: list, model) -> np.ndarray:
    embeddings = np.empty(shape=(len(image_paths), 128))
    
    for index, image_path in enumerate(image_paths):        
        image = load_image(image_path)
        embedding = image_to_embedding(image, model)
        # Store the embedding
        embeddings[index] = embedding        
    # Compute average embedding
    avg_embedding = np.mean(embeddings, axis=0)
    
    # Return average embedding
    return avg_embedding


def generate_DB(model):
    num_of_imgs = 50
    root_path = 'new_105_classes_pins_dataset/'

    # Collect all the person names
    dir_names = os.listdir(root_path)
    person_names = [name.split("_")[-1].title() for name in dir_names]
    n_individuals = len(person_names)

    print(f"Total number of individuals: {n_individuals}\n")
    print(f"Name of the individuals : \n\t{person_names}")

    np.random.seed(42)
    filepaths = [np.random.choice(glob(root_path + name + '/*'), size=num_of_imgs) for name in dir_names]

    # Create data base
    database = {name:generate_avg_embedding(paths, model=model) for paths, name in tqdm(zip(filepaths, person_names), desc="Generating Embeddings")}

    with open('database.pkl', 'wb') as pkl_file:
        pickle.dump(database, pkl_file)

# Quick Look at embeddings
# print(database["Adriana Lima"])
# Name of the individuals :['Adriana Lima', 'Alexandra Daddario', 'Alycia Dabnem Carey', 'Amber Heard', 'Anne Hathaway',
                        #   'Brenton Thwaites', 'Elizabeth Olsen', 'Emilia Clarke', 'Emma Watson', 'Gal Gadot', 'Katherine Langford', 
                        #   'Kiernen Shipka', 'Leonardo Dicaprio', 'Logan Lerman', 'Margot Robbie', 'Megan Fox', 'Natalie Dormer', 
                        #   'Robert Downey Jr', 'Scarlett Johansson', 'Sophie Turner']  
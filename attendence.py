import os
import csv
import pickle
from Integrate import generate_DB, load_image
from Recognize import recognize_face



def generate_presence_csv(faces_dir, csv_file, individuals, model):
    # Generate the database
    # generate_DB()

    # Load the database from the pickle file
    with open('database.pkl', 'rb') as pkl_file:
        loaded_database = pickle.load(pkl_file)

    # Load the model
    # model_path = 'model/facenet_keras.h5'
    # model = load_model(model_path)

    # Initialize a dictionary to store the presence information
    presence_dict = {name: 0 for name in individuals}

    # Iterate through all images in the faces directory
    for image_name in os.listdir(faces_dir):
        image_path = os.path.join(faces_dir, image_name)
        if os.path.isfile(image_path):
            img = load_image(image_path)
            predicted_name = recognize_face(model, img, loaded_database)
            print("predicted_name: ",predicted_name)
            if predicted_name in presence_dict:
                presence_dict[predicted_name] = 1

    # Write the presence information to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Presence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for name in individuals:
            writer.writerow({'Name': name, 'Presence': presence_dict[name]})

    print(f"CSV file '{csv_file}' has been generated.")

# Example usage


def mark_attendence(model):
    # Define the list of individuals
    # Specify the root directory path
    root_path = 'new_105_classes_pins_dataset/'

    # Collect all the person names
    dir_names = os.listdir(root_path)
    individuals = [name.split("_")[-1].title() for name in dir_names]
    # individuals = ['Adriana Lima', 'Alexandra Daddario', 'Alycia Dabnem Carey', 'Amber Heard', 'Anne Hathaway',
    #            'Brenton Thwaites', 'Elizabeth Olsen', 'Emilia Clarke', 'Emma Watson', 'Gal Gadot', 'Katherine Langford', 
    #            'Kiernen Shipka', 'Leonardo Dicaprio', 'Logan Lerman', 'Margot Robbie', 'Megan Fox', 'Natalie Dormer', 
    #            'Robert Downey Jr', 'Scarlett Johansson', 'Sophie Turner']
    faces_directory = "faces"
    csv_output_file = "presence.csv"
    generate_presence_csv(faces_directory, csv_output_file,individuals,model)
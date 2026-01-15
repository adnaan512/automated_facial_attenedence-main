# import plotly.express as px
# import os
# # Specify the root directory path
# root_path = 'C:/Users/Mine/Downloads/Compressed/105_classes_pins_dataset/'

# # Collect all the person names
# dir_names = os.listdir(root_path)
# person_names = [name.split("_")[-1].title() for name in dir_names]
# n_individuals = len(person_names)

# print(f"Total number of individuals: {n_individuals}/n")
# print(f"Name of the individuals : /n/t{person_names}")

# # Number of images available per person
# n_images_per_person = [len(os.listdir(root_path + name)) for name in dir_names]
# n_images = sum(n_images_per_person)

# # Show
# print(f"Total Number of Images : {n_images}.")

# # Plot the Distribution of number of images per person.
# fig = px.bar(x=person_names, y=n_images_per_person, color=person_names)
# fig.update_layout({'title':{'text':"Distribution of number of images per person"}})
# fig.show()


import os
import matplotlib.pyplot as plt

# Specify the root directory path
root_path = 'C:/Users/Mine/Downloads/Compressed/105_classes_pins_dataset/'

# Collect all the person names
dir_names = os.listdir(root_path)
person_names = [name.split("_")[-1].title() for name in dir_names]
n_individuals = len(person_names)

print(f"Total number of individuals: {n_individuals}\n")
print(f"Name of the individuals : \n\t{person_names}")

# Number of images available per person
n_images_per_person = [len(os.listdir(root_path + name)) for name in dir_names]
n_images = sum(n_images_per_person)

# Show
print(f"Total Number of Images : {n_images}.")

# Plot the Distribution of number of images per person using matplotlib
plt.figure(figsize=(10, 8))
plt.bar(person_names, n_images_per_person, color='skyblue')
plt.xlabel('Individuals')
plt.ylabel('Number of Images')
plt.title('Distribution of Number of Images per Person')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to make room for the rotated labels
plt.show()

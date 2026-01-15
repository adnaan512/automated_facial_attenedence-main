import os
import shutil
import random

def pick_one_image_from_each_folder(source_dir, target_dir):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Get the list of folders in the source directory
    class_folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]

    for folder in class_folders:
        folder_path = os.path.join(source_dir, folder)
        images = [img for img in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, img))]
        
        if images:
            selected_image = random.choice(images)
            source_image_path = os.path.join(folder_path, selected_image)
            target_image_path = os.path.join(target_dir, f"{folder}_{selected_image}")
            
            # Copy the selected image to the target directory
            shutil.copy(source_image_path, target_image_path)
            print(f"Copied {selected_image} from {folder} to {target_dir}")

# Example usage
source_directory = "new_105_classes_pins_dataset"
target_directory = "faces"
pick_one_image_from_each_folder(source_directory, target_directory)

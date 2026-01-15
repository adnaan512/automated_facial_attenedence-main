import os
import cv2

def detect_and_crop_faces(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # If faces are found
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop the face from the image
            cropped_face = image[y:y+h, x:x+w]
            # Save the cropped face
            cv2.imwrite(output_path, cropped_face)
            print(f"Face cropped and saved successfully to {output_path}")
            break  # Assuming we only want to save the first detected face
    else:
        print(f"No faces detected in the image: {image_path}")

def process_images(input_dir, output_dir, num_images=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for folder_name in os.listdir(input_dir):
        input_folder_path = os.path.join(input_dir, folder_name)
        output_folder_path = os.path.join(output_dir, folder_name)
        
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        
        images = [f for f in os.listdir(input_folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        
        for i, image_name in enumerate(images[:num_images]):
            input_image_path = os.path.join(input_folder_path, image_name)
            output_image_path = os.path.join(output_folder_path, image_name)
            
            detect_and_crop_faces(input_image_path, output_image_path)
            print(f"Processed {i+1}/{num_images} in folder {folder_name}")

# Define input and output directories
input_directory = 'new_105_classes_pins_dataset'
output_directory = 'cropped_new_105_classes_pins_dataset'

# Process the images
process_images(input_directory, output_directory)

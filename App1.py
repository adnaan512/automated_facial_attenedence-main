# from Integrate import generate_DB
# from Recognize import recognize_face
# from Integrate import load_image,load_model
# import pickle

# path = "new_105_classes_pins_dataset/pins_amber heard/amber heard4_367.jpg"
# img = load_image(path)

# generate_DB()
# # Load the database from the pickle file
# with open('database.pkl', 'rb') as pkl_file:
#     loaded_database = pickle.load(pkl_file)

# # Quick Look at loaded embeddings
# print(loaded_database["Adriana Lima"])

# model_path = 'model/facenet_keras.h5'
# model = load_model(model_path)
# x = recognize_face(model, img, loaded_database)
# print("Name: ",x)



# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk
# from Integrate import generate_DB, load_image, load_model
# from Recognize import recognize_face
# from attendence import mark_attendence
# import pickle
# import random

# class FaceRecognitionApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Face Recognition App")

#         # Define colors
#         self.bg_color = "#f0f0f0"
#         self.button_color = "#4CAF50"
#         self.text_color = "#333333"

#         # Create background canvas
#         self.canvas = tk.Canvas(master, bg=self.bg_color, width=400, height=400)
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         # Add random doodle-like shapes
#         self.add_shapes()

#         # Create Update Database button
#         self.update_button = tk.Button(master, text="Update Database", bg=self.button_color, fg="white", command=self.update_database)
#         self.update_button_window = self.canvas.create_window(100, 50, anchor=tk.NW, window=self.update_button)

#         # Create Load Image button
#         self.load_image_button = tk.Button(master, text="Load Image", bg=self.button_color, fg="white", command=self.load_image)
#         self.load_image_button_window = self.canvas.create_window(250, 50, anchor=tk.NW, window=self.load_image_button)

#         # Create Predict button
#         self.predict_button = tk.Button(master, text="Predict", bg=self.button_color, fg="white", command=self.predict)
#         self.predict_button_window = self.canvas.create_window(170, 100, anchor=tk.NW, window=self.predict_button)

#         # Create image label
#         self.image_label = tk.Label(master)
#         self.image_label_window = self.canvas.create_window(100, 150, anchor=tk.NW, window=self.image_label)

#     def add_shapes(self):
#         # Add random doodle-like shapes
#         for _ in range(5):
#             shape = random.choice(["oval", "rectangle", "line"])
#             if shape == "oval":
#                 x1, y1, x2, y2 = random.randint(0, 350), random.randint(0, 350), random.randint(50, 400), random.randint(50, 400)
#                 self.canvas.create_oval(x1, y1, x2, y2, fill=self.bg_color, outline="")
#             elif shape == "rectangle":
#                 x1, y1, x2, y2 = random.randint(0, 350), random.randint(0, 350), random.randint(50, 400), random.randint(50, 400)
#                 self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.bg_color, outline="")
#             else:
#                 x1, y1, x2, y2 = random.randint(0, 350), random.randint(0, 350), random.randint(50, 400), random.randint(50, 400)
#                 self.canvas.create_line(x1, y1, x2, y2, fill=self.bg_color)

#     def update_database(self):
#         generate_DB()
#         messagebox.showinfo("Database Updated", "Database has been updated successfully!")

#     def load_image(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             self.image = Image.open(file_path)
#             self.image = self.image.resize((200, 200), Image.ANTIALIAS)
#             self.photo = ImageTk.PhotoImage(self.image)
#             self.image_label.config(image=self.photo)
#             self.image_label.image = self.photo
#             self.loaded_image = load_image(file_path)

#     def predict(self):
#         model_path = 'model/facenet_keras.h5'
#         model = load_model(model_path)

#         with open('database.pkl', 'rb') as pkl_file:
#             loaded_database = pickle.load(pkl_file)

#         if hasattr(self, 'loaded_image'):
#             name = recognize_face(model, self.loaded_image, loaded_database)
#             messagebox.showinfo("Prediction", "Predicted Name: {}".format(name))
#         else:
#             messagebox.showerror("Error", "Please load an image first!")

# def main():
#     root = tk.Tk()
#     app = FaceRecognitionApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()



import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from Integrate import generate_DB, load_image, load_model
from Recognize import recognize_face
from attendence import mark_attendence
import pickle
import random

class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        master.title("Face Recognition App")

        model_path = 'model/facenet_keras.h5'
        self.model = load_model(model_path)

        # Define colors
        self.bg_color = "#0e0e0e"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"

        # Create background canvas
        self.canvas = tk.Canvas(master, bg=self.bg_color, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add random doodle-like shapes
        self.add_shapes()

        # Create Update Database button
        self.update_button = tk.Button(master, text="Update Database", bg=self.button_color, fg="white", command=self.update_database)
        self.update_button_window = self.canvas.create_window(650, 50, anchor=tk.NW, window=self.update_button)

        # Create Load Image button
        self.load_image_button = tk.Button(master, text="Load Image", bg=self.button_color, fg="white", command=self.load_image)
        self.load_image_button_window = self.canvas.create_window(310, 200, anchor=tk.NW, window=self.load_image_button)

        # Create Predict button
        self.predict_button = tk.Button(master, text="Predict", bg=self.button_color, fg="white", command=self.predict)
        self.predict_button_window = self.canvas.create_window(460, 200, anchor=tk.NW, window=self.predict_button)

        # Create Mark Attendance button
        self.mark_attendance_button = tk.Button(master, text="Generate Attendance sheet", bg=self.button_color, fg="white", command=mark_attendence)
        self.mark_attendance_button_window = self.canvas.create_window(50, 50, anchor=tk.NW, window=self.mark_attendance_button)

        # Create image label
        self.image_label = tk.Label(master)
        self.image_label_window = self.canvas.create_window(310, 270, anchor=tk.NW, window=self.image_label)

    def add_shapes(self):
        # Add random doodle-like shapes
        for _ in range(12):
            shape = random.choice([ "line"])
            if shape == "oval":
                x1, y1, x2, y2 = random.randint(-50, 650), random.randint(-50, 650), random.randint(50, 900), random.randint(50, 900)
                self.canvas.create_oval(x1, y1, x2, y2, fill=self.text_color, outline="")
            elif shape == "rectangle":
                x1, y1, x2, y2 = random.randint(-50, 650), random.randint(-50, 650), random.randint(50, 900), random.randint(50, 900)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.text_color, outline="")
            else:
                x1, y1, x2, y2 = random.randint(-50, 650), random.randint(-50, 650), random.randint(50, 900), random.randint(50, 900)
                self.canvas.create_line(x1, y1, x2, y2, fill=self.text_color)

    def update_database(self):
        generate_DB(self.model)
        messagebox.showinfo("Database Updated", "Database has been updated successfully!")

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((200, 200), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
            self.loaded_image = load_image(file_path)

    def predict(self):
        with open('database.pkl', 'rb') as pkl_file:
            loaded_database = pickle.load(pkl_file)

        if hasattr(self, 'loaded_image'):
            name = recognize_face(self.model, self.loaded_image, loaded_database)
            messagebox.showinfo("Prediction", "Predicted Name: {}".format(name))
        else:
            messagebox.showerror("Error", "Please load an image first!")


def main():
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

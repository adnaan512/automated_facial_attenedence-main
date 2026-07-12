# Smart-Attend: Automated Attendance System with Facial Recognition

## Project Overview
Smart-Attend is an automated attendance system that leverages **facial recognition** technology to modernize attendance management in **educational institutions and workplaces**. By integrating **deep learning models** such as **FaceNet** and **Siamese Networks**, the system ensures **accurate, efficient, and secure** attendance tracking while addressing the limitations of manual attendance methods.

##  Features
- **Automated Attendance** : Uses facial recognition to mark attendance.
- **Deep Learning Models** : Implements FaceNet and Siamese Networks for accurate recognition.
- **Intuitive UI** : A user-friendly **Tkinter-based GUI** for easy interaction.
- **CSV Export** : Automatically generates attendance records in CSV format.
- **High Accuracy** : Achieved **82%+ accuracy** with Siamese Networks.

## 🛠️ Tech Stack
- **Programming Language:** Python 
- **Deep Learning Models:** FaceNet, Siamese Networks
- **Frameworks & Libraries:** TensorFlow, OpenCV, Dlib, Tkinter
- **Dataset:** [Pins Face Recognition Dataset](https://www.kaggle.com/frules11/pins-face-recognition/)

##  Project Structure
```
 Smart-Attend
data/              # Dataset directory
models/            # Pre-trained models and weights
gui/               # Tkinter-based GUI components
main.py            # Main script to run the application
requirements.txt   # List of dependencies
README.md          # Project documentation
LICENSE            # License file
```

##  How It Works
1. **Load & Train Model**: Train FaceNet/Siamese Network on the dataset.
2. **Face Detection & Recognition**: The system detects and recognizes faces using the pre-trained model.
3. **Mark Attendance**: Recognized faces are matched against a database, and attendance is automatically recorded in a CSV file.
4. **User Interaction**: Admins can update the database, check logs, and export records.

##  Installation & Setup
1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/Smart-Attend.gi(https://github.com/adnaan512/automated_facial_attenedence-main)
   cd Smart-Attend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Experimental Results
| Model | Training Accuracy | Test Accuracy |
|--------|-----------------|--------------|
| VGG16 | 60% | - |
| FaceNet | - | **80%** |
| Siamese Network | - | **82%** |

##  Challenges & Future Work
- **Challenges**: Limited dataset, underfitting issues.
- **Solutions**: Implement **data augmentation**, **transfer learning**, and **dropout regularization**.
- **Future Enhancements**: Improve model accuracy, expand dataset, and explore **multimodal biometrics**.

##  References
- [FaceNet: A Unified Embedding for Face Recognition and Clustering (CVPR 2015)](https://arxiv.org/abs/1503.03832)
- [Dlib: Machine Learning Toolkit](http://dlib.net/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

##  Acknowledgments
Special thanks to **Dr. Florian Schroff, Dr. Dmitry Kalenichenko, and Dr. James Philbin** for their contributions to **FaceNet**, and to **Kaggle** for providing the dataset.

##  License
This project is licensed under the **MIT License**.



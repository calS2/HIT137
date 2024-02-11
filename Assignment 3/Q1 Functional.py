# Import necessary libraries
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import os
import pyttsx3

# Function to load ImageNet class labels from a file
def load_class_labels(filename):
    with open(filename) as f:  # Open the file
        labels = [line.strip() for line in f.readlines()]  # Strip whitespace and newlines
    return labels  # Return the list of labels

# Base classifier class (used for polymorphism)
class BaseClassifier:
    def __init__(self, class_labels):
        self.class_labels = class_labels  # Store class labels

    def classify_image(self, image):
        raise NotImplementedError("Subclass must implement abstract method")

# VGG16 classifier class
class VGG16Classifier(BaseClassifier):
    def __init__(self, class_labels):
        super().__init__(class_labels)  # Initialize base class
        # Load pre-trained VGG16 model
        self.model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
        self.model.eval()  # Set model to evaluation mode
        # Define image transformations
        self.transform = transforms.Compose([
            transforms.Resize(256),  # Resize image
            transforms.CenterCrop(224),  # Crop image
            transforms.ToTensor(),  # Convert image to tensor
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify_image(self, image):
        # Transform image and add batch dimension
        image_t = self.transform(image).unsqueeze(0)
        with torch.no_grad():  # Disable gradient calculation
            outputs = self.model(image_t)  # Get model predictions
            _, predicted = outputs.max(1)  # Find the index of the max log-probability
            return self.class_labels[predicted.item()]  # Return the corresponding class label

# ResNet50 classifier class
class ResNet50Classifier(BaseClassifier):
    def __init__(self, class_labels):
        super().__init__(class_labels)  # Initialize base class
        # Load pre-trained ResNet50 model
        self.model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
        self.model.eval()  # Set model to evaluation mode
        # Define image transformations (same as for VGG16)
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify_image(self, image):
        # Similar to VGG16, transform image and classify
        image_t = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(image_t)
            _, predicted = outputs.max(1)
            return self.class_labels[predicted.item()]

# Class to load images from file system
class ImageLoader:
    def load_image(self, filepath):
        try:
            image = Image.open(filepath)  # Attempt to open image
            return image
        except IOError:
            print("Error in loading the image.")  # Print error if unsuccessful
            return None

# Main application class for GUI
class ImageClassifierApp(tk.Tk):
    def __init__(self, class_labels):
        super().__init__()
        self.title("Image Classifier using VGG16 and ResNet50")  # Window title
        self.geometry("1280x720")  # Window size
        self.resizable(True, True)  # Allow window resizing
        self.class_labels = class_labels  # Store class labels
        self.configure(background="white")  # Set background color
        self.create_widgets()  # Create GUI widgets
        self.classifier = None  # Classifier will be set based on user selection

    def create_widgets(self):
        # Create and pack the frames
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Create and pack buttons and label
        self.upload_button = tk.Button(top_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.classify_button = tk.Button(top_frame, text="Classify Image", command=self.classify_image, state=tk.DISABLED)
        self.classify_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.speak_button = tk.Button(top_frame, text="Speak Result", command=self.speak_result, state=tk.DISABLED)
        self.speak_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.label = tk.Label(top_frame, text="")
        self.label.pack(side=tk.LEFT, padx=10, pady=10)

        # Create canvas for image display
        self.image_canvas = tk.Canvas(bottom_frame, bg='gray')
        self.image_canvas.pack(fill=tk.BOTH, expand=True)

        # Create and pack classifier selection dropdown
        self.classifier_option = tk.StringVar(self)
        self.classifier_option.set("VGG16")  # Default classifier
        self.classifier_menu = ttk.Combobox(top_frame, textvariable=self.classifier_option, values=["VGG16", "ResNet50"])
        self.classifier_menu.pack(side=tk.LEFT, padx=10, pady=10)
        self.classifier_menu.bind("<<ComboboxSelected>>", self.update_classifier)

    def upload_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_loader = ImageLoader()
            self.image = self.image_loader.load_image(file_path)
            if self.image:
                self.label.config(text="Image loaded successfully. Ready to classify.")
                self.classify_button["state"] = tk.NORMAL  # Enable classify button
                self.update_image_preview()  # Update the image preview on canvas
            else:
                self.label.config(text="Failed to load image.")  # Show error if image load fails

    def classify_image(self):
        # Classify the loaded image and update UI
        if self.image and self.classifier:
            class_name = self.classifier.classify_image(self.image)
            self.label.config(text=f"Predicted Class: {class_name}")
            self.speak_button["state"] = tk.NORMAL  # Enable speak button
        else:
            self.label.config(text="No image loaded.")
            self.speak_button["state"] = tk.DISABLED  # Disable speak button if no image

    def speak_result(self):
        # Use text-to-speech to read out the classification result
        class_name = self.label.cget("text").replace("Predicted Class: ", "")
        if class_name:
            engine = pyttsx3.init()  # Initialize text-to-speech engine
            engine.say(class_name)  # Say the class name
            engine.runAndWait()  # Wait until speaking is finished

    def update_image_preview(self):
        # Display the loaded image on the canvas
        if self.image:
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            self.image.thumbnail((canvas_width, canvas_height))  # Resize image to fit canvas
            self.photo = ImageTk.PhotoImage(self.image)  # Convert to PhotoImage
            self.image_canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.photo, anchor=tk.CENTER)  # Display image
        else:
            self.image_canvas.delete("all")  # Clear canvas if no image

    def update_classifier(self, event=None):
        # Update the classifier based on user selection from the dropdown menu
        classifier_name = self.classifier_option.get()
        if classifier_name == "VGG16":
            self.classifier = VGG16Classifier(self.class_labels)  # Set classifier to VGG16
        elif classifier_name == "ResNet50":
            self.classifier = ResNet50Classifier(self.class_labels)  # Set classifier to ResNet50
        self.label.config(text="Classifier updated to " + classifier_name)  # Update UI with classifier choice

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    class_labels_path = os.path.join(script_dir, "imagenet_classes.txt")  # Path to class labels
    class_labels = load_class_labels(class_labels_path)  # Load class labels
    app = ImageClassifierApp(class_labels)  # Initialize and run the application
    app.mainloop()  # Start the application's main loop

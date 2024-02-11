import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import os
import pyttsx3

def load_class_labels(filename):
    with open(filename) as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

class VGG16Classifier:
    def __init__(self, class_labels):
        self.model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
        self.model.eval()
        self.class_labels = class_labels
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify_image(self, image):
        image_t = self.transform(image)
        image_t = image_t.unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(image_t)
            _, predicted = outputs.max(1)
            return self.class_labels[predicted.item()]

class ImageLoader:
    def load_image(self, filepath):
        try:
            image = Image.open(filepath)
            return image
        except IOError:
            print("Error in loading the image.")
            return None

class ImageClassifierApp(tk.Tk):
    def __init__(self, class_labels):
        super().__init__()
        self.title("Image Classifier using VGG16")
        self.geometry("1280x720")
        self.resizable(True, True)
        self.classifier = VGG16Classifier(class_labels)
        self.image_loader = ImageLoader()
        self.configure(background="white")
        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.upload_button = tk.Button(top_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.classify_button = tk.Button(top_frame, text="Classify Image", command=self.classify_image, state=tk.DISABLED)
        self.classify_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.speak_button = tk.Button(top_frame, text="Speak Result", command=self.speak_result, state=tk.DISABLED)
        self.speak_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.label = tk.Label(top_frame, text="")
        self.label.pack(side=tk.LEFT, padx=10, pady=10)

        self.image_canvas = tk.Canvas(bottom_frame, bg='gray')
        self.image_canvas.pack(fill=tk.BOTH, expand=True)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = self.image_loader.load_image(file_path)
            if self.image:
                self.label.config(text="Image loaded successfully. Ready to classify.")
                self.classify_button["state"] = tk.NORMAL
                self.update_image_preview()
            else:
                self.label.config(text="Failed to load image.")

    def classify_image(self):
        if self.image:
            class_name = self.classifier.classify_image(self.image)
            self.label.config(text=f"Predicted Class: {class_name}")
            self.speak_button["state"] = tk.NORMAL  # Enable the speak button
        else:
            self.label.config(text="No image loaded.")
            self.speak_button["state"] = tk.DISABLED  # Disable the speak button

    def speak_result(self):
        class_name = self.label.cget("text").replace("Predicted Class: ", "")
        if class_name:
            engine = pyttsx3.init()
            engine.say(class_name)
            engine.runAndWait()

    def update_image_preview(self):
        if self.image:
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            self.image.thumbnail((canvas_width, canvas_height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.photo, anchor=tk.CENTER)
        else:
            self.image_canvas.delete("all")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    class_labels_path = os.path.join(script_dir, "imagenet_classes.txt")
    class_labels = load_class_labels(class_labels_path)
    app = ImageClassifierApp(class_labels)
    app.mainloop()

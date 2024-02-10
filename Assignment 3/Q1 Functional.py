import tkinter as tk
from tkinter import filedialog
from PIL import Image
import torch
from torchvision import models, transforms

# Load ImageNet class labels
def load_class_labels(filename="imagenet_classes.txt"):
    with open(filename) as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

# VGG16 Classifier
class VGG16Classifier:
    def __init__(self, class_labels):
        self.model = models.vgg16(pretrained=True)
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

# Image Loader
class ImageLoader:
    def load_image(self, filepath):
        try:
            image = Image.open(filepath)
            return image
        except IOError:
            print("Error in loading the image.")
            return None

# Main Application
class ImageClassifierApp(tk.Tk):
    def __init__(self, class_labels):
        super().__init__()
        self.title("Image Classifier using VGG16")
        self.geometry("400x150")
        self.classifier = VGG16Classifier(class_labels)
        self.image_loader = ImageLoader()
        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.classify_button = tk.Button(self, text="Classify Image", command=self.classify_image, state=tk.DISABLED)
        self.classify_button.pack(pady=10)

        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = self.image_loader.load_image(file_path)
            if self.image:
                self.label.config(text="Image loaded successfully. Ready to classify.")
                self.classify_button["state"] = tk.NORMAL
            else:
                self.label.config(text="Failed to load image.")

    def classify_image(self):
        if self.image:
            class_name = self.classifier.classify_image(self.image)
            self.label.config(text=f"Predicted Class: {class_name}")
        else:
            self.label.config(text="No image loaded.")

if __name__ == "__main__":
    class_labels = load_class_labels(r"C:\Users\corey\Desktop\imagenet_classes.txt")  # Make sure the file path is correct
    app = ImageClassifierApp(class_labels)
    app.mainloop()




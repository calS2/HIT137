import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import os
import pyttsx3

def load_class_labels(filename):
    with open(filename) as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

class BaseClassifier:
    def __init__(self, class_labels):
        self.class_labels = class_labels

    def classify_image(self, image):
        raise NotImplementedError("Subclass must implement abstract method")

class VGG16Classifier(BaseClassifier):
    def __init__(self, class_labels):
        super().__init__(class_labels)
        self.model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify_image(self, image):
        image_t = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(image_t)
            _, predicted = outputs.max(1)
            return self.class_labels[predicted.item()]

class ResNet50Classifier(BaseClassifier):
    def __init__(self, class_labels):
        super().__init__(class_labels)
        self.model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify_image(self, image):
        image_t = self.transform(image).unsqueeze(0)
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
        self.title("Image Classifier using VGG16 and ResNet50")
        self.geometry("720x720")
        self.resizable(True, True)
        self.class_labels = class_labels
        self.configure(background="white")
        self.classifier = VGG16Classifier(class_labels)  # Set VGG16 as the default classifier
        self.create_widgets()
        self.add_instructions()

    def create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        result_frame = tk.Frame(self, background="white")
        result_frame.pack(side=tk.TOP, fill=tk.X)

        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.upload_button = tk.Button(top_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.classify_button = tk.Button(top_frame, text="Classify Image", command=self.classify_image, state=tk.DISABLED)
        self.classify_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.speak_button = tk.Button(top_frame, text="Speak Result", command=self.speak_result, state=tk.DISABLED)
        self.speak_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.classifier_option = tk.StringVar(self)
        self.classifier_menu = ttk.Combobox(top_frame, textvariable=self.classifier_option, values=["VGG16", "ResNet50"], state="readonly")
        self.classifier_menu.pack(side=tk.LEFT, padx=10, pady=10)
        self.classifier_menu.bind("<<ComboboxSelected>>", self.update_classifier)
        self.classifier_option.set("VGG16")  # Default classifier selection

        self.result_label = tk.Label(result_frame, text="", bg='white', fg='black', font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.image_canvas = tk.Canvas(bottom_frame, bg='gray')
        self.image_canvas.pack(fill=tk.BOTH, expand=True)

    def add_instructions(self):
        instructions_text = (
            "Instructions:\n"
            "- Click 'Upload Image' to select an image file.\n"
            "- After the image is loaded, 'Classify Image' button will be enabled. Click it to classify the image.\n"
            "- The classification result will be displayed in the result area with enlarged text.\n"
            "- To hear the classification result, click 'Speak Result'.\n"
            "- Use the dropdown menu to switch between VGG16 and ResNet50 classifiers."
        )
        instructions_message = tk.Message(self, text=instructions_text, width=400, bg='white', fg='black')
        instructions_message.pack(side=tk.TOP, padx=10, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = ImageLoader().load_image(file_path)
            if self.image:
                self.result_label.config(text="Image loaded successfully. Ready to classify.")
                self.classify_button["state"] = tk.NORMAL
                self.update_image_preview()
            else:
                self.result_label.config(text="Failed to load image.")

    def classify_image(self):
        if self.image:
            class_name = self.classifier.classify_image(self.image)
            self.result_label.config(text=f"Analysed Image Contains: {class_name}")
            self.speak_button["state"] = tk.NORMAL
        else:
            self.result_label.config(text="No image loaded.")
            self.speak_button["state"] = tk.DISABLED

    def speak_result(self):
        class_name = self.result_label.cget("text").replace("Analysed Image Contains: ", "")
        if class_name:
            engine = pyttsx3.init()
            engine.say(class_name)
            engine.runAndWait()

    def update_image_preview(self):
        if self.image:
        # Clear the canvas
            self.image_canvas.delete("all")

        # Calculate the new size to fit the canvas while maintaining aspect ratio
        canvas_width = self.image_canvas.winfo_width()
        canvas_height = self.image_canvas.winfo_height()
        img_width, img_height = self.image.size
        scale_width = canvas_width / img_width
        scale_height = canvas_height / img_height
        scale = min(scale_width, scale_height)

        # Resize the image with high-quality resampling
        img_resized = self.image.resize((int(img_width * scale), int(img_height * scale)), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img_resized)

        # Center the image on the canvas
        img_width, img_height = img_resized.size
        x_position = (canvas_width - img_width) // 2
        y_position = (canvas_height - img_height) // 2

        # Display the image on the canvas
        self.image_canvas.create_image(x_position, y_position, image=self.photo, anchor=tk.NW)


    def update_classifier(self, event=None):
        classifier_name = self.classifier_option.get()
        if classifier_name == "VGG16":
            self.classifier = VGG16Classifier(self.class_labels)
        elif classifier_name == "ResNet50":
            self.classifier = ResNet50Classifier(self.class_labels)
        self.result_label.config(text="Classifier updated to " + classifier_name)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    class_labels_path = os.path.join(script_dir, "imagenet_classes.txt")
    class_labels = load_class_labels(class_labels_path)
    app = ImageClassifierApp(class_labels)
    app.mainloop()

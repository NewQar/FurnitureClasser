import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pandas as pd
import random

imgWidth = 256
imgHeight = 256
classes = ["beds", "dressers", "chairs", "tables", "lamps", "sofas"]
model = load_model(r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\new\Best")

def prepareImage(image_path):
    image = load_img(image_path, target_size=(imgHeight, imgWidth))
    img_result = img_to_array(image)
    img_result = np.expand_dims(img_result, axis=0)
    img_result = img_result / 255.
    return img_result

def predict_image(image_path):
    prepared_image = prepareImage(image_path)
    result_array = model.predict(prepared_image)
    predicted_class_index = np.argmax(result_array)
    predicted_class = classes[predicted_class_index]
    if predicted_class == "lamp":
        predicted_class = "sofas"
    elif predicted_class == "dressers":
        predicted_class = "chair"
    elif predicted_class == "chairs":
        predicted_class = "dressers"
    elif predicted_class == "sofas":
        predicted_class = "tables"
    elif predicted_class == "tables":
        predicted_class = "lamps"
    return predicted_class

def add_to_cart(file_path):
    predicted_class = predict_image(file_path)
    item_id = file_path.split('/')[-1].split('.')[0]  # Extract ID from the filename
    price = random.randint(50, 200)  # Generate a random price
    cart_items.append((item_id, predicted_class, price))
    cart_listbox.insert(tk.END, f"ID: {item_id} | Class: {predicted_class} | Price: ${price}")
    update_total_amount()

def remove_from_cart():
    selected_indices = cart_listbox.curselection()
    for index in selected_indices[::-1]:
        cart_listbox.delete(index)
        cart_items.pop(index)
    update_total_amount()

def update_total_amount():
    total = sum(item[2] for item in cart_items)
    total_label.configure(text=f"Total Amount: ${total}")

def browse_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        image_label.image = image
        price_label.configure(text="Price: Pending")
        id_label.configure(text="ID: ")
        predicted_class = predict_image(file_path)
        prediction_label.configure(text="Predicted Class: " + predicted_class)
        id_label.configure(text="ID: " + file_path.split('/')[-1].split('.')[0])

def add_item_to_cart():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        add_to_cart(file_path)

def open_checkout_page():
    checkout_window = tk.Toplevel(root)
    checkout_window.title("Checkout Page")
    checkout_window.geometry("400x400")
    checkout_window.configure(bg="#F2F2F2")

    # Checkout Label
    checkout_label = tk.Label(checkout_window, text="Checkout Page", font=("Helvetica", 16, "bold"), bg="#F2F2F2")
    checkout_label.pack(pady=20)

    # Checkout Items Label
    items_label = tk.Label(checkout_window, text="Checkout Items:", font=("Helvetica", 14), bg="#F2F2F2")
    items_label.pack()

    # Checkout Listbox
    checkout_listbox = tk.Listbox(checkout_window, font=("Helvetica", 12), width=50)
    checkout_listbox.pack(pady=10)

    # Populate Checkout Listbox
    for item in cart_items:
        item_id, predicted_class, price = item
        checkout_listbox.insert(tk.END, f"ID: {item_id} | Class: {predicted_class} | Price: ${price}")

    # Total Amount Label
    total_label = tk.Label(checkout_window, text=f"Total Amount: ${total_amount}", font=("Helvetica", 14, "bold"), bg="#F2F2F2")
    total_label.pack(pady=10)

root = tk.Tk()
root.title("Image Prediction")
root.geometry("1000x500")
root.configure(bg="#F2F2F2")

# Left Frame
left_frame = tk.Frame(root, bg="#F2F2F2")
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Right Frame
right_frame = tk.Frame(root, bg="#F2F2F2")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Browse Button
browse_button = tk.Button(left_frame, text="Browse Image", command=browse_image, font=("Helvetica", 16), padx=10, pady=5, bg="#3498DB", fg="#FFFFFF", activebackground="#2980B9", activeforeground="#FFFFFF")
browse_button.pack(pady=10)

# Image Label
image_label = tk.Label(left_frame, bg="#F2F2F2")
image_label.pack(pady=10)

# Predicted Class Label
prediction_label = tk.Label(left_frame, text="Predicted Class: ", font=("Helvetica", 16), bg="#F2F2F2")
prediction_label.pack(pady=10)

# ID Label
id_label = tk.Label(left_frame, text="ID: ", font=("Helvetica", 16), bg="#F2F2F2")
id_label.pack(pady=10)

# Price Label
price_label = tk.Label(left_frame, text="Price: ", font=("Helvetica", 16), bg="#F2F2F2")
price_label.pack(pady=10)

# Add to Cart Button
add_to_cart_button = tk.Button(left_frame, text="Add to Cart", command=add_item_to_cart, font=("Helvetica", 16), padx=10, pady=5, bg="#2ECC71", fg="#FFFFFF", activebackground="#27AE60", activeforeground="#FFFFFF")
add_to_cart_button.pack(pady=10)

# Cart Frame
cart_frame = tk.Frame(right_frame, bg="#F2F2F2")
cart_frame.pack(pady=10)

# Cart Listbox
cart_items = []
cart_listbox = tk.Listbox(cart_frame, font=("Helvetica", 12), width=50)
cart_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for Cart Listbox
scrollbar = tk.Scrollbar(cart_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
cart_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=cart_listbox.yview)

# Total Amount Label
total_label = tk.Label(right_frame, text="Total Amount: $0", font=("Helvetica", 16), bg="#F2F2F2")
total_label.pack(pady=10)

# Remove Item Button
remove_item_button = tk.Button(right_frame, text="Remove Item", command=remove_from_cart, font=("Helvetica", 16), padx=10, pady=5, bg="#E74C3C", fg="#FFFFFF", activebackground="#C0392B", activeforeground="#FFFFFF")
remove_item_button.pack(pady=10)

# Checkout Button
checkout_button = tk.Button(root, text="Checkout", command=open_checkout_page, font=("Helvetica", 16), padx=10, pady=5, bg="#FF9800", fg="#FFFFFF", activebackground="#F57C00", activeforeground="#FFFFFF")
checkout_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()

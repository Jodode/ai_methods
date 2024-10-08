from requests import get, post, put, delete
from io import BytesIO
from PIL import Image, ImageTk
from time import sleep
import tkinter as tk
from tkinter import ttk

male_images = {
    'Хабиб Нурмагомедов': 'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/images/Habib.jpeg',
    'Патрик Бэйтман': 'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/images/Patrick.jpg',
    'Иосиф Сталин': 'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/images/Stalin.jpg',
    'Олег Табаков': 'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/images/Tabakov.jpg',
    'Дональд Трамп': 'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/images/Trump.jpg',
}

female_images = {
    'Виктория Боня': 'https://raw.githubusercontent.com/Jodode/ai_methods/main/lab01/data/images/Bonya.jpg',
    'Меган Фокс': 'https://raw.githubusercontent.com/Jodode/ai_methods/main/lab01/data/images/Fox.jpg',
    'Миа Кхалифа': 'https://raw.githubusercontent.com/Jodode/ai_methods/main/lab01/data/images/Mia.jpg',
    'Юлия Навальная': 'https://raw.githubusercontent.com/Jodode/ai_methods/main/lab01/data/images/Navalny.jpg',
    'Анна Семенович': 'https://raw.githubusercontent.com/Jodode/ai_methods/main/lab01/data/images/Semenovich.jpg',
}

def get_image_from_url_method_1(request_id):
    url = "https://faceswap3.p.rapidapi.com/result/"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request_id\"\r\n\r\n{request_id}\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "x-rapidapi-key": "c1ed10766amshcae26b62c408e44p1b56dejsn0318b221d1ff",
        "x-rapidapi-host": "faceswap3.p.rapidapi.com",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }

    response = post(url, data=payload, headers=headers).json()
    url_image = response['image_process_response']['result_url']
    image = get(url_image)

    return image

def face_swap_method_1(url1, url2):
    url = "https://faceswap3.p.rapidapi.com/faceswap/v1/image"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_url\"\r\n\r\n{url1}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"swap_url\"\r\n\r\n{url2}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_face_index\"\r\n\r\n0\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "x-rapidapi-key": "c1ed10766amshcae26b62c408e44p1b56dejsn0318b221d1ff",
        "x-rapidapi-host": "faceswap3.p.rapidapi.com",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }

    response = post(url, data=payload, headers=headers).json()
    print(response)
    request_id = response['image_process_response']['request_id']

    image = get_image_from_url_method_1(request_id)

    img = Image.open(BytesIO(image.content))
    # img.show()
    return img

def get_image_from_url_method_2(request_id):
    url = "https://faceswap-api.p.rapidapi.com/result"

    payload = {
        "request_id": request_id
        }
    
    headers = {
        "x-rapidapi-key": "c1ed10766amshcae26b62c408e44p1b56dejsn0318b221d1ff",
        "x-rapidapi-host": "faceswap-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = post(url, json=payload, headers=headers).json()
    print(response)
    url_image = response['output']

    image = get(url_image)

    return image

def face_swap_method_2(url1, url2):

    url = "https://faceswap-api.p.rapidapi.com/faceswap-image"

    payload = { "input": {
            "swap_image": url1,
            "target_image": url2
        } 
    }
    headers = {
        "x-rapidapi-key": "c1ed10766amshcae26b62c408e44p1b56dejsn0318b221d1ff",
        "x-rapidapi-host": "faceswap-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = post(url, json=payload, headers=headers).json()

    request_id = response['request_id']

    sleep(10)

    image = get_image_from_url_method_2(request_id)

    img = Image.open(BytesIO(image.content))
    # img.show()
    return img

def update_preview(combo, label):
    selected_name = combo.get()
    image_url = male_images.get(selected_name) or female_images.get(selected_name)
    if image_url:
        response = get(image_url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((200, 200))  # Resize for larger preview
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

def swap_faces():
    target_name = target_combo.get()
    source_name = source_combo.get()

    target_url = male_images.get(target_name) or female_images.get(target_name)
    source_url = male_images.get(source_name) or female_images.get(source_name)

    if target_url and source_url:
        # Using face_swap_method_1
        img1 = face_swap_method_1(target_url, source_url)
        img1.thumbnail((300, 300))  # Resize for display
        img1_tk = ImageTk.PhotoImage(img1)
        result_label_1.config(image=img1_tk)
        result_label_1.image = img1_tk

        # Using face_swap_method_2
        img2 = face_swap_method_2(source_url, target_url)
        img2.thumbnail((300, 300))  # Resize for display
        img2_tk = ImageTk.PhotoImage(img2)
        result_label_2.config(image=img2_tk)
        result_label_2.image = img2_tk

app = tk.Tk()
app.title("Face Swap Application")

ttk.Label(app, text="Select Target Image:").grid(column=0, row=0, padx=10, pady=10)
target_combo = ttk.Combobox(app, values=list(male_images.keys()) + list(female_images.keys()))
target_combo.grid(column=1, row=0, padx=10, pady=10)
target_combo.bind("<<ComboboxSelected>>", lambda e: update_preview(target_combo, target_preview))

target_preview = ttk.Label(app)
target_preview.grid(column=2, row=0, padx=10, pady=10)

ttk.Label(app, text="Select Source Image:").grid(column=0, row=1, padx=10, pady=10)
source_combo = ttk.Combobox(app, values=list(male_images.keys()) + list(female_images.keys()))
source_combo.grid(column=1, row=1, padx=10, pady=10)
source_combo.bind("<<ComboboxSelected>>", lambda e: update_preview(source_combo, source_preview))

source_preview = ttk.Label(app)
source_preview.grid(column=2, row=1, padx=10, pady=10)

swap_button = ttk.Button(app, text="Swap Faces", command=swap_faces)
swap_button.grid(column=0, row=2, columnspan=3, pady=20)

ttk.Label(app, text="Result from Method 1:").grid(column=0, row=3, padx=10, pady=10, columnspan=2, sticky='ew')
result_label_1 = ttk.Label(app)
result_label_1.grid(column=0, row=4, padx=10, pady=10, columnspan=2, sticky='ew')

ttk.Label(app, text="Result from Method 2:").grid(column=2, row=3, padx=10, pady=10, columnspan=2, sticky='ew')
result_label_2 = ttk.Label(app)
result_label_2.grid(column=2, row=4, padx=10, pady=10, columnspan=2, sticky='ew')

app.mainloop()
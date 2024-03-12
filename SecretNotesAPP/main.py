import tkinter
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encrypt_click():

    if len(entry_title.get()) == 0 or len(text_secret.get("1.0","end")) == 0 or len(entry_key.get()) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info. ")
    else:

        message_encrypted = encode(entry_key.get(), text_secret.get("1.0", "end"))

        try:
            with open("secrets.txt", "a") as file:
                file.write(f"\n{entry_title.get()}\n")
                file.write(f"{message_encrypted}\n")

        except FileNotFoundError:
            with open("secrets.txt", "w") as file:
                file.write(f"\n{entry_title.get()}\n")
                file.write(f"{message_encrypted}\n")
        finally:
            entry_title.delete(0, "end")
            text_secret.delete("1.0", "end")
            entry_key.delete(0, "end")

        global user_key
        user_key = entry_key.get()

def decrypt_click():

    if len(text_secret.get("1.0", "end")) == 0 or len(entry_key.get()) == 0:
        messagebox.showinfo(title="Error!", message="Please give all info for decryption. " )
    else:
        try:
            message_decrypted = decode(entry_key.get(), text_secret.get("1.0", "end"))
            text_secret.delete("1.0", "end")
            text_secret.insert("1.0", message_decrypted)

        except:
            messagebox.showinfo(title="Error", message="Please enter encrypted text. ")

#User Interface
window = Tk()
window.geometry("400x600")
window.title("Secret Notes")
file = "secretnotesimage.png"

image = Image.open(file)
max_width = 120

pixels_x, pixels_y = tuple([int(max_width / image.size[0] * x) for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixels_x,pixels_y)))
label = tkinter.Label(image= img)
label.image = img
label.pack()

label_title = tkinter.Label(text= "Enter your title..")
label_title.pack()

entry_title = tkinter.Entry()
entry_title.config(bg="white",fg="black")
entry_title.pack()

label_secret = tkinter.Label(text= "Enter your secret..")
label_secret.pack()

text_secret = tkinter.Text(width=50,height=20)
text_secret.config(bg="white",fg="black")
text_secret.pack()


label_key = tkinter.Label(text="Enter master key")
label_key.pack()

entry_key = tkinter.Entry()
entry_key.config(bg="white",fg="black")
entry_key.pack()

encrypt_button = tkinter.Button(text="Save & Encrypt",command=encrypt_click)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=decrypt_click)
decrypt_button.pack()


window.mainloop()
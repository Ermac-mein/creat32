from tkinter import *


def encrypt():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    ciphertext_text.delete(1.0, END)
    ciphertext_text.insert(END, ciphertext)


def decrypt(ciphertext_entry=None):
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char

    plaintext_text.delete(1.0, END)
    plaintext_text.insert(END, plaintext)


# Create the main window
window = Tk()
window.title("Encryption and Decryption App")

# Create and position the widgets
plaintext_label = Label(window, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)

plaintext_entry = Entry(window, width=30)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

shift_label = Label(window, text="Shift:")
shift_label.grid(row=1, column=0, padx=5, pady=5)

shift_entry = Entry(window, width=30)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = Button(window, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=5, pady=5)

decrypt_button = Button(window, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)

ciphertext_label = Label(window, text="Ciphertext:")
ciphertext_label.grid(row=3, column=0, padx=5, pady=5)

ciphertext_text = Text(window, width=30, height=5)
ciphertext_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

plaintext_label = Label(window, text="Decrypted Text:")
plaintext_label.grid(row=5, column=0, padx=5, pady=5)

plaintext_text = Text(window, width=30, height=5)
plaintext_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()

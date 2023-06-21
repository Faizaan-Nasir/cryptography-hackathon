from tkinter import *
import random

def generate_key():
    def encrypt(text, key):
        random.seed(key)
        encrypted_text = ""
        for char in text:
            encrypted_char = chr(ord(char) ^ random.randint(0, 255))
            encrypted_text += encrypted_char
        output_e=Label(top, text='Encrypted string: '+encrypted_text, font=('Sans',18),bg='#D3D3D3')
        output_e.pack()
        output_e.place(relx=0.1,rely=0.40)
        print('encrypted string: ',encrypted_text)
    global encrypt_t
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMANOPQRSTUVWXYZ0123456789"
    key = "".join(random.choice(characters) for _ in range(6))
    text_l=str(encrypt_t.get())
    print(text_l,'key: ',key)
    encrypt(text_l,key)
    page_subheading=Label(top, text='OUTPUT:', font="Sans 22 bold underline",bg='#D3D3D3')
    page_subheading.pack()
    page_subheading.place(relx=0.1,rely=0.35)
    output_k=Label(top, text='Key string: '+key, font=('Sans',18),bg='#D3D3D3')
    output_k.pack()
    output_k.place(relx=0.1,rely=0.45)

    
def decrypted():
    def decrypt(encrypted_text, key):
        random.seed(key)
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_char = chr(ord(char) ^ random.randint(0, 255))
            decrypted_text += decrypted_char
        return decrypted_text
    global decrypt_t
    global decrypt_k
    texted=decrypt_t.get()
    key=decrypt_k.get()
    x=decrypt(texted,key)
    page_subheading=Label(top, text='OUTPUT:', font="Sans 22 bold underline",bg='#D3D3D3')
    page_subheading.pack()
    page_subheading.place(relx=0.1,rely=0.80)
    output_e=Label(top, text='Decrypted string: '+x, font=('Sans',18),bg='#D3D3D3')
    output_e.pack()
    output_e.place(relx=0.1,rely=0.85)
    

def get_text():
    pass
stroutput_e='hello world'
top=Tk()
top.title("cipher")
top.geometry("1800x900")
top.configure(bg='#D3D3D3')
page_heading=Label(top, text="CIPHER", font="Sans 35 bold underline",bg='#D3D3D3',fg='red')
page_heading.pack()
page_heading.place(relx=0.5, anchor=CENTER, rely=0.05)
page_head_e=Label(top, text='ENCRYPTION', font="Sans 28 bold underline",bg='#D3D3D3')
page_head_e.pack()
page_head_e.place(relx=0.1, rely=0.1)
encrypt=Label(top, text="Text to encrypt: ", font=("Sans",18),bg='#D3D3D3')
encrypt.pack()
encrypt.place(relx=0.1, rely=0.20)
encrypt_t=Entry(top, bd=1, font=("Sans",18))
encrypt_t.pack()
encrypt_t.place(relx=0.3, rely=0.20)
submit = Button(top, text='SUBMIT',font="Sans 12 bold", bd=1, bg='white', command=generate_key)
submit.pack()
submit.place(height=35, width=100, relx=0.5, rely=0.29, anchor=CENTER)
page_head_d=Label(top, text='DECRYPTION', font="Sans 28 bold underline",bg='#D3D3D3')
page_head_d.pack()
page_head_d.place(relx=0.1, rely=0.5)
decrypt_tl=Label(top, text="Text to decrypt: ", font=("Sans",18),bg='#D3D3D3')
decrypt_tl.pack()
decrypt_tl.place(relx=0.1, rely=0.60)
decrypt_t=Entry(top, bd=1, font=("Sans",18))
decrypt_t.pack()
decrypt_t.place(relx=0.3, rely=0.60)
decrypt_kl=Label(top, text="Key to decrypt: ", font=("Sans",18),bg='#D3D3D3')
decrypt_kl.pack()
decrypt_kl.place(relx=0.1, rely=0.65)
decrypt_k=Entry(top, bd=1, font=("Sans",18))
decrypt_k.pack()
decrypt_k.place(relx=0.3, rely=0.65)
submit = Button(top, text='SUBMIT',font="Sans 12 bold", bd=1, bg='white', command=decrypted)
submit.pack()
submit.place(height=35, width=100, relx=0.5, rely=0.75, anchor=CENTER)
top.mainloop()

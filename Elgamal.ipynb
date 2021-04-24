
#--------
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg

import random  
from math import pow
  
a = random.randint(2, 100) 
  
def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 
  
# Generating large random numbers 
def gen_key(q): 
  
    key = random.randint(pow(10, 20), q) 
    while gcd(q, key) != 1: 
        key = random.randint(pow(10, 20), q) 
  
    return key 
  
# Modular exponentiation 
def power(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 
  
# Asymmetric encryption 
def encrypt(msg, q, h, g): 
  
    en_msg = [] 
  
    k = gen_key(q)# Private key for sender 
    s = power(h, k, q) 
    global p
    p = power(g, k, q) 
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
    print("g^k used : ", p) 
    print("g^ak used : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 
  
def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 

def fun(msg):
   
    global q
    global key
    q = random.randint(pow(10, 20), pow(10, 50)) 
    g = random.randint(2, q) 
  
    key = gen_key(q)# Private key for receiver 
    h = power(g, key, q)
    en_msg, p = encrypt(msg, q, h, g)
    en_msg=list(map(str,en_msg))
    print(en_msg)
    
    en_msg=','.join(en_msg)
    print("p",p)
    print("q",q)
    print("key",key)
    
    return en_msg

    
main=Tk()
main.title("Elgamal Encrption with Image Steganography")
main.geometry("500x400+300+150")



def encode():
    main.destroy()
    enc=Tk()
    enc.title("Encode")
    enc.geometry("500x400+300+150")
    
    label1=Label(text="Secret Message")
    label1.place(relx=0.2,rely=0.17,height=40,width=100)
    
    entry=Entry()
    entry.place(relx=0.4,rely=0.2,width=200)
    
    

    label2=Label(text="File Name")
    label2.place(relx=0.2,rely=0.3,height=40,width=100)
    
    entrysave=Entry()
    entrysave.place(relx=0.4,rely=0.32,width=200)
    
    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png,jpg files","*jpg"),("all files","*.*"))) 
        
        label3=Label(text=fileopen)
        label3.place(relx=0.3,rely=0.6)
    
    def encodee():
        response=messagebox.askyesno("pop up","do you want to encode")
        if response==1:
            mes=entry.get()
            elmsg=fun(mes)
            #print(elmsg)

            
            
            stg.hide(fileopen,entrysave.get()+'.jpg',elmsg)
            messagebox.showinfo("pop up","successfully encoded")
        else:
            messagebox.warning("pop up","unsuccessful")
            
            
       
        
    buttonselect=Button(text="Select File",command=openfile)
    buttonselect.place(relx=0.5,rely=0.4)
    
    buttonencode=Button(text="Encrypt",command=encodee)
    buttonencode.place(relx=0.4,rely=0.8,height=40,width=80)
def decode():
    main.destroy()
    dnc=Tk()
    dnc.title("Decode")
    dnc.geometry("500x400+300+150")
    
    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=filedialog.askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png,jpg files","*jpg"),("all files","*.*"))) 
        
        
    
    def decodee():
        message=stg.reveal(fileopen)
        message=str(message)
        message=message[2:-1]
        print(message)
        #message=int(message)
        message=message.split(",")
        message=list(map(int,message))
        print(p)
        dr_msg = decrypt(message, p,key,q) 
        message = ''.join(dr_msg)
        label4=Label(text=message)
        label4.config(font=("Courier", 30))
        label4.place(relx=0.3,rely=0.2)
    
    buttonselect=Button(text="Choose file",command=openfile)
    buttonselect.place(relx=0.2,rely=0.4)
    
    buttonencode=Button(text="Decrypt",command=decodee)
    buttonencode.place(relx=0.4,rely=0.8,height=40,width=80)
    

encodeb=Button(text="Encode",command=encode)
encodeb.place(relx=0.2,rely=0.5,height=40,width=80)

decodeb=Button(text="Decode",command=decode)
decodeb.place(relx=0.7,rely=0.5,height=40,width=80)

main.mainloop()

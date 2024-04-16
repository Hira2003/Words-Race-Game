import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from nltk.corpus import words
from PIL import ImageTk, Image
import pygame




def is_english_word(word):
    word = word.lower()
    return word in words.words()


n = 0
w = []
nm = []
def show_message(message):
    messagebox.showinfo("Alert!!", message)

            
i = 1
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
l = []
hist = []
j = 0

def how():
    def d():
        root6.destroy()
    root6 = tk.Toplevel(root1)
    root6.geometry("400x660")
    center_window(root6, 400, 660)
    root6.title("Words Race: How to play")
    root6.configure(bg="light blue")
    tk.Label(root6,bg="light blue",text="How to play", font=('Cookie',24) ,fg="dark blue").pack(pady=7)
    tk.Label(root6,bg="white",text="1- Enter players number \nand their names \n\n\n 2- The first player \njust enter any word \n\n\n 3- here the game starts \nthe last letter of the word\n is the first in the next one \n\n\n 4- repeatation prevented \nless than 3 letters prevented", font=('Orbitron',16)).pack()
    tk.Button(root6, bg="white", font=('Cookie',18),text="Back", command=d).pack(pady=7)
    
pts = []         
def players():
    def ops():
     def crazy():
        root2.destroy()
        play()
     global n
     global i
     
     def names():
        global i
        
        nm.append(entry4.get())
        lb5.config(text=f"Player{i}")
        tk.Label(root2,text=f"Player{i}: {entry4.get()}", font=('Orbitron',16)).pack()
        entry4.delete(0, tk.END)
        if i < n:
          i += 1
          lb5.config(text=f"Player{i}")
        else:
          i = 1
          for k in range(n):
            w.append(nm[k])
            pts.append(0)
          lb5.config(text="Great! click to start playing")
          entry4.destroy()
          button10.config(text="Start", command = crazy)
          
          
        
     
     if entry4.get() != "" and int(entry4.get()) > 1 :
       n = int(entry4.get())
       entry4.delete(0, tk.END)
       
       lb5.config(text=f"Player{i}")
        
       button10.configure(command=names)
       
        
       
       
     else:
       if entry4.get() == "":
         show_message("Please enter a number first to play")
       if int(entry4.get()) < 1:
          show_message("2 or more please")

    root2 = tk.Toplevel(root1)
    root2.geometry("400x600")
    center_window(root2, 400, 600)
    root2.title("Words Race")
    root2.configure(bg="light blue")
    lb5 = tk.Label(root2, text="Players number", font=("Cookie",20),bg="light blue")  # Adjusted height for a better fit within the row
    lb5.pack(padx=10, pady=25)  # Added padding for better alignment

    entry4 = tk.Entry(root2, width= 70, font=('Orbitron',20))
    
    entry4.pack(pady=10, padx= 50)
    
    button10 = tk.Button(root2, text="OK",font=("Cookie",18),bg="white",command=ops, width= 10)  # Changed "import" to "Import" for consistency
    button10.pack(pady=10, padx= 50)
    def show_notification1():
        result = messagebox.askquestion("Notification", "If you went back you wrote names will be deleted\nDo you really want to go back to main?")
        
        if result == 'yes':
            root2.destroy()
        else:
            root2.attributes("-topmost", 1)

    tk.Button(root2,text="Back",font=("Cookie",18),bg="white",command=show_notification1, width= 10).pack(pady=10)
    
def play():
  global i
  i = 0
  def fill():
    global i
    global j
    word = entry1.get()
    if is_english_word(word) != False and word not in hist and len(word) > 2:
       if len(word) == 3:
         lb75.configure(text="Good!! +3pts")
         pts[i] = pts[i] + 3
       if len(word) == 4:
         lb75.configure(text="Nice!! +4pts")
         pts[i] = pts[i] + 4
       if len(word) == 5:
         lb75.configure(text="Fablous! +5pts")
         pts[i] = pts[i] + 5
       if len(word) >= 6:
         lb75.configure(text=f"Excellent!! +{len(word)}pts")
         pts[i] = pts[i] + len(word)
       tree.insert("", "end" , values=(nm[i],word))
       hist.append(word)
       if j < 10:
          j += 1
       if j == 10:
         first_item = tree.get_children()[0]  # Get the ID of the first item
         if first_item:  # If the item exists
          tree.delete(first_item)  # Delete the first item
       entry1.delete(0, tk.END)
       entry1.insert(0, f"{word[len(word)-1]}")
       
    else:
        show_message(f"{nm[i]} Loser")
        
        w.remove(nm[i])
        #nm.remove(nm[i])
        l.append(nm[i])
        entry1.delete(0, tk.END)
        entry1.insert(0, f"{word[len(word)-1]}")
        
    if i <= n:
      i += 1
      if i == n:
            i = 0
      while(nm[i] in l):
        i +=1
        if i == n:
            i = 0
                
      lb2.config(text= f"{nm[i]}")
    else:
      i = 0
      lb2.config(text= f"{nm[i]}")
    
    if len(w)==1:
        show_message(f"{w[0]} is Winner , Scores = {pts[i]}")
        button1.configure(state='disabled')
        s = ""
        for i in range(n):
            s = s + f"Scores: {nm[i]} has {pts[i]} points\n"
        lb75.configure(text=f"{s}")
  root = tk.Toplevel(root1)
  root.geometry("1100x600")
  center_window(root, 1100, 600)
  root.title("Words Race")
  root.configure(bg="light blue")
  
  

  # Entry fields
  entry1 = tk.Entry(root, font=('Orbitron',14))
  entry1.grid(row=0, column=3, padx=2, pady=5)
  #text_widget = tk.Text(root, width=30, height=10)
  # Labels
  lb1 = tk.Label(root, text="Word", font=("Cookie",18),bg="light blue")  # Adjusted height for a better fit within the row
  lb1.grid(row=0, column=2, padx=5, pady=5)  # Added padding for better alignment
  if i>n:
    i = 0
  lb2 = tk.Label(root, text=f"{nm[i]}", font=("Orbitron",18),bg="light blue", width=10)  # Adjusted height for a better fit within the row
  lb2.grid(row=0, column=1, padx=5, pady=5)  # Added padding for better alignment

  # Buttons
  button1 = tk.Button(root, text="Check",font=("Cookie",18),bg="white",command= fill)  # Changed "save" to "Save" for consistency
  button1.grid(row=0, column=4, padx=3, pady=5)  # Moved the "Save" button to a different row
  
  def b(event):
      fill()
  root.bind("<Return>", b)

  # Create a Treeview widget
  tree = ttk.Treeview(root, columns=('player','history'), show='headings')
  tree.heading('player', text='player')
  tree.heading('history', text='history')
  
  tree.grid(row=0, column=0, columnspan=1, padx=1, pady=1)  # Expanded the Treeview over multiple columns with padding

  lb75 = tk.Label(root, text="", font=("Cookie",18),bg="light blue")  # Adjusted height for a better fit within the row
  lb75.grid(row=1, column=1, padx=5, pady=5)  # Added padding for better alignment
  
  def show_notification2():
        result = messagebox.askquestion("Notification", "If you went back the game will restart\nDo you really want to go back to main?")
        
        if result == 'yes':
            
            nm = []
            w = []
            l = []
            pts = []
            i = 1
            j = 1
            n = 0
            hist = []
            root.destroy()
            
        else:
            root.attributes("-topmost", 1)
            
  buttonss = tk.Button(root, text="Back",font=("Cookie",18),bg="white",command= show_notification2)  # Changed "save" to "Save" for consistency
  buttonss.grid(row=200, column=4, padx=3, pady=200)  # Moved the "Save" button to a different row
  
  

root1 = tk.Tk()
pygame.init()

pygame.mixer.music.load("Beloved(chosic.com).mp3")
pygame.mixer.music.play(loops = 0)
center_window(root1, 400, 660)
root1.configure(bg="light blue")
root1.title("Words Race")
lb4 = tk.Label(root1, text="____|Words Race|___", font=("Cookie",30), fg="dark blue",bg="light blue")  # Adjusted height for a better fit within the row
lb4.pack(padx=10, pady=25)  # Added padding for better alignment

def displayimage():
    global image_labell
    image_labell = tk.Label(root1, image=pico)
    image_labell.pack()

image_labell = None

imag = Image.open("hira.png")
pico = ImageTk.PhotoImage(imag)

def display():
    
        root1.state('zoomed')
        root4.state('zoomed')
        
        root2.state('zoomed')
        
        root.state('zoomed')
def disno():
        root4.geometry("400x660")
        #center_window(root4, 400, 600)
        root1.geometry("400x660")
        #center_window(root1, 400, 600)
        root2.geometry("400x660")
        #center_window(root2, 400, 600)
        root.geometry("400x660")
        #center_window(root, 400, 600)
def opt():
    
    def Off():
        pygame.mixer.music.stop()
    def On():
        pygame.mixer.music.play(loops = 0)
    root4 = tk.Toplevel(root1)
    root4.geometry("400x660")
    center_window(root4, 400, 660)
    root4.title("Words Race")
    root4.configure(bg="light blue")
    root4.title("Words Race: Options")
    lb7 = tk.Label(root4, text="____|Options|___", font=("Cookie",30), fg="dark blue",bg="light blue")  # Adjusted height for a better fit within the row
    lb7.pack(padx=10, pady=10)  # Added padding for better alignment
    bbs = tk.Label(root4, text="****Sound****",font=("Cookie",20),fg="black", bg= "light blue")
    bbs.pack(padx=10, pady=10)
    
    
    bb2 = tk.Label(root4, text="Off:",font=("Orbitron",18),fg="black", bg= "light blue")
    bb2.pack(padx=3, pady=5)
    
    button15 = tk.Button(root4, text="",font=("Webdings",18),bg="white",command=Off, width= 5)  # Changed "import" to "Import" for consistency
    button15.pack(padx=3, pady=5)
    
    bb1 = tk.Label(root4, text="On:",font=("Orbitron",18),fg="black" , bg= "light blue")
    bb1.pack(padx=3, pady=5)
    
    button16 = tk.Button(root4, text="",font=("Webdings",18),bg="white",command=On, width= 5)  # Changed "import" to "Import" for consistency
    button16.pack(padx=3, pady=5)
    
    bbb = tk.Label(root4, text="Screen:",font=("Cookie",20),fg="black", bg= "light blue")
    bbb.pack(padx=3, pady=5)
    
    button44 = tk.Button(root4, text="Full Screen",font=("Orbitron",12),bg="white",command=display, width= 15)  # Changed "import" to "Import" for consistency
    button44.pack(padx=3, pady=5)
    
    button45 = tk.Button(root4, text="Normal Screen",font=("Orbitron",12),bg="white",command=disno, width= 15)  # Changed "import" to "Import" for consistency
    button45.pack(padx=3, pady=5)
    
    def u():
        root4.destroy()
    tk.Button(root4, text="Back",font=("Cookie",18),bg="white",command=u, width= 10).pack(pady= 5)
    
def close():
    root1.destroy()
    pygame.mixer.music.stop()

displayimage()
   
button6 = tk.Button(root1, text="Play",font=("Cookie",18),bg="white",command=players, width= 30)  # Changed "import" to "Import" for consistency
button6.pack(pady=10, padx= 50)

button7 = tk.Button(root1, text="How to Play",font=("Cookie",18),bg="white", width= 30, command= how)  # Changed "import" to "Import" for consistency
button7.pack(pady=10, padx= 50)

button8 = tk.Button(root1, text="Options",font=("Cookie",18),bg="white", command=opt, width= 30)  # Changed "import" to "Import" for consistency
button8.pack(pady=10, padx= 50)

button9 = tk.Button(root1, text="Exit",font=("Cookie",18),bg="white",command=close, width= 30)  # Changed "import" to "Import" for consistency
button9.pack(pady=10, padx= 50)

def on_closing():
    # Stop the music and close the window
    pygame.mixer.music.stop()
    root1.destroy()

# Configure the window close protocol
root1.protocol("WM_DELETE_WINDOW", on_closing)

root1.mainloop()

try:
    import Tkinter as tk
except:
    import tkinter as tk
    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry('100x50')
       self.root.title("Profile")
       button = tk.Button(self.root, text = 'Book Issue', command=self.issue)
       button.pack()
       button = tk.Button(self.root, text = 'Book Return', command=self.return_)
       button.pack()
       self.root.minsize(width = 1370, height = 700)
       self.root.maxsize(width = 1370, height = 700)
       self.root.mainloop()

   def issue(self):
       self.root.destroy()
       self.bookissue()


   def return_(self):
       self.root.destroy()
       self.bookreturn()
  
   def bookissue(self):
       self.b1 =tk.Tk()
       self.b1.title("Book Issue")
       button3 =tk.Label(self.b1, text = "Please scan the bar code", width = 150, height = 2, font=("Arial Bold", 10))
       button3.pack(padx = 1, pady =20 )
       self.b1.minsize(width = 1370, height = 700)
       self.b1.maxsize(width = 1370, height = 700)
       self.b1.mainloop()

   def bookreturn(self):
       self.r1 =tk.Tk()
       self.r1.title("Book Return")
       button3 =tk.Label(self.r1, text = "Please scan the bar code", width = 150, height = 2, font=("Arial Bold", 10))
       button3.pack(padx = 1, pady =20 )
       self.r1.minsize(width = 1370, height = 700)
       self.r1.maxsize(width = 1370, height = 700)
       self.r1.mainloop()    
    
 



app = Test()

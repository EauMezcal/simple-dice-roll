import tkinter as tk
import random

class Roller(object):
    def __init__(self):
        self.root=tk.Tk()
        # 标题
        self.root.title("Simple-Dice-Roller!")
        self.root.geometry('450x500+100+100')
        # 输入框
        self.D_input = tk.Entry(self.root, width= 15)
        # 回显列表
        self.display_info = tk.Listbox(self.root, width= 30, height= 25)
        self.text1 = tk.Label(self.root, text="1D ? :")
        self.Roll_Button = tk.Button(self.root, command= self.roll, text = "roll", width=7)
        self.clean_Button = tk.Button(self.root,command= self.clean, text= "Clean" ,bg="#BA3E35",fg="#ffffff")
        self.site = [('1D 2',1),
                     ('1D 6',2),
                     ('1D 10',3),
                     ('1D 100',4)]
        self.v = tk.IntVar()
        for name, num in self.site:
            radio_button = tk.Radiobutton(text = name, variable = self.v,value =num,command=self.roll_choose,indicatoron=False, width=7)
            radio_button.place(x=10,y=10+(num-1)*30)
        
        # GUI
        
        # 文本框
        self.D_input.place(x=10,y=160)
        # 回显框
        self.display_info.place(x=200,y=10)
        # roll按钮
        self.Roll_Button.place(x=10,y=190)
        # clean按钮
        self.clean_Button.place(x=150,y=10)
        # 文本
        self.text1.place(x=10,y=135)

    def roll_choose(self):
        self.dict={1:'2',2:'6',3:'10',4:'100'}
        self.D = int(self.dict.get(self.v.get()))
        roll = random.randint(1,self.D)
        the_roll_info = ["1D %d roll:" % int(self.dict.get(self.v.get())) + str(roll)]
        for item in the_roll_info:
            self.display_info.insert(0,item)

    def roll(self):
        self.D = int(self.D_input.get())
        roll = random.randint(1,self.D)
        the_roll_info = ["1D %d roll:" % int(self.D_input.get()) + str(roll)]
        
        for item in the_roll_info:
            self.display_info.insert(0,item)
    def clean(self):    
        self.display_info.delete(0,9999)
        
def main():
    A = Roller()
    # A.gui()
    tk.mainloop()
    pass

if __name__=="__main__":
    main()
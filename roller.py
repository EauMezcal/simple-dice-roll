import tkinter as tk
import random
from webbrowser import BackgroundBrowser


class Roller(object):
    def __init__(self):
        self.root=tk.Tk()
        # 标题
        self.root.title("Roller!")
        # self.root.geometry('450X300')
        # self.config(Background="write")
        self.D_input = tk.Entry(self.root, width=30)
        # 回显列表
        self.display_info = tk.Listbox(self.root, width=50)
        self.Roll_Button = tk.Button(self.root, command= self.roll, text = "roll!!")
        # self.display_info = tk.Listbox(self.root, width=50)

        # self.v = tk.IntVar()
        # self.v.set(0)
        # tk.Radiobutton(self, text="1D 2", variable=self.v, value=4).pack(anchor = 'w')
        # tk.Radiobutton(self, text="1D 10", fg='blue',font=('微软雅黑','12','bold'),variable=self.v, value=0).pack(anchor = 'w')
        # tk.Radiobutton(self, text="1D 20", variable=self.v, value=2).pack(anchor = 'w')
        # tk.Radiobutton(self, text="1D 100", variable=self.v, value=3).pack(anchor = 'w')
        self.site = [('1D 2',1),
                    ('1D 10',2),
                    ('1D 20',3),
                    ('1D 100',4)]
        # IntVar() 用于处理整数类型的变量
        self.v = tk.IntVar()
        # 重构后的写法，也非常简单易懂
        for name, num in self.site:
            radio_button = tk.Radiobutton(text = name, variable = self.v,value =num,command=self.roll_choose,indicatoron=False)
            radio_button.pack(anchor ='w')
    def gui(self):
        self.D_input.pack()
        self.display_info.pack()
        self.Roll_Button.pack()


    def roll_choose(self):
        self.dict={1:'2',2:'10',3:'20',4:'100'}
        self.D = int(self.dict.get(self.v.get()))
        roll = random.randint(1,self.D)
        the_roll_info = ["1D %d roll:" % int(self.dict.get(self.v.get())) + str(roll)]
        for item in the_roll_info:
            self.display_info.insert(0,item)

    def roll(self):
        self.D = int(self.D_input.get())
        roll = random.randint(1,self.D)
        the_roll_info = ["1D %d roll:" % int(self.D_input.get()) + str(roll)]

        # for item in range(10):
        #     self.display_info.insert(0,"")
        
        for item in the_roll_info:
            self.display_info.insert(0,item)
    # def Roll_1D2:
        
def main():
    A = Roller()
    A.gui()
    tk.mainloop()
    pass

if __name__=="__main__":
    main()
# while True:
#     s = input('1D  ')
#     s = int(s)
#     a = random.randint(1,s)
#     print('结果：'+str(a))

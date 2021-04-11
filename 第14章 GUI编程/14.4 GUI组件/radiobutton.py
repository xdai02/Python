import tkinter

class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x200")

        # 单选按钮需要设置显示内容和对应数据值
        self.sex = [("男", 0), ("女", 1)]

        self.label = tkinter.Label(
            self.root,
            text="选择性别：",
            font=("微软雅黑", 14)
        )
        self.label.grid(row=0, column=0)

        pos = 1
        for title, index in self.sex:
            radio = tkinter.Radiobutton(
                self.root,
                text=title, value=index,
                font=("微软雅黑", 14)
            )
            radio.grid(row=0, column=pos)
            pos += 1

        self.root.mainloop()

def main():
    MainForm()

if __name__ == "__main__":
    main()
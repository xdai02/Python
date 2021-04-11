import tkinter

class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x200")
        self.src_list()     # 待选区
        self.dst_list()     # 已选区
        self.set_button()   # 按钮区
        self.root.mainloop()
    
    def src_list(self):
        """
            待选区列表
        """
        self.src_label = tkinter.Label(
            self.root,
            text="选择擅长的编程语言",
            bg="#223011", fg="#fff",
            font=("微软雅黑", 9)
        )
        self.src_label.grid(row=0, column=0)
        self.languages = [
            "Python", "Java", "JavaScript",
            "C", "C++", "PHP", "Go", 
        ]
        self.language_listbox = tkinter.Listbox(
            self.root, selectmode="multiple"
        )
        for language in self.languages:
            self.language_listbox.insert("end", language)
        # 双击选中
        self.language_listbox.bind("<Double-Button-1>", self.add_handler)
        self.language_listbox.grid(row=1, column=0)
    
    def dst_list(self):
        """
            已选区列表
        """
        self.dst_label = tkinter.Label(
            self.root,
            text="擅长的编程语言",
            bg="#223011", fg="#fff",
            font=("微软雅黑", 9)
        )
        self.dst_label.grid(row=0, column=3)
        self.selected_listbox = tkinter.Listbox(
            self.root, selectmode="multiple"
        )
        self.selected_listbox.grid(row=1, column=3)
    
    def set_button(self):
        """
            设置按钮
        """
        self.add_btn = tkinter.Button(
            self.root,
            text="添加 >>",
            fg="#000",
            font=("微软雅黑", 9)
        )
        self.add_btn.bind("<Button-1>", self.add_handler)
        self.add_btn.grid(row=1, column=1)
    
    def add_handler(self, event):
        """
            添加按钮事件处理
        """
        # 获取全部被选中的数据索引
        for index in self.language_listbox.curselection():
            self.selected_listbox.insert("end", self.language_listbox.get(index))
        # 索引在每一次删除之后都会动态改变
        while True:
            # 有被选中的项
            if self.language_listbox.curselection():
                # 删除当前项
                self.language_listbox.delete(self.language_listbox.curselection()[0])
            else:
                break

def main():
    MainForm()

if __name__ == "__main__":
    main()
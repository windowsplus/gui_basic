from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width =30) #아이디 같은 한줄 입력
e.pack()
e.insert(0,"한줄만 입력하세요")

def btncmd():
    print(txt.get("1.0", END)) #첫째줄에서 0번째 컬럼.
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
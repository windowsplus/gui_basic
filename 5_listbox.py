from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height =0) #single=1개씩만 선택, height = 숫자(보여주는 라인)
listbox.insert(0, "사과")
listbox.insert(1, "배")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
   #listbox.delete(END) #삭제
   #print("리스트에는", listbox.size(), "개가 있어요")
   #print("1~3항목은", listbox.get(0,2)) #시작 끝
   print("선택된 항목 : ", listbox.curselection()) #위치로 반한
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
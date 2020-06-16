from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="메뉴를 선택하세요").pack()
buger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=buger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=buger_var)
btn_burger3 = Radiobutton(root, text="치킨버고", value=3, variable=buger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(buger_var.get()) #햄버거 중 선택된 라디오 항목의 값 출력
    print(drink_var.get()) #햄버거 중 선택된 라디오 항목의 값 출력
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
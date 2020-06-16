import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "매진됐어야.")

def error():
        msgbox.showerror("에러", "결제 오류가 발생.")


def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 그래도?")

def retrycancel():
        msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다. 그래도?")


def yesno():
    msgbox.askryesno("예/아니오", "역방향입니다. 그래도?")

def yesnocancel():
   response = msgbox.askyesnocancel(title = None, message ="예매 내역이 저장되지 않았습니다. \n 저장 후 종료?")
   print("응답", response)
   if response == 1:
       print("예")
   elif response == 0:
       print("아니오")
   else:
       print("취소")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()


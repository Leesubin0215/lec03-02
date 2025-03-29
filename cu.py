import tkinter

def btn_click():
    num1 =int(entry1.get()or 0)
    num2= int(entry2.get()or 0)
    num3= int(entry3.get()or 0)
    num4= int(entry4.get()or 0)
    num5= int(entry5.get()or 0)
    num6= int(entry6.get()or 0)
    num7= int(entry7.get()or 0)
    num8= int(entry8.get()or 0)
    num9= int(entry9.get()or 0)
    num10= int(entry10.get()or 0)
    num11= int(entry11.get()or 0)
    num12= int(entry12.get()or 0)


    total=0

    판매가격 = (num1 * 1800) + (num2 * 1400) + (num5 * 1800) + (num7 * 4000) + (num8 * 1500) + (num9 * 2000)

    구입가격 = (num3 * 500) + (num4 * 900) + (num6 * 800) + (num10 * 3500) + (num11 * 700) + (num12 * 1000)

    total = 판매가격 - 구입가격

    str1 = "오늘 총 매출액은 " + str(total) + "원 입니다."
   
   
    labelRes1 = tkinter.Label(root, text=str1, font=("맑은 고딕",10))
    labelRes1.place(x=47, y=240)
  
root = tkinter.Tk()
root.title("CU")
root.geometry("800x300")

label1 =tkinter.Label(root, text= "캔 커피", font=("맑은 고딕",10))
label2=tkinter.Label(root, text= "판매 수량", font=("맑은 고딕",10))
label3=tkinter.Label(root, text= "구매 수량", font=("맑은 고딕",10))
label4=tkinter.Label(root, text= "삼각김밥", font=("맑은 고딕",10))
label5=tkinter.Label(root, text= "바나나우유", font=("맑은 고딕",10))
label6=tkinter.Label(root, text= "도시락", font=("맑은 고딕",10))
label7=tkinter.Label(root, text= "콜라", font=("맑은 고딕",10))
label8=tkinter.Label(root, text= "새우깡", font=("맑은 고딕",10))

label1.place(x=100,y=20)
label2 .place(x=15, y=72)
label3 .place(x=15, y=132)
label4 .place(x=200, y=20)
label5 .place(x=300, y=20)
label6 .place(x=415, y=20)
label7 .place(x=510, y=20)
label8 .place(x=600, y=20)

entry1 = tkinter.Entry(width=5)
entry2 = tkinter.Entry(width=5)
entry3 = tkinter.Entry(width=5)
entry4 = tkinter.Entry(width=5)
entry5 = tkinter.Entry(width=5)
entry6 = tkinter.Entry(width=5)
entry7 = tkinter.Entry(width=5)
entry8 = tkinter.Entry(width=5)
entry9 = tkinter.Entry(width=5)
entry10 = tkinter.Entry(width=5)
entry11 = tkinter.Entry(width=5)
entry12 = tkinter.Entry(width=5)

entry1.place(x=105, y=75)
entry2.place(x=210, y=75)
entry5.place(x=315, y=75)
entry7.place(x=418, y=75)
entry8.place(x=508, y=75)
entry9.place(x=604, y=75)
entry3.place(x=105, y=135)
entry4.place(x=210, y=135)
entry6.place(x=315, y=135)
entry10.place(x=418, y=135)
entry11.place(x=508, y=135)
entry12.place(x=604, y=135)

btn =tkinter.Button(root, text="계산", font=("맑은 고딕",10), command=btn_click)
btn.place(x=50, y=187,width=630, height=28)
root.mainloop()
# import tkinter as tk   #Tk()=tk.Tk()
from tkinter import *
from tkinter import messagebox
import random


# root = Tk()
# root.title("윈도우 프로그래밍 연습")
# root.geometry("640x480")
#기본창 띄우기
# label = Label(root,text="안녕하세요.")
# label.pack(side="left")

#레이아웃(layout) (pack()방식)
# label1=Label(root,text="Top",bg="red",fg="white")
# label1.pack(side="top",fill="x",padx=10,pady=10)
# label2=Label(root, text="BOTTOM",bg="blue",fg="white")
# label2.pack(side="bottom",fill="x",padx=10,pady=10)
# label3=Label(root, text="left",bg="green",fg="white")
# label3.pack(side="left",fill="y",padx=10,pady=10)
# label4=Label(root, text="right",bg="yellow",fg="black")
# label4.pack(side="right",fill="y",padx=10,pady=10)
# label5=Label(root, text="중앙",bg="purple",fg="white")
# label5.pack(side="top",fill="both",expand=True, padx=10,pady=10)
#생성 순서대로 자리를 차지한다.
# root.mainloop()

#레이아웃 (grid()방식)
# label1=Label(root,text="label1",bg="red",fg="white")
# label1.grid(row=0,column=0,padx=10,pady=10)
# label2=Label(root,text="label2",bg="blue",fg="white")
# label2.grid(row=0,column=1,padx=10,pady=10)

# root.mainloop()

#위젯================================================
# #Label
# label = Label(root, text="Hello, tkinter!",font=("Pretendard", 20), fg="blue")
# label.pack()

# # root.mainloop()
# #버튼
# def on_click():
#     print("button Click")
# button = Button(root, text="클릭",command=on_click).pack() #command = 버튼 클릭시 발생할 함수
# #글씨입력--------------------------------------------------------------------------------------
# def show_text():
#     #entry
#     entried=entry.get()
#     label.config(text=f"입력된 문자는 : {entried}")
#     entry.delete(0,END) #엔트리에 있는 문자열 삭제
#     #text
#     print(text.get("1.0",END))
    
# #입력을 위해서는 레이아웃은 메서드 체인을 사용할 수 없음.
# entry=Entry(root,width=10) #entry : 한줄 입력
# entry.pack()

# #Text : 여러줄 입력
# text=Text(root,width=40, height=10)
# text.pack()


# button = Button(root, text="클릭",command=show_text).pack() #command = 버튼 클릭시 발생할 함수
# label=Label(root,text="hahahaa")
# label.pack()
#------------------------------------------------------------------------------------------------
#Frame
# top_frame=Frame(root,bg="lightblue")
# top_frame.pack(fill="x")
# Label(top_frame, text="Top frame").pack(pady=30)
# bottom_frame=Frame(root,bg="lightgreen")
# bottom_frame.pack(fill="both",expand=True)
# Label(bottom_frame, text="bottom frame",bg="yellow").pack()
#________________________________________________________________________________________________
#checkbutton
# def show_state():
#     print(f"check는 {var.get()}")

# var=IntVar()
# checkbtn=Checkbutton(root,text="동의",variable=var, command=show_state).pack()

# #radiobutton
# var=StringVar(value="option1")
# radio1= Radiobutton(root,text="옵션1",variable=var,value="option1",command=show_state).pack(pady=5)
# radio2= Radiobutton(root,text="옵션2",variable=var,value="option2",command=show_state).pack(pady=5)

#listbox------------------------------------------------------------------
# def show_selected():
#     selection = listbox.curselection()
#     print(selection)
#     if selection:
#         print(f"선택된 과일은 :{Listbox.get(selection[0][i])}")

# listbox=Listbox(root)
# listbox.pack(pady=10)
# for item in ["사과","바나나","포도","체리"]:
#     listbox.insert(END,item)

# button=Button(root,text="선택",command=show_selected)
# button.pack(pady=10)
# root.mainloop()

# messagebox ================================================================

# def show_message():
#     messagebox.showinfo("제목 : 경고","메세지창 띄우기 연습")

# button = Button(root,text="클릭시 경고",command=show_message)
# button.pack(pady=10)

# 메뉴 ========================================================================
# def new_file():
#     messagebox.showinfo("메뉴","파일이 선택되었습니다.")
# def exit_app():
#     root.quit() #윈도우창 종료

# menubar = Menu(root)
# filemenu=Menu(menubar,tearoff=0)
# filemenu.add_command(label="New",command=new_file)
# filemenu.add_separator()
# filemenu.add_command(label="EXIT",command=exit_app)

# menubar.add_cascade(label="파일",menu=filemenu)
# root.config(menu=menubar)
# root.mainloop()

# 쿠폰 추첨기 [종합 훈련 ]=======================================================
# def on_click():
#     name_list=["김민경","이동건","최승우","최영","한수빈","김혜은","이채연","조경록"]
#     name = random.sample(name_list,4)
#     print(name)
#     text.delete("1.0",END)
#     text.insert(END,name)
    
# window = Tk()
# window.title("쿠폰 추첨기")
# window.geometry("640x480")
# # #이미지 넣기
# # label_img=Label(window)
# # img=PhotoImage(file="다운로드.gif")
# # label_img.config(image=img)
# # label_img.pack()
# #추첨버튼
# Button(window, text="추첨", command=on_click).pack()
# #추첨된 사람 출력
# text=Text(window,width=40, height=5, bg="green")
# text.pack()
# window.mainloop()


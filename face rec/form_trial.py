from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def submit_data():
    messagebox.showinfo('Status','Data saved')
    category=''
    session_type=''
    section=''
    subject=sub_entry.get()
    if session_entry.get()==1:
        session_type='LAB'
    elif session_entry.get()==2:
        session_type='THEORY'
    if section_entry.get()==1:
        section='A'
    elif section_entry.get()==2:
        section='C'
    elif section_entry.get()==3:
        section='BOTH'
    if category1.get()==1:
        category+='T1 '
    if category2.get()==1:
        category+='T2 '
    if category3.get()==1:
        category+='T3 '
    if category4.get()==1:
        category+='T4 '
    print(subject,session_type,section,category)
window = Tk()
#window.geometry("500x500")
window.title('Lecture Information')
frame=Frame(window)
frame.pack()
main_frame=LabelFrame(frame,text='')
main_frame.grid(row=0,column=0,sticky='news',padx=20,pady=30)
#Subject Input
sub_lb=Label(main_frame,text='SUBJECT',font=('Cambria',17,'bold'))
sub_lb.grid(row=0,column=0,padx=20,pady=20)
sub_options=['CHE1003(Bio-sciences_Nanotechnology)',
             'CSE2022(Artificial Intelligence Techinques and Methods)',
             'CSE2101(Artificial Neural Network)',
             'CSE2102(Computer Network)',
             'CSE2103(Software Engineering and Project Management)',
             'CSE2718(Computer Architecture)']
sub_entry=ttk.Combobox(main_frame,values=sub_options,width=50,height=25)
sub_entry.grid(row=0,column=1,sticky='w',padx=20,pady=20)
#Session type input
session_lb=Label(main_frame,text='SESSION',font=('Cambria',17,'bold'))
session_lb.grid(row=1,column=0,padx=20,pady=20)
session_entry=IntVar()
session_op1=Radiobutton(main_frame,text='LAB',variable=session_entry,value=1,font=('Courier',15))
session_op2=Radiobutton(main_frame,text='THEORY',variable=session_entry,value=2,font=('Courier',15))
session_op1.grid(row=1,column=1,sticky='w',padx=10)
session_op2.grid(row=1,column=1,padx=10)

#Section Input
section_lb=Label(main_frame,text='SECTION',font=('Cambria',17,'bold'))
section_lb.grid(row=2,column=0,padx=20,pady=20)
section_entry=IntVar()
section_op1=Radiobutton(main_frame,text='A',variable=section_entry,value=1,font=('Courier',15))
section_op2=Radiobutton(main_frame,text='C',variable=section_entry,value=2,font=('Courier',15))
section_op3=Radiobutton(main_frame,text='BOTH',variable=section_entry,value=3,font=('Courier',15))
section_op1.grid(row=2,column=1,sticky='w',padx=10)
section_op2.grid(row=2,column=1,padx=10)
section_op3.grid(row=2,column=1,sticky='e',padx=10)

#Category Input
category_lb=Label(main_frame,text='CATEGORY',font=('Cambria',17,'bold'))
category_lb.grid(row=3,column=0,padx=20,pady=20)
category1 = IntVar()  
category2 = IntVar()  
category3 = IntVar()
category4 = IntVar()
c1 = Checkbutton(main_frame, text = "T1", 
                      variable = category1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
  
c2 = Checkbutton(main_frame, text = "T2",
                      variable = category2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
  
c3 = Checkbutton(main_frame, text = "T3",
                      variable = category3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))

c4 = Checkbutton(main_frame, text = "T4",
                      variable = category4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 1,
                      font=('Courier',15))
c1.grid(row=3,column=1,padx=10,sticky='w')
c2.grid(row=3,column=1,padx=10)
c3.grid(row=4,column=1,padx=10,sticky='w')
c4.grid(row=4,column=1,padx=10)

#submit button
main_frame2=LabelFrame(frame,text='')
main_frame2.grid(row=5,column=0,padx=20,pady=5)
submit=Button(main_frame2,text='Submit',width=15,height=2,bg='blue',activebackground='green',command=submit_data)
submit.grid(row=5,column=0)

window.mainloop()
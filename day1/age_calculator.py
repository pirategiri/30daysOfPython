from tkinter import *
from datetime import datetime

App=Tk()
App.title("Age calculator")

msg=Label(App,text="enter your date of birth")
msg.grid(row=0,column=0,columnspan=3)

dayL=Label(App,text="Day")
dayE=Entry(App,width=2)

monthL=Label(App,text="Month")
monthE=Entry(App,width=2)

yearL=Label(App,text="Year")
yearE=Entry(App,width=4)

dayL.grid(row=1,column=0)
dayE.grid(row=1,column=1)
monthL.grid(row=1,column=2)
monthE.grid(row=1,column=3)
yearL.grid(row=1,column=4)
yearE.grid(row=1,column=5)

def find_days():
	date=int(dayE.get())
	month=int(monthE.get())
	year=int(yearE.get())
	dob=datetime(day=date,month=month,year=year)

	time_now=datetime.now()
	time_diff=time_now-dob

	dys=Label(App,text='you lived' +str(time_diff.days)+' days')
	dys.grid(row=3,column=3,columnspan=3)
def find_sec():
	date=int(dayE.get())
	month=int(monthE.get())
	year=int(yearE.get())
	dob=datetime(day=date,month=month,year=year)

	time_now=datetime.now()
	time_diff=time_now-dob

	sec=Label(App,text='you lived' +str(time_diff.total_seconds())+' seconds')
	sec.grid(row=3,column=3,columnspan=3)

dysB=Button(App,text='total days',command=find_days)
secB=Button(App,text='total seconds',command=find_sec)
dysB.grid(row=2,column=0,columnspan=3)
secB.grid(row=2,column=3,columnspan=3)

App.mainloop()



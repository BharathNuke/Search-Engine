from tkinter import *
from urllib import urlopen

def getLinks(url):
    links = []
    while True:
        pos = url.find('<a href')
        if pos == -1:
            break
        url = url[pos+8:]
        start = url.find('"')
        links.append(url[start+1:url.find('"',start+1)])
    return links

def action():
    url = v.get()
    page = urlopen(url).read()
    sv.set('\n'.join(getLinks(page)))

def cls():
    v.set('')
    sv.set('')


main = Tk()
v = StringVar()
sv = StringVar()
frame = Frame(main, bd=4)

l = Label(frame, text="Enter URL: ")
e = Entry(frame, textvariable=v)
b = Button(frame, text = "Search",command=action)
b2 = Button(frame, text = "Clear",command=cls)

#frame2 = Frame(main)
e2 = Label(frame, textvariable=sv)
#sc = Scrollbar(frame2,orient='horizontal', command = e2.xview)
#e2.config(xscrollcommand=sc.set)

frame.grid()
l.grid(row=0, column=0,sticky='ew')
e.grid(row=0, column=1,sticky='ew')
b.grid(row=1, column=1, sticky='ew')
b2.grid(row=1,column=0,sticky='ew')

#frame2.grid()
e2.grid(row=2, sticky='ew')
#sc.grid(row=2,column=0, sticky='ew')

main.mainloop()

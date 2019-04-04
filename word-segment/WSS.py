# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:13:30 2019

@author: lenovo
"""

import requests
import tkinter as tk
import tkinter.font as tkFont

def getResponse(event):
    entry2.config(state=tk.NORMAL)
    entry2.delete(0, tk.END)
    ipt = str(entry1.get())
    response = requests.get('http://word-segment.sai.corp:8090/v1/api/seg?q=' + ipt)
    rt = eval(response.text)
    res = ''
    l = len(rt)
    for i in range(l):
        tmp = rt[i]['text']
        res += tmp
        if i < l-1:
            res += '/'
        else:
            continue
    entry2.insert(10, res)
    entry2.config(state=tk.DISABLED)
    
top = tk.Tk()
top.title('Word-Segmentation System')
top.geometry('600x300')  #窗口尺寸
tk.Label(top, text = 'query').place(x=180,y=110)
tk.Label(top, text = 'result').place(x=180,y=170)

entry1 = tk.Entry(top)
entry2 = tk.Entry(top)
entry1.place(x=250,y=110)
entry2.place(x=250,y=170)

ft = tkFont.Font(family='Fixdsys', size=24, weight=tkFont.BOLD, slant=tkFont.ITALIC)
tk.Label(top, text='Soundai', font=ft, fg='blue').place(x=240,y=40)

button = tk.Button(top, text = 'run',width=13, height=1, command = getResponse).place(x=260,y=230)
entry1.bind("<Return>", getResponse)
top.mainloop()
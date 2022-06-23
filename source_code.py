import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
import string
from tkinter.filedialog import askopenfilename
import os
import pytesseract
import time
from tkinter.ttk import Progressbar
from pytesseract import image_to_string
import csv
from tkinter import messagebox 
from tkinter import PhotoImage
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def Save_Values(): 
    csvpath='Data.csv'
    with open(csvpath,'a',newline=('')) as datafile:
        writer=csv.writer(datafile,delimiter=",")
        mylist=[combobox1.get(),combobox2.get(),text3.get(1.0,"end-1c"),combobox4.get(),
                combobox5.get(),combobox6.get(),combobox7.get(),combobox8.get(),combobox910.get()
                ,text9.get(1.0,"end-1c"),combobox10.get(),combobox11.get()
                ,combobox12.get(),combobox13.get(),combobox14.get()
                ,combobox15.get(),combobox16.get(),combobox17.get()
                ,combobox18.get(),combobox19.get(),combobox20.get()
                ,combobox21.get(),combobox22.get(),combobox23.get()
                ,text24.get(1.0,"end-1c"),combobox25.get(),combobox26.get()
                ,combobox27.get(),combobox28.get(),combobox29.get()
                ,combobox30.get(),combobox31.get(),combobox32.get()
                ,combobox33.get(),combobox34.get(),combobox35.get()]
        writer.writerow(mylist)
        progress['value']=00
        for w in f1.winfo_children():
            try:
                w.set("")
            except:
                continue
        try:
            text3.delete(1.0,"end-1c")
            text9.delete(1.0,"end-1c")
            text24.delete(1.0,"end-1c")
        except:
            pass
        v1.clear()
        v2.clear()
        v3.clear()
        v4.clear()
        v5.clear()
        v6.clear()
        v7.clear()
        v8.clear()
        v9.clear()
        v910.clear()
        v10.clear()
        v11.clear()
        v12.clear()
        v13.clear()
        v14.clear()
        v15.clear()
        v16.clear()
        v17.clear()
        v18.clear()
        v19.clear()
        v20.clear()
        v21.clear()
        v22.clear()
        v23.clear()
        v24.clear()
        v25.clear()
        v26.clear()
        v27.clear()
        v28.clear()
        v29.clear()
        v30.clear()
        v31.clear()
        v32.clear()
        v33.clear()
        v34.clear()
        v35.clear()
        datafile.close()
def Show_Image(image):
        progress['value']=5
        progress.update()
        fr.update()
        global image1
        image1 = image.resize((canvas2.winfo_width(),canvas2.winfo_height()),Image.ANTIALIAS)
        width, height = image1.size
        container = canvas2.create_rectangle(0, 0, width, height, width=0)
        bbox1 = canvas2.bbox(container)  
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (canvas2.canvasx(0),  
                 canvas2.canvasy(0),
                 canvas2.canvasx(canvas2.winfo_width()),
                 canvas2.canvasy(canvas2.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]), 
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]: 
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        x1 = max(bbox2[0] - bbox1[0], 0)
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:
            imagetk = ImageTk.PhotoImage(image1.resize((int(x2 - x1), int(y2 - y1))))
            imageid = canvas2.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),                                       anchor='nw', image=imagetk)
            canvas2.lower(imageid)  
            canvas2.imagetk = imagetk 
        canvas.update()
        Sender_Name(image)
def Select_Image():
    for w in f1.winfo_children():
            try:
                w.set("")
            except:
                continue
    try:
        text3.delete(1.0,"end-1c")
        text9.delete(1.0,"end-1c")
        text24.delete(1.0,"end-1c")
    except:
        pass
    v1.clear()
    v2.clear()
    v3.clear()
    v4.clear()
    v5.clear()
    v6.clear()
    v7.clear()
    v8.clear()
    v9.clear()
    v910.clear()
    v10.clear()
    v11.clear()
    v12.clear()
    v13.clear()
    v14.clear()
    v15.clear()
    v16.clear()
    v17.clear()
    v18.clear()
    v19.clear()
    v20.clear()
    v21.clear()
    v22.clear()
    v23.clear()
    v24.clear()
    v25.clear()
    v26.clear()
    v27.clear()
    v28.clear()
    v29.clear()
    v30.clear()
    v31.clear()
    v32.clear()
    v33.clear()
    v34.clear()
    v35.clear()
    for w in f1.winfo_children():
            try:
                w.delete(1.0,"end-1c")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.set("")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.update()
            except:
                continue
    root.update()
    global path
    path=tk.filedialog.askopenfilenames(initialdir=os.getcwd(),title="Select Image Files",
                                  filetypes=[("Image Files","*.jpg")])
    global ipath
    global pathuni
    ipath=0
    pathuni=path[ipath]
    image = Image.open(pathuni)
    Show_Image(image)
def Do_Next():
    v1.clear()
    v2.clear()
    v3.clear()
    v4.clear()
    v5.clear()
    v6.clear()
    v7.clear()
    v8.clear()
    v9.clear()
    v910.clear()
    v10.clear()
    v11.clear()
    v12.clear()
    v13.clear()
    v14.clear()
    v15.clear()
    v16.clear()
    v17.clear()
    v18.clear()
    v19.clear()
    v20.clear()
    v21.clear()
    v22.clear()
    v23.clear()
    v24.clear()
    v25.clear()
    v26.clear()
    v27.clear()
    v28.clear()
    v29.clear()
    v30.clear()
    v31.clear()
    v32.clear()
    v33.clear()
    v34.clear()
    v35.clear()
    for w in f1.winfo_children():
            try:
                w.delete(1.0,"end-1c")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.set("")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.update()
            except:
                continue
    root.update()
    global image
    global pathuni
    global ipath
    global bv
    length=len(path)
    if ipath<length-1:
        ipath+=1
        pathuni=path[ipath]
        image = Image.open(pathuni)
        Show_Image(image)
    else:
        Select_Image()
def Do_Back():
    v1.clear()
    v2.clear()
    v3.clear()
    v4.clear()
    v5.clear()
    v6.clear()
    v7.clear()
    v8.clear()
    v9.clear()
    v910.clear()
    v10.clear()
    v11.clear()
    v12.clear()
    v13.clear()
    v14.clear()
    v15.clear()
    v16.clear()
    v17.clear()
    v18.clear()
    v19.clear()
    v20.clear()
    v21.clear()
    v22.clear()
    v23.clear()
    v24.clear()
    v25.clear()
    v26.clear()
    v27.clear()
    v28.clear()
    v29.clear()
    v30.clear()
    v31.clear()
    v32.clear()
    v33.clear()
    v34.clear()
    v35.clear()
    for w in f1.winfo_children():
            try:
                w.delete(1.0,"end-1c")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.set("")
            except:
                continue
    for w in f1.winfo_children():
            try:
                w.update()
            except:
                continue
    root.update()
    global image
    global pathuni
    global ipath
    global bv
    if ipath==0:
        messagebox.showinfo(title="Error",message="You already at first Image")
    else:
        ipath-=1
        pathuni=path[ipath]
        image = Image.open(pathuni)
        Show_Image(image)
def Sender_Name(image):
    t = image_to_string(image)
    f = open(r"data\new.txt","w")
    f.write(t)
    f.close()
    f=open(r"data\new.txt","r")
    lines=f.readlines()
    num_lines = sum(1 for line in open(r'data\new.txt'))
    for x in range(num_lines-1):
        line=lines[x]
        line=line.replace(".", "")
        line=line.replace("\n", "")
        x,y,tn,z,a,e,i,o,u,p,q,r,t="m","Invoice","TAXINVOICE","TAX","a","e","i","o","u","0","1","2","3"
        if len(line) <10 :
            continue
        elif len(line) >26:
             continue
        elif x in line:
             continue
        elif y in line:
            continue
        elif z in line :
             continue
        if t in line:
            continue
        elif tn in line:
             continue
        elif a in line:
             continue
        elif e in line:
             continue
        elif i in line:
             continue
        elif o in line:
             continue
        elif u in line:
             continue
        elif p in line:
             continue
        elif q in line:
             continue
        elif r in line:
             continue
        else:
            combobox2.set(line)
            combobox2.update()
            break
    progress['value']=10
    progress.update()
    GST(lines,num_lines)
def GST(lines,num_lines):
    for p in range(num_lines-1):
        line=lines[p]
        x,y="GST","Gst"
        if len(line)<=15:
            continue
        if x in line :
            line=line.split(" ")
            ql=len(line)
            q=0
            for q in range(q,ql):
                l=line[q]
                l=l.replace(" ","")
                l=l.replace("\n","")
                if len(l)==15:
                    v6.append(l)
                    v12.append(l)
                    v16.append(l)
        if y in line:
            line=line.split(" ")
            ql=len(line)
            q=0
            for q in range(q,ql):
                l=line[q]
                l=l.replace(" ","")
                l=l.replace("\n","")
                if len(l)==15:
                    v6.append(l)
                    v12.append(l)
                    v16.append(l)
    combobox6.config(values=v6)
    combobox12.config(values=v12)
    combobox16.config(values=v16)
    try:
        combobox6.set(v6[0])
        combobox12.set(v12[1])
        combobox16.set(v16[2])
    except:
        pass
    progress['value']=15
    progress.update()
    Buyers_Name(lines,num_lines)
    """
def Pan(lines,num_lines):
    for p in range(num_lines-1):
        line=lines[p]
        x="PAN"
        if p==8:
            break
        if len(line)<=10:
            continue
        if x in line :
            line=line.split(" ")
            ql=len(line)
            q=0
            for q in range(q,ql):
                l=line[q]
                l=l.replace(":","")
                l=l.replace(" ","")
                l=l.replace("|","")
                l=l.replace("\n","")
                if len(l)==10:
                    if l.upper():
                        #combobox3.set(l)
                        break        
    for p in range(num_lines-1):
            line=lines[p]
            x="PAN"
            if len(line)<=10:
                continue
            if x in line :
                line=line.split(" ")
                ql=len(line)
                q=0
                for q in range(q,ql):
                    l=line[q]
                    l=l.replace(":","")
                    l=l.replace(" ","")
                    l=l.replace("\n","")
                    if len(l)==10:
                        if l.upper():
                            pass
                            #v3.append(l)
                            #v7.append(l)
                           # combobox7.set(l)  
    try:
    #    combobox3.set(v7[0])
        pass
    except:
        pass
   #combobox3.config(values=v3)
    combobox7.config(values=v7)
    progress['value']=20
    progress.update()
    Buyers_Name(lines,num_lines)
    """
def Buyers_Name(lines,num_lines):
    for x in range(num_lines-1):
        line=lines[x]
        line=line.replace(":", "")
        line=line.replace("\n", "")
        if len(line)<3:
            continue
        for q in range(0,3):
            w=line[q]
            a,b,c,d,e,f,g,h,j="1","tax","GST","1","2","3","0","4","Billed"
            if a in w :
                continue
            if b in w:
                continue
            if c in w:
                continue
            if d in w:
                continue
            if e in w:
                continue
            if f in w:
                continue
            if g in w:
                continue
            if h in w :
                continue
            if j in w :
                continue
            else:
                v910.append(line)
                break
    combobox910.config(values=v910)
    progress['value']=25
    progress.update()
    Find_Total(lines, num_lines)
def Find_Total(lines,num_lines):
    pl=0
    for x in range(num_lines-1):
        line=lines[x]
        x="Total"
        if x in line :
            line=line.split(" ")
            ql=len(line)
            q=0
            for q in range(q,ql):
                l=line[q]
                l=l.replace(" ","")
                l=l.replace(",", "")
                l=l.replace("\n", "")
                l2=l
                l=l.replace(".","")
                if l.isnumeric():
                    l=int(l)
                    if l>pl:
                        pl=l
                        combobox28.set(l2)
                        combobox33.set(l2)
    combobox28.update()
    combobox33.update()
    progress['value']=30
    progress.update()
    Date(lines,num_lines)
def Date(lines,num_lines):
    for x in range(num_lines-1):
        line=lines[x]
        line=line.split(" ")
        q=0
        ql=len(line)
        for i in range(q,ql):
            d=line[i]
            s="-"
            if s in d:
                ns=d.count("-")
                if ns==2:
                    v18.append(d)
    combobox18.config(value=v9)
    try:
        combobox18.set(v18[0])
        pass
    except:
        pass
    progress['value']=35
    progress.update()
    Invoice_No(lines,num_lines)
def Invoice_No(lines,num_lines):
    for x in range(num_lines-1):
        line=lines[x]
        i,i2="INVOICE","Invoice"
        if i in line:
            line=line.split(" ")
            q=0
            ql=len(line)
            h1,h2,h3,h4,h5,h6,h7,h8,h9,h0="1","2","3","4","5","6","7","8","9","0"
            for q in range (q,ql):
                n=line[q]
                
                if h1 in n:
                    v17.append(n)
                    continue
                if h2 in n:
                    v17.append(n)
                    continue
                if h3 in n:
                    v17.append(n)
                    continue
                if h4 in n:
                    v17.append(n)
                    continue
                if h5 in n:
                    v17.append(n)
                    continue
                if h6 in n:
                    v17.append(n)
                    continue
                if h7 in n:
                    v17.append(n)
                    continue
                if h8 in n:
                    v17.append(n)
                    continue
                if h9 in n:
                    v17.append(n)
                    continue
                if h0 in n:
                    v17.append(n)
                    continue
        if i2 in line:
            line=line.split(" ")
            q=0
            ql=len(line)
            h1,h2,h3,h4,h5,h6,h7,h8,h9,h0="1","2","3","4","5","6","7","8","9","0"
            for q in range (q,ql):
                n=line[q]
                if h1 in n:
                    v17.append(n)
                    continue
                if h2 in n:
                    v17.append(n)
                    continue
                if h3 in n:
                    v17.append(n)
                    continue
                if h4 in n:
                    v17.append(n)
                    continue
                if h5 in n:
                    v17.append(n)
                    continue
                if h6 in n:
                    v17.append(n)
                    continue
                if h7 in n:
                    v17.append(n)
                    continue
                if h8 in n:
                    v17.append(n)
                    continue
                if h9 in n:
                    v17.append(n)
                    continue
                if h0 in n:
                    v17.append(n)
                    continue
    for x in range(num_lines-1):
        line=lines[x]
        line=line.split(" ")
        q=0
        ql=len(line)
        for i in range(q,ql):
            d=line[i]
            s="-"
            if s in d:
                ns=d.count("-")
                if ns==2:
                    v17.append(d)
    combobox17.config(value=v17)
    try:
        combobox17.set(v17[0])
    except:
        pass
    progress['value']=50
    progress.update()
    Seller_state()
def Seller_state():
    #State of Seller
    try:
        g = combobox6.get()
        g = g[0:2]
        for key in gstate.keys():
            if key == g :
                combobox5.set(gstate[key])
                break
    except:
        pass
    Buyer_state()
def Buyer_state():    #State of Buyer
    try:
        g = combobox12.get()
        g = g[0:2]
        for key in gstate.keys():
            if key == g :
                combobox11.set(gstate[key])
                break
    except:
        pass
    Filter_Name()
def Seller_state2():
    try:
        g = combobox6.get()
        g = g[0:2]
        for key in gstate.keys():
            if key == g :
                combobox5.set(gstate[key])
                break
    except:
        pass
def Buyer_state2():
    try:
        g = combobox12.get()
        g = g[0:2]
        for key in gstate.keys():
            if key == g :
                combobox11.set(gstate[key])
                break
    except:
        pass
"""
    
def Shipment_state() :   #State of Shipment
    try:
        g = combobox16.get()
        g = g[0:2]
        for key in gstate.keys():
            if key == g :
                combobox5.set(gstate[key])
                break
    except:
        pass
    progress['value']=55
    progress.update()
    Filter_Name()"""
def Filter_Name():
        image = Image.open(pathuni)
        w,h=image.size
        img=image.crop([0,0,w,h/2])
        t = image_to_string(img)
        f = open(r"data\new.txt","w")
        f.write(t)
        f.close()
        f=open(r"data\new.txt","r")
        lines=f.readlines()
        num_lines = sum(1 for line in open(r'data\new.txt'))
        for x in range(num_lines-1):
            line=lines[x]
            line=line.replace(".", "")
            line=line.replace("\n", "")
            x,y,tn,z,p,q,r,t,u,v,w,g,k="4","55","55","55","0","1","2","3","5","6","7","8","9"
            if len(line) <10 :
                continue
            elif len(line) >26:
                 continue
            elif x in line:
                 continue
            elif y in line:
                continue
            elif z in line :
                 continue
            elif t in line:
                continue
            elif tn in line:
                 continue
            elif p in line:
                 continue
            elif q in line:
                 continue
            elif r in line:
                 continue
            elif u in line:
                 continue
            elif v in line:
                 continue
            elif g in line:
                 continue
            elif k in line:
                 continue
            else:
                line=line.replace("For", "")
                if line.startswith(" "):
                    line.replace(" ","",1)
                v2.append(line)
                v910.append(line)
                continue
        combobox2.config(values=v2)
        combobox910.config(values=v910)
        progress['value']=70
        progress.update()
        Filter_Total()
def Filter_Total():
        image=Image.open(pathuni)
        w,h=image.size
        img=image.crop([0,h/2,w,h])
        t = image_to_string(img)
        f = open(r"data\new.txt","w")
        f.write(t)
        f.close()
        f=open(r"data\new.txt","r")
        lines=f.readlines()
        num_lines = sum(1 for line in open(r'data\new.txt'))
        for x in range(num_lines-1):
            line=lines[x]
            line=line.split(" ")
            ql=len(line)
            q=0
            for q in range(q,ql):
                l=line[q]
                l=l.replace(" ","")
                l=l.replace(",", "")
                l=l.replace("\n", "")
                l2=l
                l=l.replace(".","")
                if l.isnumeric():
                    v28.append(l2)
                    v33.append(l2)
        combobox28.config(values=v28)
        combobox33.config(values=v33)
        progress['value']=100
        progress.update()
        time.sleep(0.3)
        progress['value']=00
        progress.update()
def Open_Datafile():
    os.startfile("Data.csv")
def RESET():
    progress['value']=00
    for w in f1.winfo_children():
            try:
                w.set("")
            except:
                pass
            try:
                w.delete(1.0,"end-1c")
            except:
                continue
    canvas2.delete("all")
    v1.clear()
    v2.clear()
    v3.clear()
    v4.clear()
    v5.clear()
    v6.clear()
    v7.clear()
    v8.clear()
    v9.clear()
    v910.clear()
    v10.clear()
    v11.clear()
    v12.clear()
    v13.clear()
    v14.clear()
    v15.clear()
    v16.clear()
    v17.clear()
    v18.clear()
    v19.clear()
    v20.clear()
    v21.clear()
    v22.clear()
    v23.clear()
    v24.clear()
    v25.clear()
    v26.clear()
    v27.clear()
    v28.clear()
    v29.clear()
    v30.clear()
    v31.clear()
    v32.clear()
    v33.clear()
    v34.clear()
    v35.clear()
    for w in f1.winfo_children():
            try:
                w.update()
            except:
                pass
def motion(event):
    global security
    global arc
    global cords
    try:
        curX, curY = (event.x, event.y)
        if security==1:
            canvas2.delete(arc)
        else:
            pass
        arc = canvas2.create_rectangle(sx, sy, 1, 1)
        canvas2.coords(arc, sx, sy, curX, curY)
        security=1
    except:
        pass
def start(event):
    global pt
    global sx
    global sy
    sx, sy = event.x , event.y
def end(event):
    global unitext
    try:
        ex , ey = event.x , event.y
        img=image1.crop([sx,sy,ex,ey])
        t = image_to_string(img,lang='eng')
        f = open(r"data\new.txt","w")
        f.write(t)
        f.close()
        f=open(r"data\new.txt","r")
        lines=f.readlines()
        fl=[]
        num_lines = sum(1 for line in open(r'data\new.txt'))
        for x in range(num_lines-1):
            line=lines[x]
            line=line.replace(".", "")
            line=line.replace("\n", " ")
            fl.append(line)
        final=str()
        final=''.join(fl)
        if radiovar.get() == 0:
            tk.messagebox.showinfo(title="Error",message="Column not recognized")
        elif radiovar.get() == 1:
            combobox1.set(final)
        elif radiovar.get() == 2:
            combobox2.set(final)
        elif radiovar.get() == 3:
            text3.insert("end-1c",final)
        elif radiovar.get() == 4:
            combobox4.set(final)
        elif radiovar.get() == 5:
            combobox5.set(final)
        elif radiovar.get() == 6:
            combobox6.set(final)
        elif radiovar.get() == 7:
            combobox7.set(final)
        elif radiovar.get() == 8:
            combobox8.set(final)
        elif radiovar.get() == 9:
            text9.insert("end-1c",final)
        elif radiovar.get() == 10:
            combobox10.set(final)
        elif radiovar.get() == 11:
            combobox11.set(final)
        elif radiovar.get() == 12:
            combobox12.set(final)
        elif radiovar.get() == 13:
            combobox13.set(final)
        elif radiovar.get() == 14:
            combobox14.set(final)
        elif radiovar.get() == 15:
            combobox15.set(final)
        elif radiovar.get() == 16:
            combobox16.set(final)
        elif radiovar.get() == 17:
            combobox17.set(final)
        elif radiovar.get() == 18:
            combobox18.set(final)
        elif radiovar.get() == 19:
            combobox19.set(final)
        elif radiovar.get() == 20:
            combobox20.set(final)
        elif radiovar.get() == 21:
            combobox21.set(final)
        elif radiovar.get() == 22:
            combobox22.set(final)
        elif radiovar.get() == 23:
            combobox23.set(final)
        elif radiovar.get() == 24:
             text24.insert("end-1c",final)
        elif radiovar.get() == 25:
            combobox25.set(final)
        elif radiovar.get() == 26:
            combobox26.set(final)
        elif radiovar.get() == 27:
            combobox27.set(final)
        elif radiovar.get() == 28:
            combobox28.set(final)
        elif radiovar.get() == 29:
            combobox29.set(final)
        elif radiovar.get() == 30:
            combobox30.set(final)
        elif radiovar.get() == 31:
            combobox31.set(final)
        elif radiovar.get() == 32:
            combobox32.set(final)
        elif radiovar.get() == 33:
            combobox33.set(final)
        elif radiovar.get() == 34:
            combobox34.set(final)
        elif radiovar.get() == 35:
            combobox35.set(final)
        elif radiovar.get() == 910:
            combobox910.set(final)
    except:
        pass
def Cancel(event):
    try:
        canvas2.delete(arc)
        if radiovar.get()==1:
            combobox1.set("")
        elif radiovar.get()==2:
            combobox2.set("")
        elif radiovar.get()==4:
            combobox4.set("")
        elif radiovar.get()==3:
            text3.delete(1.0,"end-1c")
        elif radiovar.get()==5:
            combobox5.set("")
        elif radiovar.get()==6:
            combobox6.set("")
        elif radiovar.get()==7:
            combobox7.set("")
        elif radiovar.get()==8:
            combobox8.set("")
        elif radiovar.get()==9:
            text9.delete(1.0,"end-1c")
        elif radiovar.get()==10:
            combobox10.set("")
        elif radiovar.get()==11:
            combobox11.set("")
        elif radiovar.get()==12:
            combobox12.set("")
        elif radiovar.get()==13:
            combobox13.set("")
        elif radiovar.get()==14:
            combobox14.set("")
        elif radiovar.get()==15:
            combobox15.set("")
        elif radiovar.get()==16:
            combobox16.set("")
        elif radiovar.get()==17:
            combobox17.set("")
        elif radiovar.get()==18:
            combobox18.set("")
        elif radiovar.get()==19:
            combobox19.set("")
        elif radiovar.get()==20:
            combobox20.set("")
        elif radiovar.get()==21:
            combobox21.set("")
        elif radiovar.get()==22:
            combobox22.set("")
        elif radiovar.get()==23:
            combobox23.set("")
        elif radiovar.get()==24:
            text24.delete(1.0,"end-1c")
        elif radiovar.get()==25:
            combobox25.set("")
        elif radiovar.get()==26:
            combobox26.set("")
        elif radiovar.get()==27:
            combobox27.set("")
        elif radiovar.get()==28:
            combobox28.set("")
        elif radiovar.get()==29:
            combobox29.set("")
        elif radiovar.get()==30:
            combobox30.set("")
        elif radiovar.get()==31:
            combobox31.set("")
        elif radiovar.get()==32:
            combobox32.set("")
        elif radiovar.get()==33:
            combobox33.set("")
        elif radiovar.get()==34:
            combobox34.set("")
        elif radiovar.get()==35:
            combobox35.set("")
        elif radiovar.get()==910:
            combobox910.set("")
    except:
        pass
def fistf():
    if os.path.isfile("Data.csv")==True :
        pass
    else:
        tk.messagebox.showinfo(title="Error",message="Datafile not found, creted newone.")
        csvpath='Data.csv'
        with open(csvpath,'a',newline=('')) as datafile:
            writer=csv.writer(datafile,delimiter=",")
            vals=["Tax Invoice","Name of Seller","Address of Seller",
                  "City of Seller","State of Seller","GSTIN of Seller",
                  "Contact Number","Email Address",'Billed to ',
                  "Address of Receipient","City of Receipient",
                  "State of Receipient","GSTIN of Receipient",
                  "Shipped To","Place of Supply","Address of Supply",
                  "GSTIN of Shipment","Invoice Number","Invoice Date",
                  "PO No.","PO Date","Vehicle No.","Bilty No.","Bilty Date",
                  "Description of Goods","CGST","IGST","SGST","Total Amount",
                  "Tax Amount","Discount","Labour(Loading&Unloading)","Round off Amount",
                  "Grand Total","Bank Account No.","Bank IFSC Code"]
            writer.writerow(vals)
            datafile.close()
root=tk.Tk()
root.title("Build-To-Excel")
root.configure(bg="black")
root.geometry("1360x768")
root.minsize(1360,768)
photo = PhotoImage(file = r'data/26.ico')
root.iconphoto(False, photo)

fl=tk.LabelFrame(root,border=2,bg="black")
fr=tk.LabelFrame(root,border=2,bg="white")

fl1=tk.Frame(fl,bg="light grey")
fl1.pack(side="top")

fl2=tk.LabelFrame(fl,bg="light grey")
fl2.pack(side="bottom",fill="both",expand="yes")
fb=tk.Frame(fl2,bg="light grey")
fb.pack(side="right",fill="y")
canvas = tk.Canvas(fl2,bg="light grey")
scrollbar = ttk.Scrollbar(fl2, orient="vertical" , command=canvas.yview)
f1 = tk.Frame(canvas,background="light grey")

f1.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=f1, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand="yes")
scrollbar.pack(side="right", fill="y")

global value
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='green', background='black')
progress = ttk.Progressbar(fl1,style="red.Horizontal.TProgressbar",length=680,maximum=100,mode="determinate")
progress.pack(side="bottom",anchor="n",fill="x")


label1=tk.Label(fl1,bg="white",fg="red",text="Check The Values Here",font="times 15 bold ",border=3,relief='solid',padx=40,pady=6)
label2=tk.Label(f1,bg="white",fg="red",text="Tax Invoice :",font="times 12 bold ",border=2,relief='solid',pady=6,padx=20)
label3=tk.Label(f1,bg="white",fg="red",text="Name of Seller :",font="times 12 bold",border=2,relief='solid',pady=6)
label4=tk.Label(f1,bg="white",fg="red",text="Address of Seller :",font="times 12 bold",border=2,relief='solid',pady=6)
label5=tk.Label(f1,bg="white",fg="red",text="City of Seller :",font="times 12 bold",border=2,relief='solid',pady=6)
label6=tk.Label(f1,bg="white",fg="red",text="State of Seller:",font="times 12 bold",border=2,relief='solid',pady=6)
label7=tk.Label(f1,bg="white",fg="red",text="GSTIN of Seller :",font="times 12 bold ",border=2,relief='solid',pady=6)
label8=tk.Label(f1,bg="white",fg="red",text="Contact Nummber :",font="times 12 bold",border=2,relief='solid',pady=6)
label9=tk.Label(f1,bg="white",fg="red",text="Email Address :",font="times 12 bold",border=2,relief='solid',pady=6)
label910=tk.Label(f1,bg="white",fg="red",text="Billed To  :",font="times 12 bold",border=2,relief='solid',pady=6)
label10=tk.Label(f1,bg="white",fg="red",text="Address of Receipient :",font="times 12 bold",border=2,relief='solid',pady=6)
label11=tk.Label(f1,bg="white",fg="red",text="City of Receipient :",font="times 12 bold ",border=2,relief='solid',pady=6)
label12=tk.Label(f1,bg="white",fg="red",text="State of Receipient :",font="times 12 bold",border=2,relief='solid',pady=6)
label13=tk.Label(f1,bg="white",fg="red",text="GSTIN of Receipient :",font="times 12 bold",border=2,relief='solid',pady=6)
label14=tk.Label(f1,bg="white",fg="red",text="Shipped To :",font="times 12 bold",border=2,relief='solid',pady=6)
label15=tk.Label(f1,bg="white",fg="red",text="Place of Supply :",font="times 12 bold",border=2,relief='solid',pady=6)
label16=tk.Label(f1,bg="white",fg="red",text="Address of Supply :",font="times 12 bold",border=2,relief='solid',pady=6)
label17=tk.Label(f1,bg="white",fg="red",text="GSTIN of Shipment :",font="times 12 bold",border=2,relief='solid',pady=6)
label18=tk.Label(f1,bg="white",fg="red",text="Invoice Number :",font="times 12 bold",border=2,relief='solid',pady=6)
label19=tk.Label(f1,bg="white",fg="red",text="Invoice Date :",font="times 12 bold",border=2,relief='solid',pady=6)
label20=tk.Label(f1,bg="white",fg="red",text="PO No. :",font="times 12 bold",border=2,relief='solid',pady=6)
label21=tk.Label(f1,bg="white",fg="red",text="PO Date :",font="times 12 bold",border=2,relief='solid',pady=6)
label22=tk.Label(f1,bg="white",fg="red",text="Vehicle No.:",font="times 12 bold",border=2,relief='solid',pady=6)
label23=tk.Label(f1,bg="white",fg="red",text="Bilty No.:",font="times 12 bold",border=2,relief='solid',pady=6)
label24=tk.Label(f1,bg="white",fg="red",text="Bilty Date :",font="times 12 bold",border=2,relief='solid',pady=6)
label25=tk.Label(f1,bg="white",fg="red",text="Description of Goods :",font="times 12 bold",border=2,relief='solid',pady=6)
label26=tk.Label(f1,bg="white",fg="red",text="CGST :",font="times 12 bold",border=2,relief='solid',pady=6)
label27=tk.Label(f1,bg="white",fg="red",text="IGST :",font="times 12 bold",border=2,relief='solid',pady=6)
label28=tk.Label(f1,bg="white",fg="red",text="SGST :",font="times 12 bold",border=2,relief='solid',pady=6)
label29=tk.Label(f1,bg="white",fg="red",text="Total Amount :",font="times 12 bold",border=2,relief='solid',pady=6)
label30=tk.Label(f1,bg="white",fg="red",text="Tax Amount :",font="times 12 bold",border=2,relief='solid',pady=6)
label31=tk.Label(f1,bg="white",fg="red",text="Discount :",font="times 12 bold",border=2,relief='solid',pady=6)
label32=tk.Label(f1,bg="white",fg="red",text="Labour(loading&unloading) :",font="times 10 bold",border=2,relief='solid',pady=6)
label33=tk.Label(f1,bg="white",fg="red",text="Round off Amount :",font="times 12 bold",border=2,relief='solid',pady=6)
label34=tk.Label(f1,bg="white",fg="red",text="Grand Total :",font="times 12 bold",border=2,relief='solid',pady=6)
label35=tk.Label(f1,bg="white",fg="red",text="Bank Account No. :",font="times 12 bold",border=2,relief='solid',pady=6)
label36=tk.Label(f1,bg="white",fg="red",text="Bank IFSC Code:",font="times 12 bold",border=2,relief='solid',pady=6)

label1.pack(side="top",pady=5)
label2.grid(row=0,column=0,sticky='nswe',pady=4,padx=5)
label3.grid(row=1,column=0,sticky='nswe',pady=4,padx=5)
label4.grid(row=2,column=0,sticky='nswe',pady=4,padx=5)
label5.grid(row=3,column=0,sticky='nswe',pady=4,padx=5)
label6.grid(row=4,column=0,sticky='nswe',pady=4,padx=5)
label7.grid(row=5,column=0,sticky='nswe',pady=4,padx=5)
label8.grid(row=6,column=0,sticky='nswe',pady=4,padx=5)
label9.grid(row=7,column=0,sticky='nswe',pady=4,padx=5)
label910.grid(row=8,column=0,sticky='nswe',pady=4,padx=5)
label10.grid(row=9,column=0,sticky='nswe',pady=4,padx=5)
label11.grid(row=10,column=0,sticky='nswe',pady=4,padx=5)
label12.grid(row=11,column=0,sticky='nswe',pady=4,padx=5)
label13.grid(row=12,column=0,sticky='nswe',pady=4,padx=5)
label14.grid(row=13,column=0,sticky='nswe',pady=4,padx=5)
label15.grid(row=14,column=0,sticky='nswe',pady=4,padx=5)
label16.grid(row=15,column=0,sticky='nswe',pady=4,padx=5)
label17.grid(row=16,column=0,sticky='nswe',pady=4,padx=5)
label18.grid(row=17,column=0,sticky='nswe',pady=4,padx=5)
label19.grid(row=18,column=0,sticky='nswe',pady=4,padx=5)
label20.grid(row=19,column=0,sticky='nswe',pady=4,padx=5)
label21.grid(row=20,column=0,sticky='nswe',pady=4,padx=5)
label22.grid(row=21,column=0,sticky='nswe',pady=4,padx=5)
label23.grid(row=22,column=0,sticky='nswe',pady=4,padx=5)
label24.grid(row=23,column=0,sticky='nswe',pady=4,padx=5)
label25.grid(row=24,column=0,sticky='nswe',pady=4,padx=5)
label26.grid(row=25,column=0,sticky='nswe',pady=4,padx=5)
label27.grid(row=26,column=0,sticky='nswe',pady=4,padx=5)
label28.grid(row=27,column=0,sticky='nswe',pady=4,padx=5)
label29.grid(row=28,column=0,sticky='nswe',pady=4,padx=5)
label30.grid(row=29,column=0,sticky='nswe',pady=4,padx=5)
label31.grid(row=30,column=0,sticky='nswe',pady=4,padx=5)
label32.grid(row=31,column=0,sticky='nswe',pady=4,padx=5)
label33.grid(row=32,column=0,sticky='nswe',pady=4,padx=5)
label34.grid(row=33,column=0,sticky='nswe',pady=4,padx=5)
label35.grid(row=34,column=0,sticky='nswe',pady=4,padx=5)
label36.grid(row=35,column=0,sticky='nswe',pady=4,padx=5)

global v1
global v2
global v3
global v4
global v5
global v6
global v7
global v8
global v9
global v910
global v10
global v11
global v12
global v13
global v14
global v15
global v16
global v17
global v18
global v19
global v20
global v21
global v22
global v23
global v24
global v25
global v26
global v27
global v28
global v29
global v30
global v31
global v32
global v33
global v34
global v35

v1=[]
v2=[]
v3=[]
v4=[]
v5=[]
v6=[]
v7=[]
v8=[]
v9=[]
v910=[]
v10=[]
v11=[]
v12=[]
v13=[]
v14=[]
v15=[]
v16=[]
v17=[]
v18=[]
v19=[]
v20=[]
v21=[]
v22=[]
v23=[]
v24=[]
v25=[]
v26=[]
v27=[]
v28=[]
v29=[]
v30=[]
v31=[]
v32=[]
v33=[]
v34=[]
v35=[]

combobox1=ttk.Combobox(f1,values=v1,font=" times 11 bold ",width=35)
combobox2=ttk.Combobox(f1,values=v2,font=" times 11 bold ",width=35)
text3=tk.Text(f1,font=" times 11 bold ",width=35,height=3)
combobox4=ttk.Combobox(f1,values=v3,font=" times 11 bold ",width=35)
combobox5=ttk.Combobox(f1,values=v5,font=" times 11 bold ",width=35)
combobox6=ttk.Combobox(f1,values=v6,font=" times 11 bold ",width=35)
combobox7=ttk.Combobox(f1,values=v7,font=" times 11 bold ",width=35)
combobox8=ttk.Combobox(f1,values=v9,font=" times 11 bold ",width=35)
combobox910=ttk.Combobox(f1,values=v910,font=" times 11 bold ",width=35)
text9=tk.Text(f1,font=" times 11 bold ",width=35,height=3)
combobox10=ttk.Combobox(f1,values=v10,font=" times 11 bold ",width=35)
combobox11=ttk.Combobox(f1,values=v11,font=" times 11 bold ",width=35)
combobox12=ttk.Combobox(f1,values=v12,font=" times 11 bold ",width=35)
combobox13=ttk.Combobox(f1,values=v13,font=" times 11 bold ",width=35)
combobox14=ttk.Combobox(f1,values=v14,font=" times 11 bold ",width=35)
combobox15=ttk.Combobox(f1,values=v15,font=" times 11 bold ",width=35)
combobox16=ttk.Combobox(f1,values=v16,font=" times 11 bold ",width=35)
combobox17=ttk.Combobox(f1,values=v17,font=" times 11 bold ",width=35)
combobox18=ttk.Combobox(f1,values=v18,font=" times 11 bold ",width=35)
combobox19=ttk.Combobox(f1,values=v19,font=" times 11 bold ",width=35)
combobox20=ttk.Combobox(f1,values=v20,font=" times 11 bold ",width=35)
combobox21=ttk.Combobox(f1,values=v21,font=" times 11 bold ",width=35)
combobox22=ttk.Combobox(f1,values=v22,font=" times 11 bold ",width=35)
combobox23=ttk.Combobox(f1,values=v23,font=" times 11 bold ",width=35)
text24=tk.Text(f1,font=" times 11 bold ",width=35,height=4)
combobox25=ttk.Combobox(f1,values=v25,font=" times 11 bold ",width=35)
combobox26=ttk.Combobox(f1,values=v26,font=" times 11 bold ",width=35)
combobox27=ttk.Combobox(f1,values=v27,font=" times 11 bold ",width=35)
combobox28=ttk.Combobox(f1,values=v28,font=" times 11 bold ",width=35)
combobox29=ttk.Combobox(f1,values=v29,font=" times 11 bold ",width=35)
combobox30=ttk.Combobox(f1,values=v30,font=" times 11 bold ",width=35)
combobox31=ttk.Combobox(f1,values=v31,font=" times 11 bold ",width=35)
combobox32=ttk.Combobox(f1,values=v32,font=" times 11 bold ",width=35)
combobox33=ttk.Combobox(f1,values=v33,font=" times 11 bold ",width=35)
combobox34=ttk.Combobox(f1,values=v34,font=" times 11 bold ",width=35)
combobox35=ttk.Combobox(f1,values=v35,font=" times 11 bold ",width=35)

combobox1.grid(row=0,column=1)
combobox2.grid(row=1,column=1)
text3.grid(row=2,column=1)
combobox4.grid(row=3,column=1)
combobox5.grid(row=4,column=1)
combobox6.grid(row=5,column=1)
combobox7.grid(row=6,column=1)
combobox8.grid(row=7,column=1)
combobox910.grid(row=8,column=1)
text9.grid(row=9,column=1)
combobox10.grid(row=10,column=1)
combobox11.grid(row=11,column=1)
combobox12.grid(row=12,column=1)
combobox13.grid(row=13,column=1)
combobox14.grid(row=14,column=1)
combobox15.grid(row=15,column=1)
combobox16.grid(row=16,column=1)
combobox17.grid(row=17,column=1)
combobox18.grid(row=18,column=1)
combobox19.grid(row=19,column=1)
combobox20.grid(row=20,column=1)
combobox21.grid(row=21,column=1)
combobox22.grid(row=22,column=1)
combobox23.grid(row=23,column=1)
text24.grid(row=24,column=1)
combobox25.grid(row=25,column=1)
combobox26.grid(row=26,column=1)
combobox27.grid(row=27,column=1)
combobox28.grid(row=28,column=1)
combobox29.grid(row=29,column=1)
combobox30.grid(row=30,column=1)
combobox31.grid(row=31,column=1)
combobox32.grid(row=32,column=1)
combobox33.grid(row=33,column=1)
combobox34.grid(row=34,column=1)
combobox35.grid(row=35,column=1)


global radiovar
radiovar=tk.IntVar()
radio1=tk.Radiobutton(f1,value=1,variable=radiovar)
radio2=tk.Radiobutton(f1,value=2,variable=radiovar)
radio3=tk.Radiobutton(f1,value=3,variable=radiovar)
radio4=tk.Radiobutton(f1,value=4,variable=radiovar)
radio5=tk.Radiobutton(f1,value=5,variable=radiovar,command=Seller_state2)
radio6=tk.Radiobutton(f1,value=6,variable=radiovar)
radio7=tk.Radiobutton(f1,value=7,variable=radiovar)
radio8=tk.Radiobutton(f1,value=8,variable=radiovar)
radio9=tk.Radiobutton(f1,value=9,variable=radiovar)

radio910=tk.Radiobutton(f1,value=910,variable=radiovar)

radio10=tk.Radiobutton(f1,value=10,variable=radiovar)
radio11=tk.Radiobutton(f1,value=11,variable=radiovar,command=Buyer_state2)
radio12=tk.Radiobutton(f1,value=12,variable=radiovar)
radio13=tk.Radiobutton(f1,value=13,variable=radiovar)
radio14=tk.Radiobutton(f1,value=14,variable=radiovar)
radio15=tk.Radiobutton(f1,value=15,variable=radiovar)
radio16=tk.Radiobutton(f1,value=16,variable=radiovar)
radio17=tk.Radiobutton(f1,value=17,variable=radiovar)
radio18=tk.Radiobutton(f1,value=18,variable=radiovar)
radio19=tk.Radiobutton(f1,value=19,variable=radiovar)
radio20=tk.Radiobutton(f1,value=20,variable=radiovar)
radio21=tk.Radiobutton(f1,value=21,variable=radiovar)
radio22=tk.Radiobutton(f1,value=22,variable=radiovar)
radio23=tk.Radiobutton(f1,value=23,variable=radiovar)
radio24=tk.Radiobutton(f1,value=24,variable=radiovar)
radio25=tk.Radiobutton(f1,value=25,variable=radiovar)
radio26=tk.Radiobutton(f1,value=26,variable=radiovar)
radio27=tk.Radiobutton(f1,value=27,variable=radiovar)
radio28=tk.Radiobutton(f1,value=28,variable=radiovar)
radio29=tk.Radiobutton(f1,value=29,variable=radiovar)
radio30=tk.Radiobutton(f1,value=30,variable=radiovar)
radio31=tk.Radiobutton(f1,value=31,variable=radiovar)
radio32=tk.Radiobutton(f1,value=32,variable=radiovar)
radio33=tk.Radiobutton(f1,value=33,variable=radiovar)
radio34=tk.Radiobutton(f1,value=34,variable=radiovar)
radio35=tk.Radiobutton(f1,value=35,variable=radiovar)

radio1.grid(row=0,column=2,padx=5)
radio2.grid(row=1,column=2,padx=5)
radio3.grid(row=2,column=2,padx=5)
radio4.grid(row=3,column=2,padx=5)
radio5.grid(row=4,column=2,padx=5)
radio6.grid(row=5,column=2,padx=5)
radio7.grid(row=6,column=2,padx=5)
radio8.grid(row=7,column=2,padx=5)
radio910.grid(row=8,column=2,padx=5)

radio9.grid(row=9,column=2,padx=5)

radio10.grid(row=10,column=2,padx=5)
radio11.grid(row=11,column=2,padx=5)
radio12.grid(row=12,column=2,padx=5)
radio13.grid(row=13,column=2,padx=5)
radio14.grid(row=14,column=2,padx=5)
radio15.grid(row=15,column=2,padx=5)
radio16.grid(row=16,column=2,padx=5)
radio17.grid(row=17,column=2,padx=5)
radio18.grid(row=18,column=2,padx=5)
radio19.grid(row=19,column=2,padx=5)
radio20.grid(row=20,column=2,padx=5)
radio21.grid(row=21,column=2,padx=5)
radio22.grid(row=22,column=2,padx=5)
radio23.grid(row=23,column=2,padx=5)
radio24.grid(row=24,column=2,padx=5)
radio25.grid(row=25,column=2,padx=5)
radio26.grid(row=26,column=2,padx=5)
radio27.grid(row=27,column=2,padx=5)
radio28.grid(row=28,column=2,padx=5)
radio29.grid(row=29,column=2,padx=5)
radio30.grid(row=30,column=2,padx=5)
radio31.grid(row=31,column=2,padx=5)
radio32.grid(row=32,column=2,padx=5)
radio33.grid(row=33,column=2,padx=5)
radio34.grid(row=34,column=2,padx=5)
radio35.grid(row=35,column=2,padx=5)


canvas2=tk.Canvas(fr,bg="black",cursor="circle")
canvas2.pack(fill="both",expand="yes")

fl.pack(fill="y",side="left")
fr.pack(side="right",fill="both",expand="yes")

canvas2.bind('<ButtonPress-1>',start)
canvas2.bind('<ButtonRelease-1>',end)
canvas2.bind('<B1-Motion>', motion)
canvas2.bind('<ButtonPress-3>',Cancel)
global security
global pt
security=0
pt=1
b3=tk.Button(fb,command=Open_Datafile,text="DATAFILE",fg="red",font="times 10 bold",border=2,relief='solid',padx=27)
b3.grid(pady=40)
b4=tk.Button(fb,command=RESET,text="RESET",fg="red",font="times 10 bold",border=2,relief='solid',padx=43)
b4.grid(pady=40)
b1=tk.Button(fb,command=Select_Image,text="SELECT IMAGE",fg="red",font="times 10 bold",border=2,relief='solid',padx=15)
b1.grid(padx=13,pady=40)
b6=tk.Button(fb,command=Do_Back,text="BACK",fg="red",font="times 10 bold",border=2,relief='solid',padx=37)
b6.grid(pady=40)
b5=tk.Button(fb,command=Do_Next,text="NEXT",fg="red",font="times 10 bold",border=2,relief='solid',padx=37)
b5.grid(pady=40)
b2=tk.Button(fb,command=Save_Values,text="SAVE",fg="red",font="times 10 bold",border=2,relief='solid',padx=30)
b2.grid(pady=40)

gstate = {
    "35":"Andaman and Nicobar Islands",
    "28":"Andhra Pradesh",
    "37":"Andhra Pradesh(New)",
    "12":"Arunachal Pradesh",
    "18":"Assam",
    "10":"Bihar",
    "04":"Chandigarh",
    "22":"Chattisgarh",
    "26":"Dadra and Nagar Haveli",
    "25":"Daman and Diu",
    "07":"Delhi",
    "30":"Goa",
    "24":"Gujarat",
    "06":"Haryana",
    "02":"Himachal Pradesh",
    "01":"Jammu and Kashmir",
    "20":"Jharkhand",
    "29":"Karnataka",
    "32":"Kerala",
    "31":"Lakshdeep Islands",
    "23":"Madhya Pradesh",
    "27":"Maharashtra",
    "14":"Manipur",
    "17":"Meghalaya",
    "15":"Mizoram",
    "13":"Nagaland",
    "21":"Odisa",
    "34":"Pondicherry",
    "03":"Punjab",
    "08":"Rajasthan",
    "11":"Sikkim",
    "33":"Tamil Nadu",
    "36":"Telangana",
    "16":"Tripura",
    "09":"Uttar Pradesh",
    "05":"Uttrakhand",
    "19":"West Bengal"
    }

fistf()

root.mainloop()
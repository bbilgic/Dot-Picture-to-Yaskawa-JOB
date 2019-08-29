#  -*- coding: cp1254 -*-
from gui import GUI
from tkinter import messagebox,filedialog
from tkinter import *
import sys
import tkinter as tk
import threading
from PIL import Image,ImageDraw
import PIL.ImageOps  
import math
import time
from datetime import datetime
global root,My_GUI,pic_path,pixel_rate
pixel_rate=None

def SelectPic():
    """
    SelectPic [Select .jpg and .png picture with this function]:

    """
    global My_GUI,root,pic_path,pixel_rate
    pic_path = filedialog.askopenfilename(filetypes = (("JPG Dosyası", "*.jpg"),("PNG Dosyası", "*.png")))

    if not pic_path== '':
            My_GUI.PicLabel.delete(0,END)
            My_GUI.PicLabel.insert(0,pic_path)
            try:
                img = Image.open(pic_path)
            except:
                messagebox.showerror("Hata", "Geçersiz resim dosyası !!!", parent=root)

            if img.mode == 'RGBA':
                r,g,b,a = img.split()
                img = Image.merge('RGB', (r,g,b))
            if img.mode == 'RGB':
                width_org, height_org = img.size
                print(str(width_org)+": :"+str(height_org))
                My_GUI.PicHeight.delete(0,END)
                My_GUI.Picwidth.delete(0,END)
                My_GUI.PicHeight.insert(0,height_org)
                My_GUI.Picwidth.insert(0,width_org)
                pixel_rate=width_org/height_org
                My_GUI.ProgressLabel.configure(text="Resim yüklendi.")
            else:
                messagebox.showerror("Hata", "Geçersiz resim dosyası, lütfen  .png veya .jpg formatı kullanın.", parent=root)
    else:
            messagebox.showerror("Hata", "Dosya seçilmedi !!!", parent=root)




def Counting(Number):
    """
    Counting [Get digit a number]:
    
    Arguments:
        Number int -- Number to be found digit

    Returns:
        Count int -- Return digit for given number
    """
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count


def print_progress(transferred):
    """
    print_progress [Progress bar updater]: 

    Arguments:
        transferred [int] -- [progress step]
    """
   
    global My_GUI,root
    My_GUI.TProgressbar1["maximum"] = 100
    My_GUI.TProgressbar1["value"] = transferred

def CreateJob():
    """CreateJob [Create Job file from given picture]:
        
    """
    global root,My_GUI,pic_path
    pic_path=My_GUI.PicLabel.get()
    My_GUI.ProgressLabel.configure(text="Resim işleniyor ...")
    if not pic_path == '':
        img = Image.open(pic_path)
        if img.mode == 'RGBA':
            background = Image.new('RGBA', img.size, (255,255,255))
            img = Image.alpha_composite(background, img)

        img = img.rotate(180)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        width_org, height_org = img.size
        width = int(My_GUI.Picwidth.get())
        height = int(My_GUI.PicHeight.get())
        #img = PIL.ImageOps.invert(img)
        thresh = int(My_GUI.Threshold.get()) 

        if thresh==0:
            img = img.convert('1')
        else:
            fn = lambda x : 255 if x > thresh else 0
            img = img.convert('L').point(fn, mode='1')

        img = img.resize((width, height),Image.ANTIALIAS) 
        data = []
        for x in range(img.width):
            for y in range(img.height):
                pixel=img.getpixel((x,y))
                if  pixel == 0:
                    data.append(str(x)+','+str(y))
        max_row=My_GUI.MaxRow.get()
        max_dots=math.ceil((int(max_row)-50)/3)
        data_size=len(data)
        for i in range(101):
            progress_count=i*1
            time.sleep(0.01)
            print_progress(progress_count)
        file_count = math.ceil(data_size/max_dots)
        My_GUI.ProgressLabel2.configure(text="Pixel Sayısı: "+str(data_size)+", Max nokta: "+str(max_dots)+", Dosyası sayısı: "+str(file_count))
        
        time.sleep(3)
        print_progress(0)
        for i in range(file_count):
            jobname=(My_GUI.JobName.get()+'-'+str(i+1)).upper()
            My_GUI.ProgressLabel.configure(text=jobname+" dosyası hazırlanıyor...")
            
            with open(jobname+'.JBI', 'w') as output:
                start = int(i*max_dots)
                end = int((i+1)*max_dots)
                NPOS_count=len(data[start:end])
                USER=1
                TOOL=4
                OFFSET=My_GUI.Offset.get()
                output.write("/JOB\n//NAME "+jobname+"\n//POS\n///NPOS "+str(NPOS_count)+",0,0,0,0,0\n")
                output.write("///USER "+str(USER)+"\n///TOOL "+str(TOOL)+"\n///POSTYPE USER\n///RECTAN\n")
                output.write("///RCONF 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n")
                for index,item in enumerate(data[start:end]):
                    progress_count=index*1/100
                    print_progress(progress_count)
                    pos_index=''
                    for i in range(5-Counting(index)):
                            pos_index=pos_index+"0"
                    pos_index=pos_index+str(index)
                    if index == 0:
                        pos_index="00000"
                    coord=item.split(",")
                    x_offset=int(My_GUI.XBegin.get())
                    y_offset=int(My_GUI.YBegin.get())
                    x=str((int(coord[0])+x_offset)*float(OFFSET))
                    y=str((int(coord[1])+y_offset)*float(OFFSET))
                    z=My_GUI.ZBegin.get()
                    Rx=My_GUI.RxBegin.get()
                    Ry=My_GUI.RyBegin.get()
                    Rz=My_GUI.RzBegin.get()
                    output.write("C"+pos_index+"="+x+".000,"+y+".000,"+z+","+Rx+","+Ry+","+Rz+"\n")

                current_date=datetime.now().strftime('%Y/%m/%d %H:%M')
               
                output.write("//INST\n///DATE "+str(current_date)+"\n///ATTR SC,RW,RJ\n////FRAME USER "+str(USER)+"\n///GROUP1 RB1\nNOP\n")   
                
                for index,item in enumerate(data[start:end]):
                    print_progress(progress_count+index*4/100)
                    pos_index=''
                    for i in range(5-Counting(index)):
                        pos_index=pos_index+"0"
                    pos_index=pos_index+str(index)
                    if index == 0:
                        pos_index="00000"
                    speed=My_GUI.Speed.get()
                    call_job=(My_GUI.CallJob.get()).upper()
                    output.write("MOVL C"+pos_index+" V="+speed+"\n")
                    output.write("CALL JOB:"+call_job+"\n")
                output.write("END\n")
                output.close()
    
        messagebox.showinfo("Bilgi", "Resim koordinatları başarılı şekilde işlenerek dosyalara yazıldı.", parent=root)
        My_GUI.ProgressLabel.configure(text="")
        My_GUI.ProgressLabel2.configure(text="")
        print_progress(0)
    else:
        messagebox.showerror("Hata", "Dosya seçilmedi !!!", parent=root)

def job_to_picture():
    """job_to_picture [Create picture from given job files]:
            
    
    """
    pics = filedialog.askopenfilenames(filetypes = (("Job Dosyası", "*.JBI"),))
    lst = list(pics)
    data_x=[]
    data_y=[]
    if not pics == '':
        for index,item in enumerate(lst):

            with open(item, 'r') as output:
                content = output.readlines()
                for index,item in enumerate(content):
                    if "C0" in item and "," in item:
                        coords=item.split("=")
                        coords=coords[1]
                        coords=coords.split(",")
                        x=coords[0].split(".")
                        x=x[0]
                        y=coords[1].split(".")
                        y=y[0]
                        data_x.append(int(x))
                        data_y.append(int(y))
                img = Image.new("RGB", (max(data_x),max(data_y)), "white")
                draw = ImageDraw.Draw(img)
                dotSize=float(My_GUI.DotSize.get())
                for index,item in enumerate(data_x):
                    x=data_x[index]
                    y=data_y[index]
                    draw.rectangle([x,y,x+dotSize-1,y+dotSize-1], fill="black")
        img = img.rotate(180)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.show()  
        messagebox.showinfo("Bilgi", "Koordinatların resmi oluşturuldu.", parent=root)

def height_changed(event):
    """height_changed [recalculate weight]:

    Arguments:
          event {[*kwarg]} -- [change event]
    """
    global pixel_rate
    if pixel_rate:
        width=int(My_GUI.Picwidth.get())
        if not My_GUI.PicHeight.get():
            height=(1/pixel_rate)*width
            My_GUI.PicHeight.delete(0,END)
            My_GUI.PicHeight.insert(0,int(height))
        height=int(My_GUI.PicHeight.get())
        My_GUI.Picwidth.delete(0,END)
        width=(pixel_rate)*height
        My_GUI.Picwidth.insert(0,int(width))

def width_changed(event):
    """width_changed [recalculate height]:
    
    Arguments:
          event {[*kwarg]} -- [change event]
    """
    if pixel_rate:
        height=int(My_GUI.PicHeight.get())
        if not My_GUI.Picwidth.get():
            width=(pixel_rate)*height
            My_GUI.Picwidth.delete(0,END)
            My_GUI.Picwidth.insert(0,int(width))
        width=int(My_GUI.Picwidth.get())
        My_GUI.PicHeight.delete(0,END)
        height=(1/pixel_rate)*width
        My_GUI.PicHeight.insert(0,int(height))


def pic_input(d, P, s,W,V,n):
    """pic_input [validate given height or weight]:
    
    Arguments:
        d {[String]} -- [0 - delete 1 - insert]
        P {[String]} -- [event before string]
        s {[String]} -- [event after string]
        W {[String]} -- [widget name]
        V {[String]} -- [event type]
        n {[String]} -- [max string]
    Returns:
        [Boolean] -- [validate true or false]
    """
    #print("tr_input: d='%s' P='%s' s='%s'  W='%s' V='%s'" % (d,P,s,W,V))
    if d=='0':
        return True
    if len(P)> int(n):
        return False
    if not P.isdigit():
            return False
    return True


def set_defaults():
    """set_defaults [Give default values]:
    """

    vcmd = (My_GUI.TLabelframe1.register(pic_input), '%d', '%P', '%s','%W','%V',5)
    My_GUI.PicHeight.configure(validate="key",validatecommand=vcmd)
    My_GUI.Picwidth.configure(validate="key",validatecommand=vcmd)
    My_GUI.SelectPic.configure(command=lambda: threading.Thread(target=SelectPic, args=[]).start())
    My_GUI.CreateJob.configure(command=lambda: threading.Thread(target=CreateJob, args=[]).start())
    My_GUI.Preview.configure(command=lambda: threading.Thread(target=job_to_picture, args=[]).start())
    My_GUI.JobName.insert(0,"Deneme")
    My_GUI.RxBegin.insert(0,"0.4770")
    My_GUI.Threshold.insert(0,"100")
    My_GUI.RyBegin.insert(0,"1.8596")
    My_GUI.RzBegin.insert(0,"20.4638")
    My_GUI.XBegin.insert(0,"0")
    My_GUI.YBegin.insert(0,"0")
    My_GUI.ZBegin.insert(0,"2.000")
    My_GUI.Speed.insert(0,"120")
    My_GUI.Offset.insert(0,"1.0")
    My_GUI.CallJob.insert(0,"Kaynak")
    My_GUI.MaxRow.insert(0,"14950")
    My_GUI.DotSize.insert(0,"1.0")
    My_GUI.PicHeight.bind('<KeyRelease>', height_changed)   
    My_GUI.Picwidth.bind('<KeyRelease>', width_changed)   




def main_func():
    """main_func [everyone need a main function]:
    """
    global root,My_GUI
    root = tk.Tk()
    My_GUI = GUI (root)
    set_defaults()
    root.mainloop()


if __name__ == '__main__':
    main_func()
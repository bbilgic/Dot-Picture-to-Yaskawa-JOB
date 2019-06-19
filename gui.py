#  -*- coding: cp1254 -*-
import tkinter.ttk as ttk

class GUI:
    def __init__(self, top=None):
        """__init__ [init function]:
        
        Keyword Arguments:
            top {[type]} -- [description] (default: {None})
        """
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.configure('Black.TLabelframe.Label',background=_bgcolor,foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("620x317+830+266")
        top.title("Picture to Job JR")
        top.configure(background="#757575")
        top.configure(height="8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.016, rely=0.032, relheight=0.363
                , relwidth=0.968)
        self.TLabelframe1.configure(relief='flat')
        self.TLabelframe1.configure(text='''Resim Seç''')
        self.TLabelframe1.configure(borderwidth="1")
        self.TLabelframe1.configure(width=600)
        self.TLabelframe1.configure(relief='flat')

        self.PicLabel = ttk.Entry(self.TLabelframe1)
        self.PicLabel.place(relx=0.025, rely=0.261, height=21, width=486
                , bordermode='ignore')
        self.PicLabel.configure(background="#fff")
        self.PicLabel.configure(foreground="#000")
        self.PicLabel.configure(font="TkDefaultFont")
        #self.PicLabel.configure(borderwidth="1")
        #self.PicLabel.configure(relief="groove")
        self.PicLabel.configure(width=486)

        self.SelectPic = ttk.Button(self.TLabelframe1)
        self.SelectPic.place(relx=0.858, rely=0.217, height=25, width=76
                , bordermode='ignore')
        self.SelectPic.configure(takefocus="")
        self.SelectPic.configure(text='''Seç''')
        self.SelectPic.configure(cursor="hand2")

        self.TLabel11 = ttk.Label(self.TLabelframe1)
        self.TLabel11.place(relx=0.033, rely=0.565, height=19, width=24
                , bordermode='ignore')
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font="TkDefaultFont")
        self.TLabel11.configure(relief="flat")
        self.TLabel11.configure(text='''En :''')

        self.TLabel12 = ttk.Label(self.TLabelframe1)
        self.TLabel12.place(relx=0.192, rely=0.565, height=19, width=30
                , bordermode='ignore')
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief="flat")
        self.TLabel12.configure(text='''Boy :''')

        self.Picwidth = ttk.Entry(self.TLabelframe1)
        self.Picwidth.place(relx=0.083, rely=0.565, relheight=0.165
                , relwidth=0.067, bordermode='ignore')
        self.Picwidth.configure(takefocus="")
        self.Picwidth.configure(cursor="ibeam")


        self.ThresholdL1 = ttk.Label(self.TLabelframe1)
        self.ThresholdL1.place(relx=0.35, rely=0.565, height=19, width=75
                , bordermode='ignore')
        self.ThresholdL1.configure(background="#d9d9d9")
        self.ThresholdL1.configure(foreground="#000000")
        self.ThresholdL1.configure(font="TkDefaultFont")
        self.ThresholdL1.configure(relief="flat")
        self.ThresholdL1.configure(text='''Renk Eşiği :''')

        self.Threshold = ttk.Entry(self.TLabelframe1)
        self.Threshold.place(relx=0.47, rely=0.565, relheight=0.165
                , relwidth=0.05, bordermode='ignore')
        self.Threshold.configure(takefocus="")
        self.Threshold.configure(cursor="ibeam")

        self.PicHeight = ttk.Entry(self.TLabelframe1)
        self.PicHeight.place(relx=0.25, rely=0.565, relheight=0.165
                , relwidth=0.067, bordermode='ignore')
        self.PicHeight.configure(takefocus="")
        self.PicHeight.configure(cursor="ibeam")

        self.TLabel13 = ttk.Label(self.TLabelframe1)
        self.TLabel13.place(relx=0.75, rely=0.0, height=18, width=152
                , bordermode='ignore')
        self.TLabel13.configure(background="#d9d9d9")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font="-family {Segoe UI} -size 7 -slant italic")
        self.TLabel13.configure(relief="flat")
        self.TLabel13.configure(text='''Coding by Murat Aydın and Berk Bilgiç''')
        self.TLabel13.configure(width=152)
		

        
        self.TLabelframe2 = ttk.Labelframe(top)
        self.TLabelframe2.place(relx=0.016, rely=0.426, relheight=0.454
                , relwidth=0.968)
        self.TLabelframe2.configure(relief='flat')
        self.TLabelframe2.configure(text='''Ayarlar''')
        self.TLabelframe2.configure(borderwidth="1")
        self.TLabelframe2.configure(width=600)

        self.TLabel2 = ttk.Label(self.TLabelframe2)
        self.TLabel2.place(relx=0.017, rely=0.208, height=19, width=54
                , bordermode='ignore')
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Job Adı :''')

        self.JobName = ttk.Entry(self.TLabelframe2)
        self.JobName.place(relx=0.1, rely=0.208, relheight=0.146, relwidth=0.168
                , bordermode='ignore')
        self.JobName.configure(width=96)
        self.JobName.configure(takefocus="")
        self.JobName.configure(cursor="ibeam")

        self.MaxRow = ttk.Entry(self.TLabelframe2)
        self.MaxRow.place(relx=0.483, rely=0.208, relheight=0.146, relwidth=0.093
                , bordermode='ignore')
        self.MaxRow.configure(takefocus="")
        self.MaxRow.configure(cursor="ibeam")


        self.TLabel3 = ttk.Label(self.TLabelframe2)
        self.TLabel3.place(relx=0.367, rely=0.208, height=19, width=66
                , bordermode='ignore')
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Max Satır :''')

        self.TLabel4 = ttk.Label(self.TLabelframe2)
        self.TLabel4.place(relx=0.25, rely=0.486, height=19, width=45
                , bordermode='ignore')
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(text='''Hız :''')

        self.Speed = ttk.Entry(self.TLabelframe2)
        self.Speed.place(relx=0.333, rely=0.486, relheight=0.146, relwidth=0.05
                , bordermode='ignore')
        self.Speed.configure(takefocus="")
        self.Speed.configure(cursor="ibeam")

        self.TLabel5 = ttk.Label(self.TLabelframe2)
        self.TLabel5.place(relx=0.883, rely=0.208, height=19, width=17
                , bordermode='ignore')
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(text='''Z :''')

        self.TLabel6 = ttk.Label(self.TLabelframe2)
        self.TLabel6.place(relx=0.608, rely=0.486, height=19, width=22
                , bordermode='ignore')
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(text='''Rx :''')

        self.TLabel7 = ttk.Label(self.TLabelframe2)
        self.TLabel7.place(relx=0.742, rely=0.486, height=19, width=23
                , bordermode='ignore')
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(text='''Ry :''')

        self.TLabel8 = ttk.Label(self.TLabelframe2)
        self.TLabel8.place(relx=0.875, rely=0.486, height=19, width=22
                , bordermode='ignore')
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font="TkDefaultFont")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(text='''Rz :''')

        self.ZBegin = ttk.Entry(self.TLabelframe2)
        self.ZBegin.place(relx=0.917, rely=0.208, relheight=0.146, relwidth=0.067
                , bordermode='ignore')
        self.ZBegin.configure(takefocus="")
        self.ZBegin.configure(cursor="ibeam")

        self.RyBegin = ttk.Entry(self.TLabelframe2)
        self.RyBegin.place(relx=0.783, rely=0.486, relheight=0.146
                , relwidth=0.067, bordermode='ignore')
        self.RyBegin.configure(takefocus="")
        self.RyBegin.configure(cursor="ibeam")

        self.RzBegin = ttk.Entry(self.TLabelframe2)
        self.RzBegin.place(relx=0.917, rely=0.486, relheight=0.146
                , relwidth=0.067, bordermode='ignore')
        self.RzBegin.configure(width=40)
        self.RzBegin.configure(takefocus="")
        self.RzBegin.configure(cursor="ibeam")

        self.RxBegin = ttk.Entry(self.TLabelframe2)
        self.RxBegin.place(relx=0.65, rely=0.486, relheight=0.146, relwidth=0.067
                , bordermode='ignore')
        self.RxBegin.configure(takefocus="")
        self.RxBegin.configure(cursor="ibeam")

        self.TLabel9 = ttk.Label(self.TLabelframe2)
        self.TLabel9.place(relx=0.017, rely=0.486, height=19, width=51
                , bordermode='ignore')
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="TkDefaultFont")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(text='''Call Job :''')

        self.CallJob = ttk.Entry(self.TLabelframe2)
        self.CallJob.place(relx=0.108, rely=0.486, relheight=0.146, relwidth=0.11
                , bordermode='ignore')
        self.CallJob.configure(takefocus="")
        self.CallJob.configure(cursor="ibeam")

        self.TLabel10 = ttk.Label(self.TLabelframe2)
        self.TLabel10.place(relx=0.417, rely=0.486, height=19, width=42
                , bordermode='ignore')
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font="TkDefaultFont")
        self.TLabel10.configure(relief="flat")
        self.TLabel10.configure(text='''Skala :''')

        self.Offset = ttk.Entry(self.TLabelframe2)
        self.Offset.place(relx=0.48, rely=0.486, relheight=0.146, relwidth=0.043
                , bordermode='ignore')
        self.Offset.configure(takefocus="")
        self.Offset.configure(cursor="ibeam")

        self.CreateJob = ttk.Button(self.TLabelframe2)
        self.CreateJob.place(relx=0.850, rely=0.694, height=29, width=81
                , bordermode='ignore')
        self.CreateJob.configure(takefocus="")
        self.CreateJob.configure(text='''Oluştur''')
        self.CreateJob.configure(cursor="hand2")

        self.Preview = ttk.Button(self.TLabelframe2)
        self.Preview.place(relx=0.700, rely=0.694, height=29, width=81
                , bordermode='ignore')
        self.Preview.configure(takefocus="")
        self.Preview.configure(text='''Preview''')
        self.Preview.configure(cursor="hand2")

        self.TLabel1 = ttk.Label(self.TLabelframe2)
        self.TLabel1.place(relx=0.617, rely=0.208, height=19, width=17
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''X :''')

        self.TLabel14 = ttk.Label(self.TLabelframe2)
        self.TLabel14.place(relx=0.75, rely=0.208, height=19, width=17
                , bordermode='ignore')
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font="TkDefaultFont")
        self.TLabel14.configure(relief="flat")
        self.TLabel14.configure(text='''Y :''')

        self.XBegin = ttk.Entry(self.TLabelframe2)
        self.XBegin.place(relx=0.65, rely=0.208, relheight=0.146, relwidth=0.067
                , bordermode='ignore')
        self.XBegin.configure(takefocus="")
        self.XBegin.configure(cursor="ibeam")

        self.YBegin = ttk.Entry(self.TLabelframe2)
        self.YBegin.place(relx=0.783, rely=0.208, relheight=0.146, relwidth=0.067
                , bordermode='ignore')
        self.YBegin.configure(takefocus="")
        self.YBegin.configure(cursor="ibeam")

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.016, rely=0.915, relwidth=0.968
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="600")

        self.ProgressLabel = ttk.Label(self.TLabelframe2)
        self.ProgressLabel.place(relx=0.01, rely=0.815, height=19, width=400, bordermode='ignore')
        self.ProgressLabel.configure(background="#d9d9d9")
        self.ProgressLabel.configure(foreground="#000000")
        self.ProgressLabel.configure(font="TkDefaultFont")
        self.ProgressLabel.configure(relief="flat")
        self.ProgressLabel.configure(text='''''')

        self.ProgressLabel2 = ttk.Label(self.TLabelframe2)
        self.ProgressLabel2.place(relx=0.01, rely=0.69, height=19, width=400, bordermode='ignore')
        self.ProgressLabel2.configure(background="#d9d9d9")
        self.ProgressLabel2.configure(foreground="#000000")
        self.ProgressLabel2.configure(font="TkDefaultFont")
        self.ProgressLabel2.configure(relief="flat")
        self.ProgressLabel2.configure(text='''''')


        self.DotsizeLabel = ttk.Label(self.TLabelframe2)
        self.DotsizeLabel.place(relx=0.59, rely=0.72, height=19, width=40, bordermode='ignore')
        self.DotsizeLabel.configure(background="#d9d9d9")
        self.DotsizeLabel.configure(foreground="#000000")
        self.DotsizeLabel.configure(font="TkDefaultFont")
        self.DotsizeLabel.configure(relief="flat")
        self.DotsizeLabel.configure(text='''Pixel : ''')

        self.DotSize = ttk.Entry(self.TLabelframe2)
        self.DotSize.place(relx=0.65, rely=0.72, relheight=0.146, relwidth=0.04
                , bordermode='ignore')
        self.DotSize.configure(takefocus="")
        self.DotSize.configure(cursor="ibeam")
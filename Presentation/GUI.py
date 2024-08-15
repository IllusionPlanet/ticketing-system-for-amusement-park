import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import Application.Application
from Application import *

global isLogined
isLogined = False
global currentPhoneNum
currentPhoneNum = ""

class BaseDesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('游乐园票务系统')
        self.root.geometry('1000x650+0+0')
        self.root.resizable(width=False,height=False)
        MainPage(self.root)

class MainPage():
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.MainPage = tk.Frame(self.master, bg='lightblue')
        self.MainPage.pack(fill=BOTH,expand=True)
        self.createscroll()
        if isLogined == True:
            text="已登录"
            Button(self.MainPage, text="已登录", width=15, height=1, bg='lightblue', font=('Arial', 15)).place(x=800,y=40)
        else:
            text="未登录"
            Button(self.MainPage, text="登录", width=15, height=1, bg='lightyellow',font=('Arial', 15),command=self.login).place(x=800,y=40)

        global images
        images = [
            ImageTk.PhotoImage(Image.open('../images/main7.jpg').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main6.jpg').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main5.jpg').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main1.jpeg').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main4.webp').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main3.jpeg').resize((1000, 400))),
            ImageTk.PhotoImage(Image.open('../images/main2.jpg').resize((1000, 400)))
        ]
        self.current = 0
        self.photo = tk.Label(self.MainPage, image=images[self.current])
        self.photo.place(x=0, y=90, width=1000, height=500)

        Label(self.MainPage, text=text, font=('Arial', 12)).place(x=720, y=50)
        Label(self.MainPage, text="游客须知：", font=('Arial', 12)).place(x=450, y=550)
        Label(self.MainPage, text="欢迎来到蔚蓝世界游乐园", bg="lightblue",
              font=('幼圆', 20)).place(x=40, y=40)
        Button(self.MainPage, text="立即订票",command=self.bookTicket, width=15, height=1,
               bg = 'lightblue',font=('Arial', 15)).place(x=10, y=550)
        Button(self.MainPage, text="游玩预览", width=15, height=1,
               bg = 'lightgreen',font=('Arial', 15), command=self.views,).place(x=800, y=550)
        Button(self.MainPage, text="个人中心", width=10, height=1,
               command=self.personalCenter, bg='white', font=('Arial', 10)).place(x=880, y=5)
        Button(self.MainPage, text="职员专用", width=10, height=1,
               command=self.adminEtrc, bg='white', font=('Arial', 10)).place(x=780, y=5)

        self.btn_prev = tk.Button(self.MainPage, text="<<<", bd=0, command=lambda: self.shift_image("prev"))
        self.btn_prev.place(relx=0, rely=0.4, relwidth=0.05, relheight=0.2)
        self.btn_next = tk.Button(self.MainPage, text=">>>", bd=0, command=lambda: self.shift_image("next"))
        self.btn_next.place(relx=0.95, rely=0.4, relwidth=0.05, relheight=0.2)

        self.display_image(self.current)

    def shift_image(self, direction: str) -> None:
        if direction == "prev":
            self.current -= 1
        if direction == "next":
            self.current += 1
        self.display_image(self.current)

    def display_image(self, index: int) -> None:
        self.photo['image'] = images[index]

        self.btn_prev['state'] = tk.DISABLED if index <= 0 else tk.NORMAL
        self.btn_next['state'] = tk.DISABLED if index >= len(images) - 1 else tk.NORMAL

    def login(self):
        self.MainPage.destroy()
        Login(self.master)

    def bookTicket(self):
        if isLogined == True:
            self.MainPage.destroy()
            #订票
            Book(self.master)
        else:
            tk.messagebox.showinfo('', "请先登录！")

    def personalCenter(self):
        if isLogined == True:
            self.MainPage.destroy()
            PersonCenter(self.master)
        else:
            tk.messagebox.showinfo('', "请先登录！")

    def views(self):
        self.MainPage.destroy()
        v(self.master)

    def createscroll(self):
        frame = tkinter.Frame(self.MainPage, bg="lightyellow", width=900, height=150)
            # 创建滚动条
        scroll = tkinter.Scrollbar(frame)
        text = tkinter.Text(frame, width=140, height=8)
        frame.pack(side='bottom')
            # side放到窗体的那一侧 fill填充
        scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        text.pack(side=tkinter.LEFT, fill=tkinter.Y)
            # 关联
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        str = '''尊敬的游客，欢迎光临蔚蓝世界游乐园，为确保园区正常的游玩秩序和游客的安全，请仔细阅读以下提示：

    *未成年人须有监护人带领游玩。

    *禁止携带管制刀具，易燃易爆、烟火爆竹等危险品进入园区。

    *衣冠不整者、携带宠物者、酗酒者请勿入园。

    *游玩过程中，请注意园区的安全警示标志，遵守游览秩序，请勿吸烟、乱刻乱画、攀爬、翻越、打闹、上下台阶请小心谨慎。

    *请保管好自己的随身物品，以防遗失。

    *请勿随地大小便、吐痰、乱扔果皮、纸屑等废弃物，保持园区清洁卫生。

    *请爱护花木及公共设施，如有损坏，须照价赔偿。

    *如需帮助，请拨打园区电话：19988126242。'''
        text.insert(tkinter.INSERT, str)
        text["state"] = DISABLED

    def adminEtrc(self):
        self.MainPage.destroy()
        staffLogin(self.master)

class WelcomePage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("1000x640")
        self.root.overrideredirect(True)
        self.welcome()
        self.temp()

    def welcome(self):
        canvas = tk.Canvas(self.root, width=1008, height=730, highlightthickness=0)
        self.im = Image.open('../images/welcome.jpeg').resize((1008, 730))
        self.img = ImageTk.PhotoImage(self.im)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        canvas.pack()

    def temp(self):
        self.root.after(1000, lambda: self.root.destroy())

class Login():
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.Login = tk.Frame(self.master)
        self.Login.pack(fill=BOTH,expand=True)

        self.var_phone = StringVar()
        self.var_password = StringVar()
        global img
        self.canvas = tk.Canvas(self.Login, width=1024, height=640, highlightthickness=0)
        im = Image.open('../images/login.jpg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()

        Label(self.Login, text="手机号", font=("微软雅黑", 20)).place(x=200, y=150)
        Entry(self.Login, textvariable=self.var_phone,bd=2, width=30, font=("宋体", 17)).place(x=400, y=160)
        Label(self.Login, text="密码", font=("微软雅黑", 20)).place(x=200, y=250)
        Entry(self.Login, textvariable=self.var_password,bd=2, width=30, font=("宋体", 17),show="*").place(x=400, y=260)
        Button(self.Login, text="登 录",width=15, height=1, command=self.login_submit ,font=("微软雅黑", 20),
               bg="lightblue").place(x=200, y=350)
        Button(self.Login, text="返回", width=10, height=1,command=self.back, font=("微软雅黑", 10),
               bg="gold").place(x=20, y=20)
        Button(self.Login, text="注 册",width=15, height=1, command=self.register, font=("微软雅黑", 20),
               bg="lightblue").place(x=550, y=350)

    def login_submit(self):
        if self.var_phone.get() == "" or self.var_password.get() == "":
            tk.messagebox.showinfo(" ", "手机号或密码不能为空！")
        else:
            if Application.a_login_submit(self.var_phone.get(),
                                                      self.var_password.get()) == 0:
                tk.messagebox.showinfo(" ", "手机号或密码存在错误！")
            else:
                tk.messagebox.showinfo(" ", "登录成功！")
                global isLogined
                isLogined = True
                global currentPhoneNum
                currentPhoneNum = self.var_phone.get()
                self.Login.destroy()
                MainPage(self.master)

    def register(self):
        self.Login.destroy()
        Register(self.master)

    def back(self):
        self.Login.destroy()
        MainPage(self.master)

class Register():
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.Register = tk.Frame(self.master)
        self.Register.pack(fill=BOTH, expand=True)
        global img
        self.canvas = tk.Canvas(self.Register, width=1024, height=640, highlightthickness=0)
        im = Image.open('../images/login.jpg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()
        self.nickName = StringVar()
        self.phoneNum = StringVar()
        self.password = StringVar()
        self.password_confirm = StringVar()
        Label(self.Register, text="昵称", font=("微软雅黑",17), anchor='e').place(x=200, y=100)
        Entry(self.Register, bd=2, width=30, font=("宋体", 17),
              textvariable= self.nickName).place(x=350, y=100)
        Label(self.Register, text="手机号", font=("微软雅黑",17), anchor='e').place(x=200, y=200)
        Entry(self.Register, bd=2, width=30, font=("宋体", 17),
              textvariable= self.phoneNum).place(x=350, y=200)
        Label(self.Register, text="密码", font=("微软雅黑", 17), anchor='e').place(x=200, y=300)
        Entry(self.Register, bd=2, width=30, font=("宋体", 17),
              textvariable= self.password).place(x=350, y=300)
        Label(self.Register, text="确认密码", font=("微软雅黑", 17), anchor='e').place(x=200, y=400)
        Entry(self.Register, bd=2, width=30, font=("宋体", 17),
              textvariable= self.password_confirm).place(x=350, y=400)
        Button(self.Register, text="注 册", width=10, height=1, font=("微软雅黑", 20),
               bg="lightblue", command=self.registerConfirm).place(x=400, y=500)
        Button(self.Register, text="返回", width=10, height=1, command=self.back, font=("微软雅黑", 10),
               bg="gold").place(x=20,y=20)

    def registerConfirm(self):
        if self.nickName.get() == "" or self.phoneNum.get() == "" or self.password.get() == "" or \
                self.password_confirm.get() == "":
            tk.messagebox.showinfo(" ", "请完整填写信息！")
        elif self.password.get() != self.password_confirm.get():
            tk.messagebox.showinfo(" ", "密码不一致！")
        else:
            Application.registNew(self.phoneNum.get(), self.nickName.get(), self.password.get())
            tk.messagebox.showinfo(" ", "注册成功！")
            self.Register.destroy()
            MainPage(self.master)

    def back(self):
        self.Register.destroy()
        Login(self.master)

class PersonCenter():
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.PersonCenter = tk.Frame(self.master)
        self.PersonCenter.pack(fill=BOTH, expand=True)
        global img
        self.canvas = tk.Canvas(self.PersonCenter, width=1024, height=640, highlightthickness=0)
        im = Image.open('../images/login.jpg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()

        myphone,myname,mymoney = Application.displayPersonCenter(currentPhoneNum)

        Label(self.PersonCenter, text="您的昵称：", height=1, width=10,
              font=("微软雅黑", 20), anchor='w').place(x=200, y=70)
        Label(self.PersonCenter, text="您的手机号：", height=1, width=10,
              font=("微软雅黑", 20),anchor='w').place(x=200, y=130)
        Label(self.PersonCenter, text="您的余额：", height=1, width=10,
              font=("微软雅黑", 20), anchor='w').place(x=200, y=190)
        Button(self.PersonCenter, text="充值", height=1, width=8,bg='lightyellow',
               command=self.enterRecharge, font=("微软雅黑", 20)).place(x=500, y=250)
        Button(self.PersonCenter, text="订票记录", height=1, width=10,command=self.enterRecords,
              font=("微软雅黑", 20),bg='lightblue').place(x=200, y=250)
        Button(self.PersonCenter, text="退出登录", width=10, height=1, font=("微软雅黑", 15),
               bg="lightblue", command=self.quitLogin).place(x=400, y=500)
        Button(self.PersonCenter, text="返回", width=10, height=1, command=self.back,
               font=("微软雅黑", 10),bg="gold").place(x=20, y=20)
        Label(self.PersonCenter, text=myname, height=1, width=20,
              font=("微软雅黑", 20)).place(x=400, y=70)
        Label(self.PersonCenter, text=myphone, height=1, width=20,
               font=("微软雅黑", 20)).place(x=400, y=130)
        Label(self.PersonCenter, text=mymoney, height=1, width=20,
              font=("微软雅黑", 20)).place(x=400, y=190)

    def quitLogin(self):
        #退出登录
        global isLogined
        isLogined = False
        self.PersonCenter.destroy()
        MainPage(self.master)

    def back(self):
        self.PersonCenter.destroy()
        MainPage(self.master)

    def enterRecharge(self):
        self.PersonCenter.destroy()
        Recharge(self.master)

    def enterRecords(self):
        self.PersonCenter.destroy()
        Records(self.master)

class Recharge():
    def __init__(self,master):
        self.master = master
        self.master.config()
        self.Recharge = tk.Frame(self.master)
        self.Recharge.pack(fill=BOTH, expand=True)
        global img
        self.canvas = tk.Canvas(self.Recharge, width=1024, height=640, highlightthickness=0)
        im = Image.open('../images/login.jpg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()

        self.var_addmoney = StringVar()
        Label(self.Recharge, text="请输入你要充值的金额:", height=1, width=20,
              font=("微软雅黑", 20)).place(x=150, y=130)
        Entry(self.Recharge, textvariable=self.var_addmoney,bd=2, width=10,
                  font=("宋体", 17)).place(x=500, y=140)
        Button(self.Recharge, text="返回", width=10, height=1, command=self.back,
               font=("微软雅黑", 10), bg="gold").place(x=20, y=20)
        Button(self.Recharge, text="确定充值", width=15, height=1, command=self.confirmRecharge,
               font=("微软雅黑", 20), bg="lightblue").place(x=300, y=400)

    def back(self):
        self.Recharge.destroy()
        PersonCenter(self.master)

    def confirmRecharge(self):
        num = self.var_addmoney.get()
        Application.addMoney(currentPhoneNum,num)
        tk.messagebox.showinfo('', "充值成功！")
        self.var_addmoney.set("")

class v():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.personview = tk.Frame(self.master)
        self.personview.pack(fill=BOTH, expand=True)

        global img, img1, img2, img3, img4, img5,img6,img7,img8,img9,img10,img11,img12,img13,img14
        self.canvas = tk.Canvas(self.personview, width=1024, height=713, highlightthickness=0)
        im = Image.open('../images/map.jpeg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()


        self.btn = tk.Button(self.personview, text="退出", bd=0, bg="light blue", command=self.re)
        self.btn.place(relx=0.9, rely=0.95, relwidth=0.1, relheight=0.05)

        self.btn1 = tk.Button(self.personview, text="特色活动", bd=0, bg="light blue", command=self.create)
        self.btn1.place(relx=0.8, rely=0.95, relwidth=0.1, relheight=0.05)

        im1 = Image.open('../images/1.jpg')
        img1 = ImageTk.PhotoImage(im1)
        self.v1 = tk.Label(self.personview, image=img1)
        self.v1.place(x=40, y=25, width=76, height=80)
        self.v1.bind("<Enter>", self.create1)

        im2 = Image.open('../images/2.jpg')
        img2 = ImageTk.PhotoImage(im2)
        self.v2 = tk.Label(self.personview, image=img2)
        self.v2.place(x=475, y=0, width=65, height=58)
        self.v2.bind("<Enter>", self.create2)

        im3 = Image.open('../images/3.jpg')
        img3 = ImageTk.PhotoImage(im3)
        self.v3 = tk.Label(self.personview, image=img3)
        self.v3.place(x=880, y=35, width=100, height=110)
        self.v3.bind("<Enter>", self.create3)

        im4 = Image.open('../images/4.jpg')
        img4 = ImageTk.PhotoImage(im4)
        self.v4 = tk.Label(self.personview, image=img4)
        self.v4.place(x=483, y=576, width=78, height=72)
        self.v4.bind("<Enter>", self.create4)

        im5 = Image.open('../images/5.jpg')
        img5 = ImageTk.PhotoImage(im5)
        print(img5.width(), img5.height())
        self.v5 = tk.Label(self.personview, image=img5)
        self.v5.place(x=465, y=265, width=96, height=96)
        self.v5.bind("<Enter>", self.create5)

        im6 = Image.open('../images/6.jpg')
        img6 = ImageTk.PhotoImage(im6)
        self.v6 = tk.Label(self.personview, image=img6)
        self.v6.place(x=270, y=100, width=109, height=111)
        self.v6.bind("<Enter>", self.create6)

        im7 = Image.open('../images/7.jpg')
        img7 = ImageTk.PhotoImage(im7)
        self.v7 = tk.Label(self.personview, image=img7)
        self.v7.place(x=871, y=225, width=149, height=138)
        self.v7.bind("<Enter>", self.create7)

        im8 = Image.open('../images/8.jpg')
        img8 = ImageTk.PhotoImage(im8)
        self.v8 = tk.Label(self.personview, image=img8)
        self.v8.place(x=6, y=375, width=185, height=147)
        self.v8.bind("<Enter>", self.create8)

        im9 = Image.open('../images/9.jpg')
        img9 = ImageTk.PhotoImage(im9)
        self.v9 = tk.Label(self.personview, image=img9)
        self.v9.place(x=280, y=335, width=126, height=121)
        self.v9.bind("<Enter>", self.create9)

        im10 = Image.open('../images/10.jpg')
        img10 = ImageTk.PhotoImage(im10)
        self.v10 = tk.Label(self.personview, image=img10)
        self.v10.place(x=160, y=548, width=216, height=75)
        self.v10.bind("<Enter>", self.create10)

        im11 = Image.open('../images/11.jpg')
        img11 = ImageTk.PhotoImage(im11)
        print(img11.width(), img11.height())
        self.v11 = tk.Label(self.personview, image=img11)
        self.v11.place(x=655, y=575, width=133, height=100)
        self.v11.bind("<Enter>", self.create11)

        im12 = Image.open('../images/12.jpg')
        img12 = ImageTk.PhotoImage(im12)
        print(img12.width(), img12.height())
        self.v12 = tk.Label(self.personview, image=img12)
        self.v12.place(x=620, y=148, width=130, height=88)
        self.v12.bind("<Enter>", self.create12)

        im13 = Image.open('../images/13.jpg')
        img13 = ImageTk.PhotoImage(im13)
        print(img13.width(), img13.height())
        self.v13 = tk.Label(self.personview, image=img13)
        self.v13.place(x=85, y=253, width=108, height=83)
        self.v13.bind("<Enter>", self.create13)

        im14 = Image.open('../images/14.jpg')
        img14 = ImageTk.PhotoImage(im14)
        print(img14.width(), img14.height())
        self.v14 = tk.Label(self.personview, image=img14)
        self.v14.place(x=159, y=165, width=82, height=83)
        self.v14.bind("<Enter>", self.create14)

    def create(self):
        top0 = tk.Toplevel()
        top0.overrideredirect(True)
        top0.geometry("400x400+400+275")

        btn1 = Button(top0, text='<', command=lambda: top0.destroy())
        btn1.place(relx=0, rely=0, relwidth=0.08, relheight=0.05)

        msg = tk.Message(top0, text='特色活动', width=200)
        msg = tk.Message(top0, text='【EnTrance微型电子音乐节】\n让你跟随音乐的律动，把这篇游乐之地的经历'
                                    '变成你最疯狂难忘的回忆之一。\n时间：7月22日~7月26日19:00，播放键按下。\n\n'
                                    '【荷尔蒙随机舞】\n这将是使人的荷尔蒙飞溅的舞蹈，并且随机重点围绕一些观众煽动他们'
                                    '参与其中。\n时间：7月23日~7月29日，14:00~20:00随机进行。\n\n'
                                    '【Lavlish美食分享嘉年华】\n披萨、沙拉、冰淇淋……各色花样将被用来装点你的游乐之旅！'
                                    '而且最重要的是……它们免费！\n时间：7月的每晚19:00~20:00。'
                                    '',font=("微软雅黑", 10), width=200)
        msg.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

    def create1(self, event):
        global top, ph1
        top = tk.Toplevel()
        top.overrideredirect(True)
        top.geometry("400x400+116+105")

        msg = tk.Message(top, text='海滨别墅', width=200)
        msg.pack()
        ph = Image.open('../images/001.jpg').resize((400, 400))
        ph1 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top, image=ph1)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v1.bind("<Leave>", self.dis1)
        msg1 = tk.Message(top, text='坐落于粼粼波澜旁的歇脚之地，除了休息外，还能在这里购买到纪念品'
                                    '和冰凉解渴的冷饮。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis1(self, event):
        global top
        top.destroy()

    def create2(self, event):
        global top1, ph2
        top1 = tk.Toplevel()
        top1.overrideredirect(True)
        top1.geometry("400x400+540+58")

        msg = tk.Message(top1, text='树妖神殿', width=200)
        msg.pack()
        ph = Image.open('../images/002.jpg').resize((400, 400))
        ph2 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top1, image=ph2)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v2.bind("<Leave>", self.dis2)
        msg1 = tk.Message(top1, text='暗绿色的氛围衬托着这里的险恶，当心随时出现的树妖用藤条在你的背后'
                                     '扫过，堪比鬼屋的体验！', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis2(self, event):
        global top1
        top1.destroy()

    def create3(self, event):
        global top3, ph3
        top3 = tk.Toplevel()
        top3.overrideredirect(True)
        top3.geometry("400x400+520+98")

        msg = tk.Message(top3, text='国风·迷藏追逐', width=200)
        msg.pack()
        ph = Image.open('../images/003.jpg').resize((400, 400))
        ph3 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top3, image=ph3)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v3.bind("<Leave>", self.dis3)
        msg1 = tk.Message(top3, text='在拥有浓郁国风的楼台和亭子间参与捉迷藏与追逐游戏，不要小看工作人员，'
                                     '尽管他们可能没有你快，但他们可是对这里非常熟悉。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis3(self, event):
        global top3
        top3.destroy()

    def create4(self, event):
        global top4, ph4
        top4 = tk.Toplevel()
        top4.overrideredirect(True)
        top4.geometry("400x400+561+330")

        msg = tk.Message(top4, text='入 口', width=200)
        msg.pack()
        ph = Image.open('../images/004.jpg').resize((400, 400))
        ph4 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top4, image=ph4)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v4.bind("<Leave>", self.dis4)
        msg1 = tk.Message(top4, text='蔚蓝世界的入口！确保你穿着舒适宽松，以及带上一颗爱玩的心！', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis4(self, event):
        global top4
        top4.destroy()

    def create5(self, event):
        global top5, ph5
        top5 = tk.Toplevel()
        top5.overrideredirect(True)
        top5.geometry("400x400+561+330")

        msg = tk.Message(top5, text='洞穴激光大战', width=200)
        msg.pack()
        ph = Image.open('../images/005.jpg').resize((400, 400))
        ph5 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top5, image=ph5)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v5.bind("<Leave>", self.dis5)
        msg1 = tk.Message(top5, text='黯黑的氛围，光滑的水流声，时不时掠过耳边的回声……当心，这些绝不是'
                                     '安宁的征兆！你将与他人组队，随时留意敌队射来的激光，当然，你也可以用手中的'
                                     '激光发射器反击他们。\n本项目讲究战术和策略，最好确保你胸有成竹！', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis5(self, event):
        global top5
        top5.destroy()

    def create6(self, event):
        global top6, ph6
        top6 = tk.Toplevel()
        top6.overrideredirect(True)
        top6.geometry("400x400+379+105")

        msg = tk.Message(top6, text='矿井过山车', width=200)
        msg.pack()
        ph = Image.open('../images/006.jpg').resize((400, 400))
        ph6 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top6, image=ph6)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v6.bind("<Leave>", self.dis6)
        msg1 = tk.Message(top6, text='经典的过山车项目绝不会在这里不见踪影，它的最佳效果就是让你的'
                                     '心脏跳出身体！', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis6(self, event):
        global top6
        top6.destroy()

    def create7(self, event):
        global top7, ph7
        top7 = tk.Toplevel()
        top7.overrideredirect(True)
        top7.geometry("400x400+471+300")

        msg = tk.Message(top7, text='TOTORO翠绿攀爬场', width=200)
        msg.pack()
        ph = Image.open('../images/007.jpg').resize((400, 400))
        ph7 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top7, image=ph7)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v7.bind("<Leave>", self.dis7)
        msg1 = tk.Message(top7, text='攀岩、平衡桥、蹦床、攀爬杆……这里是尽情散发原始特性的场地！\n'
                                     '在撒欢前，确保安全措施没出问题。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis7(self, event):
        global top7
        top7.destroy()

    def create8(self, event):
        global top8, ph8
        top8 = tk.Toplevel()
        top8.overrideredirect(True)
        top8.geometry("400x400+191+200")

        msg = tk.Message(top8, text='激流勇进', width=200)
        msg.pack()
        ph = Image.open('../images/008.jpg').resize((400, 400))
        ph8 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top8, image=ph8)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v8.bind("<Leave>", self.dis8)
        msg1 = tk.Message(top8, text='经典水上项目！如果你不想在水花中穿梭并淋湿汗衫的话，别玩这个。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis8(self, event):
        global top8
        top8.destroy()

    def create9(self, event):
        global top9, ph9
        top9 = tk.Toplevel()
        top9.overrideredirect(True)
        top9.geometry("400x400+406+300")

        msg = tk.Message(top9, text='河道漫游', width=200)
        msg.pack()
        ph = Image.open('../images/009.jpg').resize((400, 400))
        ph9 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top9, image=ph9)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v9.bind("<Leave>", self.dis9)
        msg1 = tk.Message(top9, text='如果过于激情的项目不适合你，那乘坐小船一边漫游一边欣赏风光也许'
                                     '值得你的尝试！', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis9(self, event):
        global top9
        top9.destroy()

    def create10(self, event):
        global top10, ph10
        top10 = tk.Toplevel()
        top10.overrideredirect(True)
        top10.geometry("400x400+376+335")

        msg = tk.Message(top10, text='飞行器博物馆', width=200)
        msg.pack()
        ph = Image.open('../images/010.jpg').resize((400, 400))
        ph10 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top10, image=ph10)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v10.bind("<Leave>", self.dis10)
        msg1 = tk.Message(top10, text='飞行器爱好者不可错过的地点！这里有个秘密：'
                                      '我们甚至有一架水上飞机。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis10(self, event):
        global top10
        top10.destroy()

    def create11(self, event):
        global top11, ph11
        top11 = tk.Toplevel()
        top11.overrideredirect(True)
        top11.geometry("400x400+265+335")

        msg = tk.Message(top11, text='冰激淋战士', width=200)
        msg.pack()
        ph = Image.open('../images/011.jpg').resize((400, 400))
        ph11 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top11, image=ph11)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v11.bind("<Leave>", self.dis11)
        msg1 = tk.Message(top11, text='冰凉又美味的冰激凌从这里购买，让你获得一路的享受。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis11(self, event):
        global top11
        top11.destroy()

    def create12(self, event):
        global top12, ph12
        top12 = tk.Toplevel()
        top12.overrideredirect(True)
        top12.geometry("400x400+230+148")

        msg = tk.Message(top12, text='猎人之家', width=200)
        msg.pack()
        ph = Image.open('../images/012.jpg').resize((400, 400))
        ph12 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top12, image=ph12)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v12.bind("<Leave>", self.dis12)
        msg1 = tk.Message(top12, text='这里是属于隐居的猎人的地带，你能够获得猎枪的射击体验。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis12(self, event):
        global top12
        top12.destroy()

    def create13(self, event):
        global top13, ph13
        top13 = tk.Toplevel()
        top13.overrideredirect(True)
        top13.geometry("400x400+193+253")

        msg = tk.Message(top13, text='龙之摆荡', width=200)
        msg.pack()
        ph = Image.open('../images/013.jpg').resize((400, 400))
        ph13 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top13, image=ph13)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v13.bind("<Leave>", self.dis13)
        msg1 = tk.Message(top13, text='感受龙的身姿！因剧烈摇摆产生的晕眩是难以避免的，'
                                      '但更多的是欢乐。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis13(self, event):
        global top13
        top13.destroy()

    def create14(self, event):
        global top14, ph14
        top14 = tk.Toplevel()
        top14.overrideredirect(True)
        top14.geometry("400x400+241+165")

        msg = tk.Message(top14, text='3D游戏体验屋', width=200)
        msg.pack()
        ph = Image.open('../images/014.webp').resize((400, 400))
        ph14 = ImageTk.PhotoImage(ph)
        la1 = tk.Label(top14, image=ph14)
        la1.place(relx=0, rely=0.07, relwidth=1, relheight=0.6)
        self.v14.bind("<Leave>", self.dis14)
        msg1 = tk.Message(top14, text='用第一人称，带你身临其境，穿越森林，去会面精灵；穿过天空，去触摸彩虹；'
                                      '或者去到另一颗星，看会有什么东西在你面前降临。', width=200)
        msg1.place(relx=0, rely=0.67, relwidth=1, relheight=0.34)

    def dis14(self, event):
        global top14
        top14.destroy()

    def re(self):
        self.personview.destroy()
        MainPage(self.master)

class Book():
    def __init__(self, master=None):
        self.master = master
        self.master.config()
        self.master["bg"] = "lightgreen"

        self.Book = Frame(self.master, bg="lightgreen")
        self.Book.pack(fill=BOTH, expand=True)

        Label(self.Book, text="双击购买", bg="lightgreen").grid(row=0, column=0)
        Button(self.Book, text="返回", command=self.back, width=5, height=1, font=("宋体",10),
               bg="gold").place(x=0, y=0)

        self.tree = ttk.Treeview(self.Book, show="headings")  # #创建表格对象
        self.tree["columns"] = ("类型", "价格", "时间", "剩余数量")  # #定义列
        self.tree.column("类型", width=245, anchor="center")  # #设置列
        self.tree.column("价格", width=245, anchor="center")
        self.tree.column("时间", width=245, anchor="center")
        self.tree.column("剩余数量", width=245, anchor="center")
        self.tree.heading("类型", text="类型")  # #设置显示的表头名
        self.tree.heading("价格", text="价格")
        self.tree.heading("时间", text="时间")
        self.tree.heading("剩余数量", text="剩余数量")

        i = 0
        r = Application.getTicket()
        for result in r:
            self.tree.insert("", i, text=str(i + 1), values=(result[0], result[1], result[2],
                                                             result[3]))
            i += 1

        self.tree.bind("<Double-1>",self.treeviewClick)

        vbar = Scrollbar(self.Book, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        self.tree.grid(row=1, column=0, sticky=NSEW)
        vbar.grid(row=1, column=1, sticky=NS)
        self.Book.place(x=0, y=50)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            Buy(item_text[0], item_text[1], item_text[2], item_text[3], self.master)
            self.Book.destroy()

    def back(self):
        MainPage(self.master)
        self.Book.destroy()

class Buy():
    def __init__(self, type, price, time, num, master=None):
        self.master = master
        self.master.config()
        self.master["bg"] = "lightgreen"

        self.time = time
        self.type = type
        self.price = price
        self.num = num

        print(time, type, num, price)

        self.Buy = Frame(self.master, bg="lightgreen")
        self.Buy.pack(fill=BOTH, expand=True)

        text = "已选择 " + time + "  " + type + " 选择数量："

        Label(self.Buy, text=text, bg="lightgreen", font=("宋体", 15)).place(x=100, y=200)

        myvalue = []
        for i in range(int(num)-1):
            myvalue.append(str(i+1))
        myvalue.append(num)

        self.com = ttk.Combobox(self.Buy, width=10, values=myvalue)
        self.com.current(0)
        self.com.bind("<<ComboboxSelected>>", self.update)
        self.com.place(x=500, y=200)

        self.sumprice = StringVar()
        self.sumprice.set(self.getprice())

        Button(self.Buy, text="确定", command=self.ok, width=10, height=2,
               font=("宋体",13)).place(x=500, y=300)
        Button(self.Buy, text="返回", command=self.back, width=5, height=1,
               font=("宋体",10), bg="gold").place(x=10, y=10)
        Label(self.Buy, textvariable=self.sumprice, bg="lightgreen",
              font=("宋体", 15)).place(x=700, y=200)

    def getprice(self):
        price = "共需 "
        price += str(int(self.com.get())*float(self.price))
        price += " 元"
        return price

    def update(self, *args):
        price = self.getprice()
        self.sumprice.set(price)

    def ok(self):
        ConfirmBuy(self.time, self.type, self.price,
                   self.num, int(self.com.get())*float(self.price),self.master)
        self.Buy.destroy()

    def back(self):
        Book(self.master)
        self.Buy.destroy()

class ConfirmBuy():
    def __init__(self, time, type, price, num, need, master=None):
        self.master = master
        self.master.config()
        self.master["bg"] = "lightgreen"

        self.time = time
        self.type = type
        self.price = price
        self.num = num
        self.need = need

        self.ConfirmBuy = Frame(self.master, bg="lightgreen")
        self.ConfirmBuy.pack(fill=BOTH, expand=True)

        data = "购买 "
        data += str(int(need/float(price)))
        data += " 张 "
        data += time
        data += " 的 "
        data += type

        r = Application.getBalance(currentPhoneNum)

        self.money = ""
        for result in r:
            self.money += str(result[0])

        havetext = "账户余额 "
        havetext += self.money
        havetext += " 元"

        needtext = "本次购票需 "
        needtext += str(need)
        needtext += " 元"

        lefttext = "购票后剩余 "
        lefttext += str(float(self.money) - need)
        lefttext +=" 元"

        Label(self.ConfirmBuy, text=data, bg="lightgreen", font=("黑体", 20)).place(x=200, y=150)
        Label(self.ConfirmBuy, text=havetext, bg="lightgreen", font=("黑体", 20)).place(x=200, y=200)
        Label(self.ConfirmBuy, text=needtext, bg="lightgreen", font=("黑体", 20)).place(x=200, y=250)
        Label(self.ConfirmBuy, text=lefttext, bg="lightgreen", font=("黑体", 20)).place(x=200, y=300)

        Button(self.ConfirmBuy, text="返回", command=self.back, width=5, height=1,
               font=("宋体", 10), bg="gold").place(x=10, y=10)
        Button(self.ConfirmBuy, text="确定", command=self.ok, width=10, height=2,
               font=("宋体", 13)).place(x=600, y=500)

    def back(self):
        Buy(self.type, self.price,self.time, self.num, self.master)
        self.ConfirmBuy.destroy()
    def ok(self):
        text = ""
        if float(self.money) < self.need:
            text = "账号余额不足"
            messagebox.showinfo("购票结果", text)
            Buy(self.type, self.price, self.time, self.num, self.master)
            self.ConfirmBuy.destroy()
        else:
            text = "购票成功\n"
            text += "余额： "
            text += str(float(self.money) - self.need)
            text += " 元"
            messagebox.showinfo("购票结果", text)
            Application.ticketbooking(currentPhoneNum, self.money, self.time, self.type, self.price, self.num, self.need)

            Book(self.master)
            self.ConfirmBuy.destroy()

class Records():
    def __init__(self, master=None):
        self.master = master
        self.master.config()
        self.master["bg"] = "lightgreen"

        self.Records = Frame(self.master, bg="lightgreen")
        self.Records.pack(fill=BOTH, expand=True)

        Label(self.Records, text="我的订单（双击退票）", font=("微软雅黑", 15),
              bg="lightgreen").grid(row=0, column=0)
        Button(self.Records, text="返回", width=10, height=1, command=self.back,
               font=("微软雅黑", 10), bg="gold").place(x=20, y=5)
        self.tree = ttk.Treeview(self.Records, show="headings")  # #创建表格对象
        self.tree["columns"] = ("订单编号", "到达日期", "类型", "数量", "状态")  # #定义列
        self.tree.column("订单编号", width=195, anchor="center")
        self.tree.column("到达日期", width=195, anchor="center")
        self.tree.column("类型", width=195, anchor="center")
        self.tree.column("数量", width=195, anchor="center")
        self.tree.column("状态", width=195, anchor="center")
        self.tree.heading("订单编号", text="订单编号")
        self.tree.heading("到达日期", text="到达日期")
        self.tree.heading("类型", text="类型")
        self.tree.heading("数量", text="数量")
        self.tree.heading("状态", text="状态")

        cursor = Application.userbooking(currentPhoneNum)
        i = 0
        for result in cursor:
            self.tree.insert("", i, text=str(i), values=(str(result[0]), str(result[3]), str(result[2]), str(result[4]), str(result[7])))

        self.tree.bind("<Double-1>",self.treeviewClick)

        vbar = Scrollbar(self.Records, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        self.tree.grid(row=1, column=0, sticky=NSEW)
        vbar.grid(row=1, column=1, sticky=NS)
        self.Records.place(x=0, y=50)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            if item_text[4]=="未检票":
                text = "确定要退订 "
                text += item_text[3]
                text += " 张 "
                text += item_text[1]
                text += "  的 "
                text += item_text[2]
                text += " 吗？"
                answer = messagebox.askquestion(title="确认退票", message=text)
                if answer == "yes":
                    Application.reback(item_text, currentPhoneNum)
                    messagebox.showinfo(title="退票成功", message="退票成功")
                    self.Records.destroy()
                    Records(self.master)
            else:
                messagebox.showinfo(title="该票已检票", message="该票已检票")

    def back(self):
        self.Records.destroy()
        PersonCenter(self.master)

class staffLogin():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.staffLogin = tk.Frame(self.master)
        self.staffLogin.pack(fill=BOTH, expand=True)
        global img
        self.canvas = tk.Canvas(self.staffLogin, width=1024, height=640, highlightthickness=0)
        im = Image.open('../images/login.jpg')
        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.pack()
        Button(self.staffLogin, text="返回", width=10, height=1, command=self.back, font=("微软雅黑", 10),
               bg="gold").place(x=20, y=20)
        self.var_accName = StringVar()
        self.var_password = StringVar()
        Label(self.staffLogin, text="职员账号", font=(
            "微软雅黑", 20)).place(x=200, y=150)
        Entry(self.staffLogin, textvariable=self.var_accName, bd=2,
              width=30, font=("宋体", 17)).place(x=400, y=160)
        Label(self.staffLogin, text="职员密码", font=(
            "微软雅黑", 20)).place(x=200, y=250)
        Entry(self.staffLogin, textvariable=self.var_password, bd=2,
              width=30, font=("宋体", 17), show="*").place(x=400, y=260)
        Button(self.staffLogin, text="登 录", width=15, height=1, command=self.login_submit, font=("微软雅黑", 20),
               bg="lightblue").place(x=350, y=350)

    def login_submit(self):
        if self.var_accName.get() == "" or self.var_password.get() == "":
            tk.messagebox.showinfo('', "职员账号或密码不能为空！")
        else:
            if Application.staffLoginSubmit(self.var_accName.get(), self.var_password.get()) == 0:
                tk.messagebox.showinfo('', "职员账号或密码错误！")
            else:
                tk.messagebox.showinfo('', "职员登录成功！")
                self.staffLogin.destroy()
                mngmt(self.master)

    def back(self):
        self.staffLogin.destroy()
        MainPage(self.master)


class mngmt():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.master["bg"] = "lightgreen"
        self.mngmt = Frame(self.master, bg="lightgreen")
        self.mngmt.pack(fill=BOTH, expand=True)
        self.phoneNum = StringVar()
        Label(self.mngmt, text="手机号：", bg="lightgreen", font=("微软雅黑", 15)).place(x=200, y=150)
        Entry(self.mngmt, textvariable=self.phoneNum, bd=2, width=30,
              font=("宋体", 17)).place(x=500, y=150)
        Button(self.mngmt, text="搜索", width=10, height=1, command=self.search,
               font=("微软雅黑", 10), bg="lightblue").place(x=450, y=220)

        Label(self.mngmt, text="双击检票", bg="lightgreen", font=("微软雅黑",17)).place(x=450, y=50)

        Button(self.mngmt, text="返回", width=10, height=1, command=self.back,
               font=("微软雅黑", 10), bg="gold").place(x=20, y=15)
        self.tree = ttk.Treeview(self.mngmt, show="headings")  # #创建表格对象
        self.tree["columns"] = ("序号", "手机号", "类型", "有效日期", "数量", "总价", "订票日期", "状态") #定义列
        self.tree.column("序号", width=50, anchor="center")
        self.tree.column("手机号", width=150, anchor="center")  # #设置列
        self.tree.column("类型", width=150, anchor="center")
        self.tree.column("有效日期", width=150, anchor="center")
        self.tree.column("数量", width=50, anchor="center")
        self.tree.column("总价", width=150, anchor="center")
        self.tree.column("订票日期", width=150, anchor="center")
        self.tree.column("状态", width=150, anchor="center")
        self.tree.heading("序号", text="序号")
        self.tree.heading("手机号", text="手机号")  # #设置显示的表头名
        self.tree.heading("类型", text="类型")
        self.tree.heading("有效日期", text="有效日期")
        self.tree.heading("数量", text="数量")
        self.tree.heading("总价", text="总价")
        self.tree.heading("订票日期", text="订票日期")
        self.tree.heading("状态", text="状态")
        self.tree.bind("<Double-1>", self.treeviewClick)
        vbar = Scrollbar(self.mngmt, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        self.tree.place(x=0,y=300)
        vbar.grid(row=1, column=1, sticky=NS)
        #self.mngmt.place(x=0, y=50)

    def treeviewClick(self,j):
        item = self.tree.selection()
        slct = self.tree.item(item, "values")
        Application.checkTicket(slct)
        messagebox.showinfo("", '检票完成！')

    def search(self):
        x = self.tree.get_children()
        for i in x:
            self.tree.delete(i)
        if self.phoneNum.get() == "":
            tk.messagebox.showinfo("", "不能为空！")
        else:
            i = 0
            r = Application.staffGetTicketBooking(self.phoneNum.get())
            print(r)
            for result in r:
                self.tree.insert("", i, text=str(i + 1), values=(result[0], result[1], result[2], result[3], result[4],
                                                                 result[5], result[6], result[7]))
                i += 1

    def back(self):
        self.mngmt.destroy()
        MainPage(self.master)

if __name__ == '__main__':
    root1 = Tk()
    WelcomePage(root1)
    root1.mainloop()

    root = tk.Tk()
    BaseDesk(root)
    root.mainloop()
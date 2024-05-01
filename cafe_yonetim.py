import tkinter
from tkinter import ttk
import os
from tkinter import messagebox
from PIL import Image, ImageTk
uKontrol = False
kontrol = False
kKontrol = False
kullanicilar = {}
defaultMasa = ""
kullaniciAdi = ""
kullaniciSifre = ""
satir = 2
sutun = 0
masaSayisi = 0
secilenMasa = 0
urunum = ""
dosya = os.getcwd()
dosyaYolu = dosya + "\\masa"
geciciYol = ""
class Giris:
    def __init__(self):
        self.girisPencere = tkinter.Tk()
        self.girisPencere.title("Kullanıcı Girişi")
        self.screen_width = self.girisPencere.winfo_screenwidth()
        self.screen_height = self.girisPencere.winfo_screenheight()
        self.girisPencere.geometry(f"400x400+{(self.screen_width//2)-200}+{(self.screen_height//2)-300}")
        self.girisPencere.resizable(width=False,height=False)
        self.top = tkinter.Frame(self.girisPencere)
        self.photo_label = tkinter.Label(self.top)
        self.photo_label.pack()
        self.frame1 = tkinter.Frame(self.girisPencere)
        self.frame1.place(x=0,y=0,width=400,height=400)
        self.loginLabel = tkinter.Label(self.frame1,text="LOGIN")
        self.loginLabel.pack()
        self.kAdi = tkinter.StringVar()
        self.id = tkinter.Entry(self.frame1,borderwidth=3,textvariable=self.kAdi)
        self.id.pack()
        self.sifre = tkinter.StringVar()
        self.password = tkinter.Entry(self.frame1,borderwidth=3,textvariable=self.sifre)
        self.password.pack()
        self.buton = tkinter.Button(self.frame1,text="Giriş Yap",borderwidth=3,command=self.control)
        self.buton.pack()
        self.top.pack()
        self.frame1.pack()
        self.kullaniciAtamalari()
        self.gorsel()
        self.girisPencere.bind("<Return>", self.control)
        self.girisPencere.mainloop()
    def control(self,event=None):
        global kullaniciAdi
        global kullaniciSifre
        id = self.kAdi.get()
        password = self.sifre.get()
        if id in kullanicilar and password == kullanicilar[id]:
            kullaniciAdi = id
            kullaniciSifre = password
            self.girisPencere.destroy()
            Yonetim()
        else:
            girisHata = messagebox.showerror("Hata!","Kullanıcı adı ve/veya şifre hatalı!")
    def gorsel(self):
        photo_path = dosya + '\\cafe.png'
        image = Image.open(photo_path)
        image = image.resize((200,200))
        photo = ImageTk.PhotoImage(image)
        self.photo_label.config(image=photo)
        self.photo_label.image = photo
    def kullaniciAtamalari(self):
        global kullanicilar
        global defaultMasa
        kullanicilar.clear()
        kullaniciDoldurma = open(f'{dosya}\\kullanicilar.txt','r')
        doldurmaSatir = int(kullaniciDoldurma.readline().strip('\n'))
        defaultMasa = doldurmaSatir
        doldurmaSatir = kullaniciDoldurma.readline()
        while doldurmaSatir != '':
            doldurmaSatir = doldurmaSatir.strip('\n')
            doldurmaSatir = doldurmaSatir.split(',')
            list(doldurmaSatir)
            kullanicilar[doldurmaSatir[0]] = doldurmaSatir[1]
            doldurmaSatir = kullaniciDoldurma.readline()
        kullaniciDoldurma.close()
class Yonetim:
    def __init__(self):
        self.yonetimPencere = tkinter.Tk()
        self.yonetimPencere.title("Yönetim Paneli")
        self.screen_width = self.yonetimPencere.winfo_screenwidth()
        self.screen_height = self.yonetimPencere.winfo_screenheight()
        self.yonetimPencere.geometry(f"920x830+{(self.screen_width//2)-460}+{(self.screen_height//2)-450}")
        self.yonetimPencere.resizable(width=False,height=False)
        self.top = tkinter.Frame(self.yonetimPencere,width=1360,height=20).place(x=0,y=0)
        self.masa = tkinter.Button(self.top,text="EKRANI KİLİTLE",command=self.kilitle,width=15)
        self.masa.grid(row=0,column=0)
        self.urun = tkinter.Button(self.top,text="ÜRÜNLER",command=self.urunler,width=15)
        self.urun.grid(row=0,column=1)
        self.ayar = tkinter.Button(self.top,text="AYARLAR",command=self.ayarlar,width=15)
        self.ayar.grid(row=0,column=2)
        self.frame1 = tkinter.Frame(self.yonetimPencere,width=1360,height=20).place(x=0,y=30)
        self.frame2 = tkinter.Frame(self.yonetimPencere,width=1360,height=750)
        self.frame2.place(x=0,y=60)
        self.label = tkinter.Label(self.frame1, text="Masa Ekle:",width=15)
        self.label.grid(row=1,column=0)
        self.entry = tkinter.Entry(self.frame1,width=15)
        self.entry.grid(row=1,column=1)
        self.create_button = tkinter.Button(self.frame1, text="Masaları Ekle", command=self.masaEkle,width=15)
        self.create_button.grid(row=1,column=2)
        self.ekleButon = tkinter.Button(self.frame1,text="-",command=self.silMasa)
        self.ekleButon.grid(row=1,column=3)
        self.silButon = tkinter.Button(self.frame1,text="+",command=self.ekleMasa)
        self.silButon.grid(row=1,column=4)
        self.create_buttons()
        self.yonetimPencere.mainloop()
    def kilitle(self):
        global masaSayisi
        global defaultMasa
        global satir
        global sutun
        defaultMasa = masaSayisi
        masaSayisi = 0
        satir = 2
        sutun = 0
        self.yonetimPencere.destroy()
        Giris()
    def urunler(self):
        global masaSayisi
        global defaultMasa
        global satir
        global sutun
        defaultMasa = masaSayisi
        masaSayisi = 0
        satir = 2
        sutun = 0
        self.yonetimPencere.destroy()
        UrunYonetim()
    def ayarlar(self):
        global masaSayisi
        global defaultMasa
        global satir
        global sutun
        defaultMasa = masaSayisi
        masaSayisi = 0
        satir = 2
        sutun = 0
        self.yonetimPencere.destroy()
        Ayarlar()
    def button_click(self,button_id):
        global secilenMasa
        global masaSayisi
        global defaultMasa
        global satir
        global sutun
        global dosyaYolu
        global geciciYol
        secilenMasa = button_id
        self.yonetimPencere.destroy()
        defaultMasa = masaSayisi
        masaSayisi = 0
        satir = 2
        sutun = 0
        aktifYol = dosyaYolu + str(button_id) + ".txt"
        geciciYol = aktifYol
        try:
            dosya =open(aktifYol,'r')
            dosya.close()
            MasaIslem()
        except:
            dosya = open(aktifYol,"w")
            dosya.close()
            MasaIslem()
    def create_buttons(self):
        global satir
        global sutun
        global masaSayisi
        global defaultMasa
        button_count = defaultMasa
        for i in range(button_count):
            button = tkinter.Button(self.frame2, text=f"MASA {masaSayisi+1}")
            button.config(command=lambda button_id=masaSayisi+1: self.button_click(button_id),width=15,height=5)
            masaSayisi = masaSayisi + 1
            if sutun % 8 == 0:
                sutun = 0
                satir = satir + 1
            button.grid(row=satir,column=sutun)
            sutun = sutun + 1
    def masaEkle(self):
        global masaSayisi
        global sutun
        global satir
        button_count = int(self.entry.get())
        for i in range(button_count):
            button = tkinter.Button(self.frame2, text=f"MASA {masaSayisi+1}")
            button.config(command=lambda button_id=masaSayisi+1: self.button_click(button_id),width=15,height=5)
            masaSayisi = masaSayisi + 1
            if sutun % 8 == 0:
                sutun = 0
                satir = satir + 1
            button.grid(row=satir,column=sutun)
            sutun = sutun + 1
    def ekleMasa(self):
        global masaSayisi
        global sutun
        global satir
        button_count = 1
        for i in range(button_count):
            button = tkinter.Button(self.frame2, text=f"MASA {masaSayisi+1}")
            button.config(command=lambda button_id=masaSayisi+1: self.button_click(button_id),width=15,height=5)
            masaSayisi = masaSayisi + 1
            if sutun % 8 == 0:
                sutun = 0
                satir = satir + 1
            button.grid(row=satir,column=sutun)
            sutun = sutun + 1
    def silMasa(self):
        global masaSayisi
        global sutun
        global satir
        if masaSayisi > 0:
            masaSayisi = masaSayisi - 1
            sutun = masaSayisi % 8
            last_button = self.frame2.winfo_children()[-1]
            last_button.destroy()
            if sutun % 8 == 0:
                satir = satir - 1
class MasaIslem():
    def __init__(self):
        self.mPencere = tkinter.Tk()
        self.mPencere.title(str(secilenMasa) + ". Masa")
        self.screen_width = self.mPencere.winfo_screenwidth()
        self.screen_height = self.mPencere.winfo_screenheight()
        self.mPencere.geometry(f"1400x800+{(self.screen_width//2)-700}+{(self.screen_height//2)-450}")
        self.mPencere.resizable(width=False,height=False)
        self.left = tkinter.Frame(self.mPencere,width=700,height=800).place(x=0,y=0)
        self.right = tkinter.Frame(self.mPencere,width=700,height=800).place(x=701,y=0)
        self.treeview = ttk.Treeview(self.left, columns=("Adet","Urun", "Fiyat"))
        self.treeview.heading("#0", text="Adet", anchor="w")
        self.treeview.heading("#1", text="Ürün Adı", anchor="w")
        self.treeview.heading("#2", text="Toplam Fiyat", anchor="w")
        self.treeview.column("#0", width=50)
        self.treeview.column("#1", width=500)
        self.treeview.column("#2", width=150)
        self.treeview.place(x=0,y=0,width=700,height=800)
        self.urunListesi = tkinter.Listbox(self.right,exportselection="False",width=700,height=15)
        self.urunListesi.bind('<<ListboxSelect>>',self.secim)
        self.urunListesi.place(x=701,y=0)
        self.adetString = tkinter.StringVar()
        self.adetGirdi = tkinter.Entry(self.right,textvariable=self.adetString,width=25).place(x=940,y=270)
        self.butonBir = tkinter.Button(self.right,text="1",width=5,height=5,command=lambda: self.girdi(1)).place(x=940,y=300)
        self.butonIki = tkinter.Button(self.right,text="2",width=5,height=5,command=lambda: self.girdi(2)).place(x=1020,y=300)
        self.butonUc = tkinter.Button(self.right,text="3",width=5,height=5,command=lambda: self.girdi(3)).place(x=1100,y=300)
        self.butonDort = tkinter.Button(self.right,text="4",width=5,height=5,command=lambda: self.girdi(4)).place(x=940,y=390)
        self.butonBes = tkinter.Button(self.right,text="5",width=5,height=5,command=lambda: self.girdi(5)).place(x=1020,y=390)
        self.butonAlti = tkinter.Button(self.right,text="6",width=5,height=5,command=lambda: self.girdi(6)).place(x=1100,y=390)
        self.butonYedi = tkinter.Button(self.right,text="7",width=5,height=5,command=lambda: self.girdi(7)).place(x=940,y=480)
        self.butonSekiz = tkinter.Button(self.right,text="8",width=5,height=5,command=lambda: self.girdi(8)).place(x=1020,y=480)
        self.butonDokuz = tkinter.Button(self.right,text="9",width=5,height=5,command=lambda: self.girdi(9)).place(x=1100,y=480)
        self.butonTemizle = tkinter.Button(self.right,text="Temizle",width=5,height=5,command=self.temizle).place(x=940,y=570)
        self.butonSifir = tkinter.Button(self.right,text="0",width=5,height=5,command=lambda: self.girdi(0)).place(x=1020,y=570)
        self.butonGonder = tkinter.Button(self.right,text="EKLE",width=5,height=5,command=lambda: self.ekleme()).place(x=1100,y=570)
        self.urunSil = tkinter.Button(self.right,text="ÜRÜN SİL",width=10,height=5,command=lambda: self.urunSilme()).place(x=701,y=300)
        self.butonTemizle = tkinter.Button(self.right,text="Masayı Temizle",width=11,height=5,command=lambda: self.masaTemizleme()).place(x=912,y=690)
        self.comboMasa = tkinter.StringVar()
        self.comboMasaSecim = ttk.Combobox(self.right,textvariable=self.comboMasa)
        masalar = []
        for m in range(1,defaultMasa+1):
            masalar.append(m)
        self.comboMasaSecim['values'] = (masalar)
        self.comboMasaSecim.current(secilenMasa - 1)
        self.comboMasaSecim.place(x=960,y=660)
        self.butonAktar = tkinter.Button(self.right,text="Masayı Aktar",width=11,height=5,command=self.masaAktarma).place(x=1010,y=690)
        self.butonTemizle = tkinter.Button(self.right,text="Adisyon",width=11,height=5,command=self.adisyon).place(x=1108,y=690)
        self.masaUrunler()
        self.listeUrun()
        self.mPencere.mainloop()
        Yonetim()
    def secim(self,event):
        global urunum
        urunum = self.urunListesi.get(self.urunListesi.curselection())
    def masaUrunler(self):
        global geciciYol
        okunanMasa = open(geciciYol,'r')
        masaSatir = okunanMasa.readline()
        while masaSatir != '':
            okunanUrunler = open(f'{dosya}\\urunler.txt','r')
            masaSatir = masaSatir.split(',')
            list(masaSatir)
            urunSatir = okunanUrunler.readline()
            while urunSatir != '':
                urunSatir = urunSatir.split(',')
                list(urunSatir)
                if masaSatir[0] == urunSatir[0]:
                    urunAdedi = masaSatir[1]
                    urunAdi = masaSatir[0]
                    urunFiyat = int(urunSatir[1])
                    urunToplamFiyat = int(urunAdedi) * urunFiyat
                    self.treeview.insert("", "end",text=urunAdedi, values=(urunAdi,urunToplamFiyat))
                urunSatir = okunanUrunler.readline()
            masaSatir = okunanMasa.readline()

    def listeUrun(self):
        urunler = []
        urunListeleme = open(f'{dosya}\\urunler.txt','r')
        okunanUrun = urunListeleme.readline()
        while okunanUrun != '':
            okunanUrun = okunanUrun.split(',')
            list(okunanUrun)
            urunler.append(okunanUrun[0])
            okunanUrun = urunListeleme.readline()
        for urun in urunler:
            self.urunListesi.insert(tkinter.END,urun)
        urunListeleme.close()
    def girdi(self,number):
        aktif = str(self.adetString.get())
        self.adetString.set(aktif + str(number))
    def temizle(self):
        self.adetString.set("")
    def ekleme(self):
        global urunum
        global geciciYol
        eklemeMasa = open(geciciYol,'a')
        eklemeMasa.write(urunum + ',' + self.adetString.get() + '\n')
        urunFiyat = open(f'{dosya}\\urunler.txt','r')
        urunSatir = urunFiyat.readline()
        while urunSatir != '':
            urunSatir = urunSatir.split(',')
            list(urunSatir)
            if urunSatir[0] == urunum:
                fiyat = int(self.adetString.get()) * int(urunSatir[1])
            urunSatir = urunFiyat.readline()
        self.treeview.insert("","end",text=self.adetString.get(), values=(urunum,fiyat))
        self.adetString.set("")
        urunFiyat.close()
    def urunSilme(self):
        secilenUrun = self.treeview.selection()
        secilenSatir = self.treeview.item(secilenUrun, "values")
        self.treeview.delete(secilenUrun)
        silmeDosyam = open(geciciYol,'r')
        yeniGelen = geciciYol.rstrip('.txt')
        yeniGelen = yeniGelen + 'gecici.txt'
        yeniDosyam = open(yeniGelen,'w')
        silmeSatir = silmeDosyam.readline()
        while silmeSatir != '':
            yazilacak = silmeSatir
            silmeSatir = silmeSatir.split(',')
            list(silmeSatir)
            if silmeSatir[0] != secilenSatir[0]:
                yeniDosyam.write(yazilacak)
            silmeSatir = silmeDosyam.readline()
        silmeDosyam.close()
        yeniDosyam.close()
        os.remove(geciciYol)
        os.rename(yeniGelen,geciciYol)
    def masaTemizleme(self):
        cevap = messagebox.askokcancel("Masa Temizlensin Mi?","Masadaki tüm bilgiler silinecek. Devam etmek istediğinizden emin misiniz?")
        if cevap == True:
            dosyaBoşaltma = open(geciciYol,'w')
            dosyaBoşaltma.close()
            for satir in self.treeview.get_children():
                self.treeview.delete(satir)
    def masaAktarma(self):
        cevapAktarma = messagebox.askokcancel("Masa Aktarılsın Mı?","Masadaki tüm bilgiler aktarılacak. Devam etmek istediğinizden emin misiniz?")
        if cevapAktarma == True:
            deneme = dosyaYolu + str(self.comboMasaSecim.get()) + '.txt'
            try:
                masaYeni = open(deneme,'r')
                newSatir = masaYeni.readline()
                masaYeni.close()
                if newSatir == '':
                    os.remove(deneme)
                    os.rename(geciciYol,deneme)
                else:
                    aktarmaHata = messagebox.showerror("Hata!","Aktarılacak yeni masa boş değil!")
            except FileNotFoundError:
                os.rename(geciciYol,deneme)
    def adisyon(self):
        toplamFiyat = 0
        urunler = self.treeview.get_children()
        print("Masa " + str(secilenMasa) + " adisyonu: ")
        print("-----------------------------")
        print("Adet" + "\t" + "Ürün" + "\t" + "\t" + "Fiyat")
        print("-----------------------------")
        for urun in urunler:
            urunAdet = self.treeview.item(urun,"text")
            urunIcerik = self.treeview.item(urun,"values")
            toplamFiyat = toplamFiyat + int(urunIcerik[1])
            print(urunAdet[0] + "\t" + urunIcerik[0] + "\t" + "\t" + urunIcerik[1])
        print("-----------------------------")
        print("Toplam Fiyat: " + "\t" + str(toplamFiyat))
class UrunYonetim:
    def __init__(self):
        self.urunPencere = tkinter.Tk()
        self.urunPencere.title("Ürün Yönetim Penceresi")
        self.screen_width = self.urunPencere.winfo_screenwidth()
        self.screen_height = self.urunPencere.winfo_screenheight()
        self.urunPencere.geometry(f"1400x800+{(self.screen_width//2)-700}+{(self.screen_height//2)-450}")
        self.urunPencere.resizable(width=False,height=False)
        self.solFrame = tkinter.Frame(self.urunPencere,width=700,height=800).place(x=0,y=0)
        self.sagFrame = tkinter.Frame(self.urunPencere,width=700,height=800).place(x=701,y=0)


        self.treeview = ttk.Treeview(self.solFrame, columns=("Urun", "Fiyat"))
        self.treeview.heading("#0", text="Ürün Adı", anchor="w")
        self.treeview.heading("#1", text="Toplam Fiyat", anchor="w")
        self.treeview.column("#0", width=550)
        self.treeview.column("#1", width=150)
        self.treeview.place(x=0,y=0,width=700,height=800)


        self.ekleme = tkinter.Button(self.sagFrame,text="ÜRÜN EKLE",width=20,height=10,command= self.uGizleGoster).place(x=840,y=300)
        self.silme = tkinter.Button(self.sagFrame,text="ÜRÜN SİL",width=20,height=10,command= self.sil).place(x=1060,y=300)
        self.urunAdLabel = tkinter.Label(self.sagFrame,text="Ürün Adı")
        self.urunAdLabel.place(x=801,y=230)
        self.urunAdEntry = tkinter.Entry(self.sagFrame)
        self.urunAdEntry.place(x=801,y=250)
        self.tutarLabel = tkinter.Label(self.sagFrame,text="Tutar")
        self.tutarLabel.place(x=1001,y=230)
        self.tutarEntry = tkinter.Entry(self.sagFrame)
        self.tutarEntry.place(x=1001,y=250)
        self.urunEkleButon = tkinter.Button(self.sagFrame,text="Ürünü Ekle",command=self.ekle)
        self.urunEkleButon.place(x=1201,y=250)
        self.uGorunmez()
        self.doldur()
        self.urunPencere.mainloop()
        Yonetim()
    def doldur(self):
        urunDosyam = open(f'{dosya}\\urunler.txt','r')
        satirim = urunDosyam.readline()
        while satirim != '':
            satirim = satirim.split(',')
            self.treeview.insert("", "end",text=satirim[0], values=(satirim[1]))
            satirim = urunDosyam.readline()
        urunDosyam.close()
    def ekle(self):
        if self.urunAdEntry.get() != "" and self.tutarEntry.get() != "":
            urunAd = self.urunAdEntry.get()
            toplamTut = self.tutarEntry.get()
            self.treeview.insert("", "end",text=urunAd, values=(toplamTut))
            urunDosyam = open(f'{dosya}\\urunler.txt','a')
            urunDosyam.write(urunAd + ',' + toplamTut + '\n')
            urunDosyam.close()
        else:
            bosBirakildi = messagebox.showerror("Hata!","Gerekli bilgiler eksik!")
    def sil(self):
        normalYol = f'{dosya}\\urunler.txt'
        kopyaYol = f'{dosya}\\urunlerGecici.txt'
        secilenUrun = self.treeview.selection()
        secilenSatir = self.treeview.item(secilenUrun, "text")
        self.treeview.delete(secilenUrun)
        silmeDosyam = open(normalYol,'r')
        yeniDosyam = open(kopyaYol,'w')
        silmeSatir = silmeDosyam.readline()
        while silmeSatir != '':
            yazilacak = silmeSatir.rstrip('\n')
            silmeSatir = silmeSatir.split(',')
            list(silmeSatir)
            if silmeSatir[0] != secilenSatir:
                yeniDosyam.write(yazilacak+'\n')
            silmeSatir = silmeDosyam.readline()
        silmeDosyam.close()
        yeniDosyam.close()
        os.remove(normalYol)
        os.rename(kopyaYol,normalYol)
    def uGizleGoster(self):
        global uKontrol
        if uKontrol == False:
            self.uGorunur()
            uKontrol = True
        else:
            self.uGorunmez()
            uKontrol = False
    def uGorunur(self):
        self.urunAdLabel.place(x=801,y=230)
        self.urunAdEntry.place(x=801,y=250)
        self.tutarLabel.place(x=1001,y=230)
        self.tutarEntry.place(x=1001,y=250)
        self.urunEkleButon.place(x=1201,y=250)
    def uGorunmez(self):
        self.urunAdLabel.place_forget()
        self.urunAdEntry.place_forget()
        self.tutarLabel.place_forget()
        self.tutarEntry.place_forget()
        self.urunEkleButon.place_forget()
class Ayarlar:
    def __init__(self):
        self.ayarPencere = tkinter.Tk()
        self.ayarPencere.title("Kullanıcı Ayarları")
        self.screen_width = self.ayarPencere.winfo_screenwidth()
        self.screen_height = self.ayarPencere.winfo_screenheight()
        self.ayarPencere.geometry(f"700x400+{(self.screen_width//2)-350}+{(self.screen_height//2)-300}")
        self.ayarPencere.resizable(width=False,height=False)
        self.masa = tkinter.Frame(self.ayarPencere)
        self.kullanici = tkinter.Frame(self.ayarPencere)
        self.sifreYonetim = tkinter.Frame(self.ayarPencere)
        self.kKayit = tkinter.Frame(self.ayarPencere)
        self.aktifMasaLabel = tkinter.Label(self.masa, text=f"Aktif Masa Sayısı: {defaultMasa}")
        self.aktifMasaLabel.pack()
        self.masaLabel = tkinter.Label(self.masa, text="Masa Sayısı:")
        self.masaLabel.pack(side="left")
        self.masaEntry = tkinter.Entry(self.masa)
        self.masaEntry.pack(side="left")
        self.masaButon = tkinter.Button(self.masa,text="KAYDET",command=self.masaSayiKaydet)
        self.masaButon.pack(side="left")
        self.kullaniciLabel1 = tkinter.Label(self.kullanici, text="Kullanıcı Adı:")
        self.kullaniciLabel1.pack(side="left")
        self.kullaniciLabel2 = tkinter.Label(self.kullanici, text=kullaniciAdi)
        self.kullaniciLabel2.pack(side="left")
        self.sifreButon = tkinter.Button(self.sifreYonetim,text="Şifre Yönetimi",command=self.gizleGoster)
        self.sifreButon.pack()
        self.sifre1Label = tkinter.Label(self.sifreYonetim, text="Eski Şifreyi Giriniz: ")
        self.sifre1Label.pack()
        self.eskiSifre1Entry = tkinter.Entry(self.sifreYonetim)
        self.eskiSifre1Entry.pack()
        self.yeniSifre1Label = tkinter.Label(self.sifreYonetim, text="Yeni Şifreyi Giriniz: ")
        self.yeniSifre1Label.pack()
        self.yeniSifre1Entry = tkinter.Entry(self.sifreYonetim)
        self.yeniSifre1Entry.pack()
        self.yeniSifre2Label = tkinter.Label(self.sifreYonetim, text="Yeni Şifreyi Tekrar Giriniz: ")
        self.yeniSifre2Label.pack()
        self.yeniSifre2Entry = tkinter.Entry(self.sifreYonetim)
        self.yeniSifre2Entry.pack()
        self.sifreDegisButon = tkinter.Button(self.sifreYonetim,text="Şifreyi Değiştir",command=self.sifreDegistir)
        self.kButon = tkinter.Button(self.kKayit,text='Yeni Kayıt Oluştur',command=self.kGizleGoster)
        self.kButon.pack()
        self.yeniKAdiLabel = tkinter.Label(self.kKayit, text= 'Kullanıcı Adı Giriniz: ')
        self.yeniKAdiLabel.pack()
        self.yeniKAdiEntry = tkinter.Entry(self.kKayit)
        self.yeniKAdiEntry.pack()
        self.yeniKSifre1Label = tkinter.Label(self.kKayit, text= 'Şifreyi Giriniz: ')
        self.yeniKSifre1Label.pack()
        self.yeniKSifre1Entry = tkinter.Entry(self.kKayit)
        self.yeniKSifre1Entry.pack()
        self.yeniKSifre2Label = tkinter.Label(self.kKayit, text= 'Şifreyi Tekrar Giriniz: ')
        self.yeniKSifre2Label.pack()
        self.yeniKSifre2Entry = tkinter.Entry(self.kKayit)
        self.yeniKSifre2Entry.pack()
        self.kayitOlustur = tkinter.Button(self.kKayit,text='Kayıt Oluştur',command=self.yeniKayit)
        self.sifreDegisButon.pack()
        self.masa.pack()
        self.kullanici.pack()
        self.sifreYonetim.pack()
        self.kKayit.pack()
        self.kGorunmez()
        self.gorunmez()
        self.ayarPencere.mainloop()
        Yonetim()
    def masaSayiKaydet(self):
        global defaultMasa
        eskiYol = f'{dosya}\\kullanicilar.txt'
        yeniYol = f'{dosya}\\kullanicilarGecici.txt'
        masaEskiD = open(eskiYol,'r')
        masaYeniD = open(yeniYol,'w')
        kopyaMasaSatir = masaEskiD.readline()
        masaYeniD.write(self.masaEntry.get() + '\n')
        kopyaMasaSatir = masaEskiD.readline()
        while kopyaMasaSatir != '':
            masaYeniD.write(kopyaMasaSatir)
            kopyaMasaSatir = masaEskiD.readline()
        masaEskiD.close()
        masaYeniD.close()
        os.remove(eskiYol)
        os.rename(yeniYol,eskiYol)
        defaultMasa = int(self.masaEntry.get())
    def sifreDegistir(self):
        sifreDosyam = open(f'{dosya}\\kullanicilar.txt','r')
        sifreSatir = sifreDosyam.readline()
        sifreSatir = sifreDosyam.readline()
        while sifreSatir != '':
            sifreSatir = sifreSatir.split(',')
            list(sifreSatir)
            if sifreSatir[0] == kullaniciAdi:
                if self.eskiSifre1Entry.get() == kullaniciSifre:
                    if self.yeniSifre1Entry.get() == self.yeniSifre2Entry.get():
                        yeniSifre = self.yeniSifre1Entry.get()
                        sifreDegisti = messagebox.showerror("Başarılı!","Şifre Başarıyla Değiştirildi!")
                        break
                    else:
                        degisimHata = messagebox.showerror("Hata!","Girilen Yeni Şifreler Aynı Değil!")
                else:
                    eskiSifreHata = messagebox.showerror("Hata!","Eski Şifre Doğru Değil!")
            sifreSatir = sifreDosyam.readline()
        sifreDosyam.close()
        eskiYol = f'{dosya}\\kullanicilar.txt'
        yeniYol = f'{dosya}\\kullanicilarGecici.txt'
        sifreEskiD = open(eskiYol,'r')
        sifreYeniD = open(yeniYol,'w')
        kopyaSatir = sifreEskiD.readline()
        sifreYeniD.write(kopyaSatir)
        kopyaSatir = sifreEskiD.readline()
        while kopyaSatir != '':
            sifsif = kopyaSatir.split(',')
            list(sifsif)
            if sifsif[0] == kullaniciAdi:
                yeniSatir = sifsif[0] + ',' + yeniSifre + '\n'
                sifreYeniD.write(yeniSatir)
            else:
                sifreYeniD.write(kopyaSatir)
            kopyaSatir = sifreEskiD.readline()
        sifreEskiD.close()
        sifreYeniD.close()
        os.remove(eskiYol)
        os.rename(yeniYol,eskiYol)
    def yeniKayit(self):
        kullaniciAdiYeni = self.yeniKAdiEntry.get()
        if self.yeniKSifre1Entry.get() == self.yeniKSifre2Entry.get():
            kullaniciSifreYeni = self.yeniKSifre1Entry.get()
            kayit = open(f'{dosya}\\kullanicilar.txt','a')
            yeniKullanici = kullaniciAdiYeni + ',' + kullaniciSifreYeni + '\n'
            kayit.write(yeniKullanici)
        kayit.close()
    def kGorunmez(self):
        self.yeniKAdiLabel.pack_forget()
        self.yeniKAdiEntry.pack_forget()
        self.yeniKSifre1Label.pack_forget()
        self.yeniKSifre1Entry.pack_forget()
        self.yeniKSifre2Label.pack_forget()
        self.yeniKSifre2Entry.pack_forget()
        self.kayitOlustur.pack_forget()
    def kGorunur(self):
        self.yeniKAdiLabel.pack()
        self.yeniKAdiEntry.pack()
        self.yeniKSifre1Label.pack()
        self.yeniKSifre1Entry.pack()
        self.yeniKSifre2Label.pack()
        self.yeniKSifre2Entry.pack()
        self.kayitOlustur.pack()
    def gorunmez(self):
        self.sifre1Label.pack_forget()
        self.eskiSifre1Entry.pack_forget()
        self.yeniSifre2Label.pack_forget()
        self.yeniSifre2Entry.pack_forget()
        self.yeniSifre1Label.pack_forget()
        self.yeniSifre1Entry.pack_forget()
        self.sifreDegisButon.pack_forget()
    def gorunur(self):
        self.sifre1Label.pack()
        self.eskiSifre1Entry.pack()
        self.yeniSifre2Label.pack()
        self.yeniSifre2Entry.pack()
        self.yeniSifre1Label.pack()
        self.yeniSifre1Entry.pack()
        self.sifreDegisButon.pack()
    def gizleGoster(self):
        global kontrol
        if kontrol == False:
            self.gorunur()
            kontrol = True
        else:
            self.gorunmez()
            kontrol = False
    def kGizleGoster(self):
        global kKontrol
        if kKontrol == False:
            self.kGorunur()
            kKontrol = True
        else:
            self.kGorunmez()
            kKontrol = False
if __name__ == "__main__":
    Giris()
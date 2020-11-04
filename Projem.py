import sqlite3 as sql

class Turkoglu:
    def __init__(self,sirketIsmi):
        self.sirketIsmi =sirketIsmi
        self.calismaDurumu = True
        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            imlec.execute("CREATE TABLE IF NOT EXISTS mallar(odun,komur,soba)")
            imlec.execute("CREATE TABLE IF NOT EXISTS paralar(nakit,borc,alacakNakit)")
            imlec.execute("CREATE TABLE IF NOT EXISTS müsteriler(ad,tur,miktar,fiyat)")
            imlec.execute("CREATE TABLE IF NOT EXISTS birim_fiyatlar(BRkomur,BRodun,BRsoba)")
            with open("kontrol.txt","r")as dosya:
              kontrol =dosya.read()
              if kontrol=="0":

                print("BU GİRDİLER BİR DEFALI OLACAKTIR .")
                print("*********** PARA İŞLEMLERİ *********** ")
                nakit =int(input("Kasadaki Toplam Para Miktarını Giriniz : "))
                borc =int(input("Borçlu Olduğunuz Toplam Parayı Giriniz : "))
                alacak = int(input("Alacaklı Olduğunuz Toplma Parayı Giriniz : "))
                imlec.execute("INSERT INTO paralar(nakit,borc,alacakNakit) VALUES ('"+str(nakit)+"','"+str(borc)+"','"+str(alacak)+"')")
                print("*********** Malların Girdileri ***********")
                odunMiktar=int(input("Stokta Bulunan Odun Miktarını Ton Cinsinden Giriniz : "))
                komurMiktar=int(input("Stokta Bulunan Kömür Miktarını Ton Cinsinden Giriniz : "))
                sobaMiktar=int(input("Stokta Bulunan Soba Adetini Giriniz : "))
                imlec.execute("INSERT INTO mallar(odun,komur,soba) VALUES ('"+str(odunMiktar)+"','"+str(komurMiktar)+"','"+str(sobaMiktar)+"')")
                print("*********** Malların Fiyat Girdileri ***********")
                BRodun =int(input("1 Ton Odunun Fiyatını Giriniz : "))
                BRkomur =int(input("1 Ton Kömürün Fiyatını Giriniz : "))
                BRsoba =int(input("1 Ton Sobanın Fiyatını Giriniz : "))
                imlec.execute("INSERT INTO birim_fiyatlar(BRkomur,BRodun,BRsoba) VALUES ('"+str(BRkomur)+"','"+str(BRodun)+"','"+str(BRsoba)+"')")
                print("*******************************************************")
                print("GİRDİLER BİTMİŞTİR.UYGULAMANIZI KULLANABİLİRSİNİZ")

                with open("kontrol.txt","w")as dosya:
                    dosya.write("1")
                    print("GİRDLERİNZ KAYIT EDİLMİŞTİR.")
              if kontrol =="1":
                  pass

    def Menu(self):
        print("*"*50)
        secim =int(input("1)Durum Görüntüle\n2)Kasaya Para Ekle\n3)Kasadan Para Çıkar\n4)Borç Ekle\n5)Borç Eksilt\n6)Stokları Güncelle\n7)Stokları Görüntüle\n"))
        print("*"*50)
        if secim ==1:
            self.DurumGoruntule()
        if secim ==2:
            self.ParaEkle()
        if secim ==3:
            self.ParaCıkar()
        if secim ==4:
            self.BorcEkle()
        if secim ==5:
            self.BorcEksilt()
        if secim ==6:
            self.StoklariGuncelle()
        if secim ==7:
            self.StolariGoruntule()


    def DurumGoruntule(self):

        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            imlec.execute("SELECT * FROM paralar")
            bilgiler =imlec.fetchall()
            print(f"Nakit : {bilgiler[0][0]}\nBorc : {bilgiler[0][1]}\nVeresiye : {bilgiler[0][2]}")

    def ParaEkle(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            girdi =int(input("Kasaya Kaç Tl Para Eklemek İstersiniz : "))
            imlec.execute("SELECT nakit FROM paralar")
            para =int(imlec.fetchall()[0][0])
            yeni_para =para + girdi
            imlec.execute("UPDATE paralar SET nakit ='"+str(yeni_para)+"' WHERE nakit ='"+str(para)+"'")
    def ParaCıkar(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec = veritabani.cursor()
            girdi =int(input("Kasadan Kaç Tl Çıkarmak İstersiniz : "))
            imlec.execute("SELECT nakit FROM paralar")
            para =int(imlec.fetchall()[0][0])
            yeni_para =para - girdi
            imlec.execute("UPDATE paralar SET nakit ='"+str(yeni_para)+"'WHERE nakit='"+str(para)+"'")
    def BorcEkle(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            girdi =int(input("Kasaya Kaç TL Borç Girmek İstersiniz : "))
            imlec.execute("SELECT borc FROM paralar")
            borc=int(imlec.fetchall()[0][0])
            yeni_borc =borc + girdi
            imlec.execute("UPDATE paralar SET borc ='"+str(yeni_borc)+"'WHERE borc='"+str(borc)+"'")
    def BorcEksilt(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            girdi =int(input("Kasadan Kaç TL Borç Çıkmak İstersiniz : "))
            imlec.execute("SELECT borc FROM paralar")
            borc =int(imlec.fetchall()[0][0])
            yeni_borc =borc - girdi
            imlec.execute("UPDATE paralar SET borc ='"+str(yeni_borc)+"'WHERE borc='"+str(borc)+"'")
    def StoklariGuncelle(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec = veritabani.cursor()
            secim =int(input("1)Kömür\n2)Odun\n3)Soba\nGüncellemek İstediğiniz Malın Numarasını Giriniz : "))
            print("*"*50)
            if secim ==1:
                imlec.execute("SELECT komur FROM mallar")
                cikti =int(input("1)Arttır\n2)Azalt\nHangi İşlemi Yapmak İstersiniz : "))

                if cikti ==1:
                    soru =int(input("Kaç Ton Arttırmak İstersininz : "))
                    komur =int(imlec.fetchall()[0][0])
                    yeni_komur =komur + soru
                    imlec.execute("UPDATE mallar SET komur='"+str(yeni_komur)+"' WHERE komur='"+str(komur)+"'")
                if cikti ==2:
                    soru = int(input("Kaç Ton Azaltmak İstersininz : "))
                    komur = int(imlec.fetchall()[0][0])
                    yeni_komur = komur - soru
                    imlec.execute("UPDATE mallar SET komur='" + str(yeni_komur) + "' WHERE komur='" + str(komur) + "'")

            if secim ==2:
                imlec.execute("SELECT odun FROM mallar")
                cikti = int(input("1)Arttır\n2)Azalt\nHangi İşlemi Yapmak İstersiniz : "))

                if cikti == 1:
                    soru = int(input("Kaç Ton Arttırmak İstersininz : "))
                    odun = int(imlec.fetchall()[0][0])
                    yeni_odun = odun + soru
                    imlec.execute("UPDATE mallar SET odun='" + str(yeni_odun) + "' WHERE komur='" + str(odun) + "'")
                if cikti == 2:
                    soru = int(input("Kaç Ton Azaltmak İstersininz : "))
                    odun = int(imlec.fetchall()[0][0])
                    yeni_odun = odun - soru
                    imlec.execute("UPDATE mallar SET odun='" + str(yeni_odun) + "' WHERE komur='" + str(odun) + "'")
            if secim ==3:
                imlec.execute("SELECT soba FROM mallar")
                cikti = int(input("1)Arttır\n2)Azalt\nHangi İşlemi Yapmak İstersiniz : "))

                if cikti == 1:
                    soru = int(input("Kaç Adet Soba Arttırmak İstersininz : "))
                    soba = int(imlec.fetchall()[0][0])
                    yeni_soba = soba + soru
                    imlec.execute("UPDATE mallar SET soba='" + str(yeni_soba) + "' WHERE soba='" + str(soba) + "'")
                if cikti == 2:
                    soru = int(input("Kaç Adet Soba Azaltmak İstersininz : "))
                    soba = int(imlec.fetchall()[0][0])
                    yeni_soba = soba - soru
                    imlec.execute("UPDATE mallar SET odun='" + str(yeni_soba) + "' WHERE komur='" + str(soba) + "'")

    def StolariGoruntule(self):
        with sql.connect("kasa.sqlite")as veritabani:
            imlec =veritabani.cursor()
            imlec.execute("SELECT * FROM mallar")
            mallar =imlec.fetchall()
            print(f"ODUN : {mallar[0][0]} Ton\nKÖMÜR : {mallar[0][1]} Ton\nSOBA : {mallar[0][2]} Adet")

Mahmut =Turkoglu("GEREK")

while Mahmut.calismaDurumu:
    Mahmut.Menu()
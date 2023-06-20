#flow

def cekUsia(usia):

    #jika usia dbawah 20 maka jangan izinkan
    if usia<20 :
        print("Kamu belum bisa masuk")
    else :
        print("Silahkan masuk")


def checkUsername():
    username = input("Masukan username : ")

    if username =="Vorneus":
        print("Login berhasil")
    else :
        print("Username tidak terdaftar! ")

def login():
    username = input("Masukan username : ")
    password = input("Masukan password : ")

    if username == "Vorneus" and password =="232323":
        print("Login berhasil")
    else :
        print("Login gagal !")

def login2():
    username = input("Masukan username : ")
    password = input("Masukan password : ")

    if username != "Vorneus" or password != "232323" :
        print("Username atau password SALAH !")
        return
    print("Selamat Datang !")

def login3():
    dataUsername =["Vorneus","Hikari","Joneus","Ambatukam"]
    dataPassword =["232323","121212","131313","AAAHHH"]

    username = input("Masukan Username : ")

    if username not in dataUsername:
        print("Username tidak ditemukan ! ")
        return
    password = input("Masukan Password : ")

    if password not in dataPassword:
        print("Password SALAH!")
        return
    
    print("""
 =======================================================
 S E L A M A T - D A T A N G - D I - N E B U L A - M 7 8
 =======================================================
    """)

login3()
                             

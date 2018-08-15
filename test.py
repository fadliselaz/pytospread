import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
import random

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pakong-online-1fdb20ccf11b.json", scope)

gc = gspread.authorize(creds)

sheet = gc.open("test").sheet1
pp = pprint.PrettyPrinter()
# result = sheet.get_all_records()
# result = sheet.row_values(2)
# result = sheet.col_values(1)

# row, col
# result = int(sheet.cell(3, 4).value)
# pp.pprint(result)

# sheet.update_cell(3, 4, result + x)
# result = sheet.cell(3, 4).value
# pp.pprint(result)

# >>>>>>>> input username <<<<<<<<<<<<

# x = input("masukan username: ")
# y = input("masukan password: ")
# z = int(input("masukan uang : Rp. "))
# newUser = [x, y, z]

# sheet.append_row(newUser)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

dataUsername = sheet.col_values(1)
dataPassword = sheet.col_values(2)
dataUang = sheet.col_values(3)

def login():
    while True:
        x = input("username : ")
        y = input("password : ")
        if x in dataUsername and y in dataPassword:
            print("selamat datang")
            mainPakong()
            break
        else:
            print("username atau password salah..!!!")
            continue



def register():
    while True:
        x = input("masukan username: ")
        y = input("masukan password: ")
        z = 100000
        newUser = [x, y, z]

        tambah = sheet.append_row(newUser)
        if tambah:
            print("berhasil ditambahkan..!")
            print("\n" * 50)
            menu()
        else:
            print("gagal mendaftar.. /nSilakan coba kembali..")
            print("\n" * 50)
            menu()

def info():
    print("""
Pakong online..
cara cepat anda menjadi miliuner..

kami berikan modal dasar sebesar
Rp. 100.000
F R E E > > > >

Masih kurang puas..?
daftarkan 10 orang teman anda,
kami berikan Rp.100.000 lagi..

Ayo tunggu apa lagi,
daftarkan diri anda ke
Pakong Online RAJA NINGRAT..

    """)

    x = input("enter untuk kembali... : ")
    if x:
        print("\n" * 50)
        menu()
    else:
        print("\n" * 50)
        menu()


def mainPakong():
    uang = 100000
    space = "\n" * 10
    binatang = ["kambing", "kuda", "anjing", "babi"]
    binDecor = """
    *****************  ***********
    * K A M B I N G *  * K U D A *
    *****************  ***********

    ***************  ***********
    * A N J I N G *  * B A B I *
    ***************  ***********
    """ + space

    bangkrut = """
    ***********************************
    * A N D A  >> B A N G K R U T ! ! *
    ***********************************
    """ + space






    while True:
        pakongOnline = f"""
        ******************************
        * P A K O N G >> O N L I N E *
        ******************************

            >> by raja serah <<

        Keuntungan ditangan anda..
        kami berikan Free Rp.100.000

        Yang menang untung...
        Yang kalah untung...

        But Carabut Cabuuuuuttttt...


             U A N G  - A N D A
        *****************************
                   {uang}
        *****************************

        """

        print("\n" * 50)
        print(pakongOnline)
        print("uang anda : Rp.",uang)
        if uang <= 0:
            print("\n" * 50)
            print(bangkrut)
            time.sleep(5)
            menu()


        taruh = int(input("masukan taruhan anda : "))
        while taruh > uang or taruh < 5000:
            print("\n" * 50)
            print("Taruhan tidak sesuai.. \nSilakan masukan jumlah sesuai..\n minimal taruhan adalah Rp.5000")
            print("uang anda Rp.", uang)
            taruh = int(input("masukan taruhan anda : "))

        while taruh == uang:
            print("\n" * 50)
            val = input("anda akan mempertaruhkan \nsemua uang anda..?\nya / tidak : ")
            if val == "ya":
                break



        print("\n")
        print("\n" * 50)
        print(binDecor)
        x = input("pilih binatang anda: ")
        x = x.lower()
        if x in binatang:

            print("\n" * 50)
            print("semoga beruntung...")
            print("silakan tunggu...")
            time.sleep(3)
            print("but carabut cabutt...")
            time.sleep(1)

            print("\n" * 50)
            result = random.choice(binatang)

            print("""
    Binatangnya :
    **********************
    * >>>>> {} <<<<< *
    **********************""".format(result))


            if x == result:
                uang = uang + taruh
                print(f"""
    *****************************
    * >> SELAMAT ANDA MENANG << *
    *          {taruh}          *
    *****************************






    """)
                time.sleep(5)
                print("\n" * 50)
            else:
                uang = uang - taruh
                print("""
    ***************************
    * >> ANDA KALAH !!! << *  *
    * >> SILAKAN COBA LAGI << *
    ***************************





    """)
                time.sleep(5)
                print("\n" * 50)

        else:
            print("\nmaaf pilihan anda tidak ada..")




def menu():
    print(" ____   _    _  _____  _   _  ____")
    time.sleep(1)
    print("|  _ \ / \  | |/ / _ \| \ | |/ ___|")
    time.sleep(1)
    print("| |_) / _ \ | ' / | | |  \| | |  _")
    time.sleep(1)
    print("|  __/ ___ \| . \ |_| | |\  | |_| |")
    time.sleep(1)
    print("|_| /_/   \_\_|\_\___/|_| \_|\____|")
    time.sleep(1)

    print("\n---------  O N L I N E ------------")

    print("""
    1. Login Pakong
    2. Daftar Pakong
    3. Info Pakong
    4. Keluar...

    """)

    print("-------------------------------------")


    while True:
        x = input("\nMasukan pilihan anda: ")
        if x == "1":
            print("\n" * 50)
            login()
        elif x == "2":
            print("\n" * 50)
            register()
        elif x == "3":
            print("\n" * 50)
            info()
        elif x == "4":
            print("\n" * 50)
            exit()
        else:
            print("\n" * 50)
            print("maaf pilihan anda tidak ada..")
            menu()

menu()

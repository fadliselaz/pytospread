import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("flask-app-afc057120d09.json", scope)

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
            menu()
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

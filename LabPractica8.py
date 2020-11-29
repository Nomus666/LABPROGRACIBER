
from ftplib import FTP, FTP_PORT

host = input("Ingrese el host para la conexion FTP\n")
user = input("Ingrese su Usuario:\n")
passwd= ("anonymous")

tp = FTP (host, user, passwd)

archivos = tp.nlst()

tp.quit()

for name in archivos:

    print(name
)

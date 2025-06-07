import time
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fake_attack(name):
    clear()
    slow_print(f"{name} hedef alınıyor...")
    time.sleep(1)
    slow_print("Bağlantı kuruluyor...")
    time.sleep(1)
    for i in range(1, 101, 10):
        slow_print(f"İlerle: {i}%")
        time.sleep(0.3)
    slow_print("Veriler çekiliyor...")
    time.sleep(1)
    slow_print("Parolalar çözülüyor...")
    time.sleep(1)
    slow_print("[!] Güvenlik duvarı atlandı!")
    time.sleep(1)
    slow_print("✅ İşlem tamamlandı. Bilgiler sızdırıldı.")
    input("\nDevam etmek için Enter'a bas...")

def main():
    while True:
        clear()
        print("""
 ██████╗ ██╗   ██╗██████╗ ███████╗███████╗
██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
██║   ██║██║   ██║██████╔╝█████╗  ███████╗
██║▄▄ ██║██║   ██║██╔═══╝ ██╔══╝  ╚════██║
╚██████╔╝╚██████╔╝██║     ███████╗███████║
 ╚══▀▀═╝  ╚═════╝ ╚═╝     ╚══════╝╚══════╝
        Sahte Hacker Konsolu v1.0
        """)

        print("1. Instagram hesabı çal")
        print("2. WhatsApp mesajlarını sızdır")
        print("3. Konum bilgisi bul")
        print("4. Kamera erişimi sağla")
        print("5. Çıkış yap")
        choice = input("\nSeçiminiz: ")

        if choice == "1":
            fake_attack("Instagram")
        elif choice == "2":
            fake_attack("WhatsApp")
        elif choice == "3":
            fake_attack("Konum Servisi")
        elif choice == "4":
            fake_attack("Kamera Sistemi")
        elif choice == "5":
            slow_print("Çıkış yapılıyor...")
            break
        else:
            slow_print("Geçersiz seçim, tekrar dene...")
            time.sleep(1)

if __name__ == "__main__":
    main()

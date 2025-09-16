import time
import os
import sqlite3

VT_ADI = "rehber.db"

def temizle():
    """Konsolu temizler."""
    os.system("cls" if os.name == "nt" else "clear")

def baglan():
    """Veritabanı bağlantısını döndürür."""
    return sqlite3.connect(VT_ADI)

def menu():
    """Ana menüyü gösterir ve kullanıcıdan seçim alır."""
    temizle()
    print("\n========== ANA MENÜ ==========\n")
    print("1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Güncelle")
    print("4. Kişileri Listele")
    print("5. Çıkış\n")
    print("==============================\n")

    secim = input("👉 Menü Seçimi Yapınız: ")

    if secim == "1":
        ekle()
    elif secim == "2":
        sil()
    elif secim == "3":
        guncelle()
    elif secim == "4":
        listele()
    elif secim == "5":
        print("Çıkış Yapılıyor...")
        print("Güle Güle 👋")
        time.sleep(2)
        exit()
    else:
        print("⚠️ Geçerli Bir Değer Giriniz...")
        time.sleep(1)

    menu()

def ekle():
    """Veritabanına yeni bir kişi ekler."""
    temizle()
    print("\n--- KİŞİ EKLEME ---\n")
    listele_yardimci()

    isim = input("\n➕ Eklemek İstediğiniz Adı Girin: ").strip()

    if not isim:
        print("⚠️ İsim boş olamaz.")
        time.sleep(2)
        return

    try:
        conn = baglan()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kisiler (isim) VALUES (?)", (isim,))
        conn.commit()
        print(f"✅ '{isim}' rehbere eklendi.")
    except sqlite3.IntegrityError:
        print(f"⚠️ '{isim}' zaten rehberde kayıtlı.")
    finally:
        if conn:
            conn.close()

    time.sleep(2)

def sil():
    """Veritabanından bir kişiyi siler."""
    temizle()
    print("\n--- KİŞİ SİLME ---\n")
    listele_yardimci()

    hedef = input("\n❌ Silmek istediğiniz kişinin ID'sini veya adını girin: ").strip()

    if not hedef:
        print("⚠️ Boş değer girilemez.")
        time.sleep(2)
        return

    try:
        conn = baglan()
        cursor = conn.cursor()
        
        if hedef.isdigit():
            cursor.execute("DELETE FROM kisiler WHERE id = ?", (int(hedef),))
        else:
            cursor.execute("DELETE FROM kisiler WHERE isim = ?", (hedef,))
            
        degisen_satir = cursor.rowcount
        conn.commit()

        if degisen_satir > 0:
            print(f"✅ '{hedef}' rehberden silindi.")
        else:
            print(f"⚠️ '{hedef}' rehberde bulunamadı.")
    finally:
        if conn:
            conn.close()

    time.sleep(2)

def guncelle():
    """Veritabanında bir kişinin adını günceller."""
    temizle()
    print("\n--- KİŞİ GÜNCELLEME ---\n")
    listele_yardimci()

    hedef = input("\n✏️ Güncellemek istediğiniz kişinin ID'sini veya adını girin: ").strip()
    if not hedef:
        print("⚠️ Hedef boş olamaz.")
        time.sleep(2)
        return

    yeni_isim = input("🔄 Yeni adını girin: ").strip()
    if not yeni_isim:
        print("⚠️ Yeni ad boş olamaz.")
        time.sleep(2)
        return

    try:
        conn = baglan()
        cursor = conn.cursor()

        if hedef.isdigit():
            cursor.execute("UPDATE kisiler SET isim = ? WHERE id = ?", (yeni_isim, int(hedef)))
        else:
            cursor.execute("UPDATE kisiler SET isim = ? WHERE isim = ?", (yeni_isim, hedef))

        degisen_satir = cursor.rowcount
        conn.commit()

        if degisen_satir > 0:
            print(f"✅ '{hedef}' güncellendi -> '{yeni_isim}'.")
        else:
            print(f"⚠️ '{hedef}' rehberde bulunamadı.")
    except sqlite3.IntegrityError:
        print(f"⚠️ '{yeni_isim}' zaten rehberde kayıtlı. Güncelleme başarısız.")
    finally:
        if conn:
            conn.close()
    
    time.sleep(2)

def listele():
    """Veritabanındaki tüm kişileri listeler."""
    temizle()
    print("\n--- KİŞİLERİ LİSTELEME ---\n")
    listele_yardimci()
    input("\n➡️ Devam etmek için Enter'a basın...")

def listele_yardimci():
    """Liste işlemlerine yardımcı olan, veritabanını sorgulayan ve sonuçları yazdıran fonksiyon."""
    conn = baglan()
    cursor = conn.cursor()
    cursor.execute("SELECT id, isim FROM kisiler ORDER BY isim ASC")
    kisiler = cursor.fetchall()
    conn.close()

    if not kisiler:
        print("📂 Rehber şu anda boş.")
    else:
        print("📂 Mevcut Rehber:\n")
        for id, isim in kisiler:
            print(f"  ID: {id:<3} | Adı: {isim}")

# Programı başlat
if __name__ == "__main__":
    menu()
Basit CRUD Uygulaması

Bu proje, temel veritabanı işlemlerini (oluşturma, okuma, güncelleme ve silme) gerçekleştiren basit bir CRUD (Create, Read, Update, Delete) uygulamasıdır. Proje, Python dili kullanılarak geliştirilmiştir.

Özellikler

    Veri Oluşturma (Create): Veritabanına yeni kayıtlar ekleme.

    Veri Okuma (Read): Mevcut kayıtları listeleme.

    Veri Güncelleme (Update): Bir kaydın bilgilerini düzenleme.

    Veri Silme (Delete): Kayıtları veritabanından kalıcı olarak silme.

Gereksinimler

    Python 3.x

    db.py dosyasının çalıştırılması için gerekli modüller (eğer varsa, requirements.txt dosyasını belirtin).

Kurulum ve Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

1. Veritabanını Oluşturma

İlk olarak, db.py dosyasını çalıştırarak veritabanı dosyasının (genellikle database.db veya benzeri bir isimde) otomatik olarak oluşturulmasını sağlayın.
Bash

python3 db.py

Bu komut, projenin çalışması için gerekli olan veritabanı yapısını hazırlar.

2. Uygulamayı Başlatma

Veritabanı hazır olduktan sonra, uygulamayı app.py dosyasını çalıştırarak başlatabilirsiniz.
Bash

python3 app.py

Uygulama, terminalde çalışmaya başlayacak ve CRUD işlemleri için komut satırı arayüzü sunacaktır.

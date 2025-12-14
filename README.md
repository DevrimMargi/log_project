# Log Analiz Projesi

Bu proje, bir API’den veri çekerek sentetik loglar üretmeyi, bu logları regex kullanarak
parse etmeyi ve elde edilen veriler üzerinden istatistiksel raporlar oluşturmayı amaçlamaktadır.
Proje, Python ile paketli bir yapı kullanılarak geliştirilmiştir.

---

## 📌 Proje Özeti

Projede sırasıyla aşağıdaki adımlar uygulanmıştır:

1. API’den JSON formatında veri çekme
2. Çekilen verilerden log dosyası üretme
3. Log satırlarını regex ile parse etme
4. Logları analiz ederek CSV ve JSON raporları oluşturma
5. Tüm adımları komut satırı üzerinden yönetme (CLI)

---

## 📁 Proje Yapısı

log_project/
│
├── src/
│ ├── fetcher.py # API’den veri çekme
│ ├── log_generator.py # Log üretimi
│ ├── models.py # LogRecord modeli
│ ├── parser.py # Regex ile log çözümleme
│ ├── report.py # Rapor üretimi
│ └── main.py # Komut satırı arayüzü (CLI)
│
├── data/
│ ├── raw_posts.json # API’den çekilen ham veriler
│ └── app.log # Üretilen log dosyası
│
├── reports/
│ ├── summary.csv # CSV raporu
│ └── summary.json # JSON raporu
│
├── tests/
│ └── test_parser.py # Parser için örnek test
│
├── requirements.txt
└── README.md

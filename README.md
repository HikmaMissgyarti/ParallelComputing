# Parallel Computing — Matrix Example

## 👤 Author

Nama: **Nur Hikma Missgyarti**

Mata Kuliah: **Komputasi Paralel & Sistem Terdistribusi**

---

## 📌 Deskripsi Project

Project ini merupakan implementasi contoh arsitektur komputasi paralel berdasarkan klasifikasi Flynn, yaitu:

* SISD (Single Instruction Single Data)
* SIMD (Single Instruction Multiple Data)
* MISD (Multiple Instruction Single Data)
* MIMD (Multiple Instruction Multiple Data)

Semua contoh menggunakan operasi **penjumlahan matriks** agar perbedaan arsitektur mudah diamati.

---

## 🧠 Konsep Arsitektur

| Arsitektur | Konsep                            |
| ---------- | --------------------------------- |
| SISD       | Satu instruksi satu data (serial) |
| SIMD       | Satu instruksi banyak data        |
| MISD       | Banyak instruksi satu data        |
| MIMD       | Banyak instruksi banyak data      |

---

## ▶️ Cara Menjalankan Program

### 1️⃣ SISD

```
python sisd.py
```

---

### 2️⃣ SIMD

```
pip install numpy
python simd.py
```

---

### 3️⃣ MISD

```
python misd.py
```

---

### 4️⃣ MIMD

```
python mimd.py
```

---

## 📊 Hasil Output

### SISD Output

```
[[6, 8],
 [10, 12]]
```

### SIMD Output

```
[[ 6  8]
 [10 12]]
```

### MISD Output

```
Tambah: [[2, 3], [4, 5]]
Kali: [[2, 4], [6, 8]]
```

### MIMD Output

```
[[6, 8], [10, 12]]
```

---

## ⚖️ Analisis Perbedaan

| Arsitektur | Kelebihan                         | Kekurangan       |
| ---------- | --------------------------------- | ---------------- |
| SISD       | sederhana                         | lambat           |
| SIMD       | cepat untuk data besar            | terbatas operasi |
| MISD       | cocok untuk sistem fault-tolerant | jarang dipakai   |
| MIMD       | fleksibel & scalable              | kompleks         |

---

## 🏆 Kesimpulan

MIMD merupakan arsitektur paling powerful karena dapat menjalankan banyak instruksi pada banyak data secara paralel. Oleh karena itu, arsitektur ini paling banyak digunakan pada sistem modern seperti multi-core CPU dan distributed computing.

---

## 📎 Catatan

Project ini dibuat untuk memahami perbedaan konsep arsitektur paralel melalui implementasi langsung menggunakan Python.

---

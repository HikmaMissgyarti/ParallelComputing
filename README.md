# Parallel Computing — Matrix Example

Nama: **Nur Hikma Missgyarti** <br>
Mata Kuliah: **Komputasi Paralel & Sistem Terdistribusi**

---

## Deskripsi Project

Project ini merupakan implementasi contoh arsitektur komputasi paralel berdasarkan klasifikasi Flynn, yaitu:

* SISD (Single Instruction Single Data)
* SIMD (Single Instruction Multiple Data)
* MISD (Multiple Instruction Single Data)
* MIMD (Multiple Instruction Multiple Data)

Semua contoh menggunakan operasi **penjumlahan matriks** agar perbedaan arsitektur mudah diamati.

---

## Konsep Arsitektur

| Arsitektur | Konsep                            |
| ---------- | --------------------------------- |
| SISD       | Satu instruksi satu data (serial) |
| SIMD       | Satu instruksi banyak data        |
| MISD       | Banyak instruksi satu data        |
| MIMD       | Banyak instruksi banyak data      |

---

## Cara Menjalankan Program

### SISD

```
python SISD.py
```

---

### 2️⃣ SIMD

```
pip install numpy
python SIMD.py
```

---

### MISD

```
python MISD.py
```

---

### MIMD

```
python MIMD.py
```

---

## Output

### SISD Output

```
SISD: [[6, 8], [10, 12]]
```

### SIMD Output

```
SIMD:
[[ 6  8]
 [10 12]]
```

### MISD Output

```
MISD:
Tambah: [[2, 3], [4, 5]]
Kali: [[2, 4], [6, 8]]
```

### MIMD Output

```
MIMD:  [[6, 8], [10, 12]]
```

---

## Analisis Perbedaan

| Arsitektur | Kelebihan                         | Kekurangan       |
| ---------- | --------------------------------- | ---------------- |
| SISD       | sederhana                         | lambat           |
| SIMD       | cepat untuk data besar            | terbatas operasi |
| MISD       | cocok untuk sistem fault-tolerant | jarang dipakai   |
| MIMD       | fleksibel & scalable              | kompleks         |

---

## Kesimpulan

MIMD merupakan arsitektur paling kuat karena dapat menjalankan banyak instruksi pada banyak data secara paralel. Oleh karena itu, arsitektur ini paling banyak digunakan pada sistem modern seperti multi-core CPU dan distributed computing.

---

## Catatan

Project ini dibuat untuk memahami perbedaan konsep arsitektur paralel melalui implementasi langsung menggunakan Python.

---

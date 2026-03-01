import time

def hitung_kuadrat(x):
    return x * x

data = list(range(1, 11))  # 1 sampai 10

start = time.time()
hasil_serial = [hitung_kuadrat(x) for x in data]  # proses satu-satu
end = time.time()

print("Hasil Serial:", hasil_serial)
print("Waktu Serial:", round(end-start, 4), "detik")
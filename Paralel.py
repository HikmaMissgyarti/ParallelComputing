import time
from concurrent.futures import ThreadPoolExecutor  # bisa juga ProcessPoolExecutor

def hitung_kuadrat(x):
    return x * x

data = list(range(1, 11))

start = time.time()

# buat thread pool, jalankan fungsi hitung_kuadrat secara paralel
with ThreadPoolExecutor() as executor:
    hasil_parallel = list(executor.map(hitung_kuadrat, data))

end = time.time()

print("Hasil Parallel:", hasil_parallel)
print("Waktu Parallel:", round(end-start, 4), "detik")
import multiprocessing

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

def hitung(baris):
    return [A[baris][i] + B[baris][i] for i in range(2)]

if __name__ == "__main__":
    pool = multiprocessing.Pool(2)
    hasil = pool.map(hitung,[0,1])
    print("MIMD: ", hasil)
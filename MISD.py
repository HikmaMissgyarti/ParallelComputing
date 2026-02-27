import threading

A = [[1,2],[3,4]]

print("MISD:")
def tambah():
    print("Tambah:", [[x+1 for x in row] for row in A])

def kali():
    print("Kali:", [[x*2 for x in row] for row in A])

t1 = threading.Thread(target=tambah)
t2 = threading.Thread(target=kali)

t1.start()
t2.start()
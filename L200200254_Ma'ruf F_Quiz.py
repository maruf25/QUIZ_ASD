#Nomor 1
##import re
##
##username = '@25maruf_'
##cocok = re.findall(r'@[a-z]+[0-9]+_',username)
##if cocok:
##    print(cocok, "pass")
##else:
##    print("Failed")

#Nomor 2
##import re
##f = open('quizno2.txt')
##teks = f.read()
##f.close()
##p = r'\w+@+[\w.-]+'
##strings = re.findall(p,teks)
##print(strings)

#Nomer 3
class Pohon(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = Pohon("A")
B = Pohon("B")
C = Pohon("C")
D = Pohon("D")
E = Pohon("E")
F = Pohon("F")
G = Pohon("G")
H = Pohon("H")
I = Pohon("I")

A.kiri = B ; A.kanan = C
C.kiri = D ; C.kanan = E
E.kiri = F ; E.kanan = G
G.kiri = H
B.kiri = I

def cetakLuarKiri(data):
    if data is not None:
        cetakLuarKiri(data.kiri)
        print(data.data)
def cetakLuarKanan(data):
    if data is not None:
        print(data.data)
        cetakLuarKanan(data.kanan)
        

def cetakLuar(data):
    cetakLuarKiri(data)
    cetakLuarKanan(data)

cetakLuar(A)

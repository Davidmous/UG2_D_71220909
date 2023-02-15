nope = str(input('Masukkan Nomor Telepon : '))
 
def operator():
    if nope[0:4] == '0816' :
        print('Anda menggunakan operator Indosat')
    elif nope[0:4] == '0814' :
        print('Anda menggunakan operator Telkomsel')
    else :
        print('Operator anda tidak diketahui')

def ganjilgenap() :
    if int(nope) % 2 == 0 :
        print('Nomor anda berakhiran genap')
    else :
        print('Nomor anda berakhiran ganjil')

operator()
ganjilgenap()
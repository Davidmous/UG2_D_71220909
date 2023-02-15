print('='*12,'MAKANAN','='*12)
print('1. Telur Bakar          : Rp 7.000')
print('2. Lele Terbang Mas Bhe : Rp 10.000')
print('3. Es COklat Lempu      : Rp 5000')
print('4. Es Doger Langensai   : Rp 13.000')

telur1 = 7000
lele1 = 10000
coklat1 = 5000
doger1 = 13000

print('='*12,'PESANAN','='*12)
telur2 = int(input('Telur Bakar             : '))
lele2 = int(input('Lele Terbang            : '))
coklat2 = int(input('Es Coklat               : '))
doger2 = int(input('Es Doger                : '))
print('='*12,'TOTAL','='*12)
def total(telur, lele, coklat, doger) :
    telur3 = telur1 * telur2
    print('TOTA TELUR BAKAR x',telur2,' : Rp',telur3)
    lele3 = lele1 * lele2
    print('TOTA LELE TERBANG x',lele2,': Rp',lele3)
    coklat3 = coklat1 * coklat2
    print('TOTA ES COKLAT x',coklat2,'   : Rp',coklat3)
    doger3 = doger1 * doger2
    print('TOTA ES DOGER x',doger2,'    : Rp',doger3)
    jumlah = telur3 + lele3 + coklat3 + doger3
    print('Jumlah total biaya yang harus dibayar adalah Rp',jumlah)

total(telur1, lele1, coklat1, doger1)
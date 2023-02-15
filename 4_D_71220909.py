print('','','!! Selamat datang di H+ GYM !!')
print('Silahkan pilih menu dibawah ini:')
print('1. Menambah data')
print('2. Menampilkan data')
print('3. Keluar')
pilihan = input('Masukan Pilihan yang anda inginkan : ')

data_nama = []
data_member = []

for i in pilihan :
    if pilihan == '1' :
        nama = str(input('Masukan nama pelanggan : '))
        member = str(input('Masukkan jenis member : '))
        data_member.insert(0,nama)
        data_member.insert(0,member)
        print('Data sudah berhasil ditambahkan!')
    elif pilihan == '2':
        print(data_nama)
        print(data_member)
    else :
        break

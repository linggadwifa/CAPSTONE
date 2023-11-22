# Toko linggadwifa
list_barang = [['101', 'Mangkok', 100, 80000, 'Peralatan Makan'],
               ['201', 'Sendok', 200, 15000, 'Peralatan Makan'],
               ['301', 'Gelas', 500, 10000, 'Peralatan Minum'],
               ['401', 'Garpu', 2000, 20000, 'Peralatan Makan'],
               ['501', 'Piring', 500, 30000, 'Peralatan Makan'],
               ['601', 'Panci', 700, 35000, 'Peralatan Masak'],
               ['701', 'Pisau', 400, 50000, 'Peralatan Masak']]

daftar_jajan = []


# Menu toko linggadwifa
def menampilkan_daftar_barang():
    print('Selamat Datang Di Toko LinggaDwifa ')
    print('daftar barang\n')
    print('index\t| id_barang\t|    nama_barang\t|  stock_barang\t| harga_barang\t| Jenis Barang\t|')
    for i in range(len(list_barang)):
        print(f'{i}\t|{list_barang[i][0]}\t|{list_barang[i][1]}\t|{list_barang[i][2]}\t|{list_barang[i][3]}\t|{list_barang[i][4]}\t|')


# Menambah barang belanja
def menambah_barang():
    id_barang = input('Masukan ID barang : ')
    nama_barang = input('Masukan Nama Barang : ')
    stock_barang = int(input('Masukan Jumlah Barang Yang Ingin Dibeli : '))
    harga_barang = int(input('Masukkan Harga Barang : '))
    jenis_barang = input('Memasukkan jenis Barang Yang Dibeli : ')
    list_barang.append([id_barang, nama_barang, stock_barang, harga_barang, jenis_barang])
    menampilkan_daftar_barang()


# Menghapus Barang
def menghapus_barang():
    index_barang = int(input('Memasukan Index Barang Yang Anda Ingin Ganti/Hapus : '))
    if 0 <= index_barang < len(list_barang):
        del list_barang[index_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Index barang tidak valid.")
    menampilkan_daftar_barang()


# Membeli barang
def beli_barang():
    while True:
        index_barang = int(input('Masukkan Index Barang yang mau dibeli : '))
        if 0 <= index_barang < len(list_barang):
            jumlah_barang = int(input('Masukkan Jumlah Barang yang mau dibeli : '))
            if jumlah_barang > list_barang[index_barang][2]:
                print(f"Jumlah barang yang dimasukkan terlalu banyak. Stock barang hanya tersisa {list_barang[index_barang][2]}.")
            else:
                daftar_jajan.append([list_barang[index_barang][1], jumlah_barang, list_barang[index_barang][3], index_barang])
                print('Isi Daftar Belanja :')
                print('Nama\t| Jumlah_Barang\t| Harga')
                for item in daftar_jajan:
                    print(f'{item[0]}\t| {item[1]}\t| {item[2]}\t ')
                checker = input('Mau beli yang lain? (y/n) = ')
                if checker.lower() == 'n':
                    print('Daftar Belanja :')
                    print('Nama\t| jumlah_barang \t| Harga\t| Total Harga')
                    total_harga = 0
                    for item in daftar_jajan:
                        print(f'{item[0]}\t| {item[1]}\t| {item[2]}\t| {item[1] * item[2]}')
                        total_harga += item[1] * item[2]
                    while True:
                        print('Total Yang Harus Dibayar = {}'.format(total_harga))
                        jumlah_uang = int(input('Masukkan jumlah uang : '))
                        if jumlah_uang >= total_harga:
                            kembali = jumlah_uang - total_harga
                            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
                            for item in daftar_jajan:
                                list_barang[item[3]][2] -= item[1]
                            daftar_jajan.clear()
                            return
                        else:
                            kekurangan = total_harga - jumlah_uang
                            print('Uang anda kurang sebesar {}'.format(kekurangan))
                else:
                    print("Input yang tidak valid. Silakan masukkan 'y' atau 'n'.")
        else:
            print("Index barang tidak valid. Silakan masukkan index yang benar.")


# Update atau edit barang
def edit_barang():
    index_barang = int(input(' Memasukkan Index Barang yang Anda Perlu Edit : '))
    if 0 <= index_barang < len(list_barang):
        id_barang = input('Masukan ID barang : ')
        nama_barang = input('Masukan Nama Barang : ')
        stock_Barang = int(input('Masukan Jumlah Barang Yang ingin Dibeli : '))
        harga_barang = int(input('Masukan Harga Barang : '))
        jenis_barang = input('Memasukan jenis Barang Yang Dibeli : ')
        list_barang[index_barang] = [id_barang, nama_barang, stock_Barang, harga_barang, jenis_barang]
        print("Barang berhasil diubah.")
        menampilkan_daftar_barang()
    else:
        print("Index barang tidak valid. Silakan masukkan index yang benar.")



# Main Menu
while True:
    pilihan_menu = input('''
        Selamat Berbelanja Ditoko Linggadwifa, Silahkan Pilih Menu Yang Di inginkan!!
        List Menu :
        1. Menampilkan Daftar Barang
        2. Menambah Barang    
        3. Menghapus Barang
        4. Membeli Barang
        5. Edit input Barang
        6. Exit Program
        Masukkan angka menu yang anda pilih : ''')
    if pilihan_menu == '1':
        while True:
            opsi_menu_1 = input('''silakan masukan angkanya 1/2
            1. daftar barang
            2. menu utama
            Masukkan angka menu yang anda pilih :''')
            if opsi_menu_1 == '1':
                menampilkan_daftar_barang()
            elif opsi_menu_1 == '2':
                break
    elif pilihan_menu == '2':
        while True:
            opsi_menu_2 = input('''
            1. tambah barang
            2. tidak menambah
            Masukkan angka menu yang anda pilih :''')
            if opsi_menu_2 == '1':
                menambah_barang()
            elif opsi_menu_2 == '2':
                break
    elif pilihan_menu == '3':
        while True:
            opsi_menu_3 = input('''
            1. hapus barang
            2. tidak hapus barang
            Masukkan angka menu yang anda pilih :''')
            if opsi_menu_3 == '1':
                menghapus_barang()
            elif opsi_menu_3 == '2':
                break
    elif pilihan_menu == '4':
        while True:
            opsi_menu_4 = input('''
            1. beli barang
            2. tidak membeli
            Masukkan angka menu yang anda pilih :''')
            if opsi_menu_4 == '1':
                beli_barang()
            elif opsi_menu_4 == '2':
                break
    elif pilihan_menu == '5':
        while True:
            opsi_menu_5 = input('''
            1. edit barang
            2. tidak edit
            Masukkan angka menu yang anda pilih :''')
            if opsi_menu_5 == '1':
                edit_barang()
            elif opsi_menu_5 == '2':
                break
    elif pilihan_menu == '6':
        break
    else:
        print('error')

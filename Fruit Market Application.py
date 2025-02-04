# # Soal No. 1
# aku = {'Avengers', 'Hulk', 'Iron Man 3', 'Wonder Woman', 'Batman'}
# print("Film Favoritku: Avengers, Hulk, Iron Man 3, Wonder Woman, Batman")
# teman = set(input('Masukkan 5 Film Favoritmu: ').title().split(", "))
# sama = teman.intersection(aku)
# a = int((len(sama)/len(aku))*100)
# print(f"Kesamaan Film Favorit Kita Sebesar {a}%")
# print()

# Soal No. 2
data = [['Index', 'Nama', 'Stock', 'Harga'], ['Apel', 20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]
cart = [['Nama', 'Qty', 'Harga']]
while True:
    print()
    print("Selamat Datang di Pasar Buah")
    print()
    print("List Menu:")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    print()
    menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))
    print()
    if menu == 1:
        print('Daftar Buah')
        print()
        from tabulate import tabulate
        print(tabulate(data, headers = "firstrow", showindex='always'))
    elif menu == 2:
        buah = str(input('Masukkan Nama Buah: ')).title()
        stok = int(input('Masukkan Stock Buah: '))
        price = int(input('Masukkan Harga Buah: Rp '))
        print()
        data_baru = [buah, stok, price]
        data.append(data_baru)
        print('Daftar Buah')
        print()
        from tabulate import tabulate
        print(tabulate(data, headers = "firstrow", showindex='always'))
    elif menu == 3:
        print()
        print('Daftar Buah')
        print()
        from tabulate import tabulate
        print(tabulate(data, headers = "firstrow", showindex='always'))
        print()
        hapus = int(input('Masukkan Index Buah yang Ingin dihapus: '))
        for a in range(len(data) - 1):
            if a == hapus:
                del data[a + 1]
        from tabulate import tabulate
        print(tabulate(data, headers = "firstrow", showindex='always'))
    elif menu == 4:
        while True:
            print()
            print('Daftar Buah')
            print()
            from tabulate import tabulate
            print(tabulate(data, headers = "firstrow", showindex='always'))
            print()
            index_beli = int(input('Masukkan Index Buah yang Ingin dibeli: '))
            jmlbuah = int(input('Jumlah Buah yang Ingin dibeli: '))
            if jmlbuah > data[index_beli + 1][1]:
                print(f"Stok tidak cukup, stok {data[index_beli + 1][0]} tinggal {data[index_beli + 1][1]}")
                print()
                print('Keranjang Belanja')
                from tabulate import tabulate
                print(tabulate(cart, headers = "firstrow"))
                break
            elif jmlbuah <= data[index_beli + 1][1]:
                data[index_beli + 1][1] -= jmlbuah
                data_baru = data[index_beli + 1].copy()
                keranjang = (data_baru)
                keranjang[1] = jmlbuah
                cart.append(keranjang)
                from tabulate import tabulate
                print(tabulate(cart, headers = "firstrow"))
                total = 0
                for x in range(len(cart)):
                    if x >= 1:
                        y = cart[x][1]  
                        z = cart[x][2]  
                        yz = (y*z)
                        total += yz
                print(f"Total Belanja Anda Sebesar: Rp {total}")
            print()
            lanjutan = (str(input('Mau Beli yang Lain? (Ya/Tidak): '))).title()
            if lanjutan == 'Tidak':
                uang = int(input("Masukkan jumlah uang: Rp "))
                kembalian = uang-total
                kurang = total-uang
                if uang > total:
                    print("Terimakasih")
                    print(f"Uang kembali anda sebanyak Rp {kembalian}")
                elif uang == total:
                    print("Terimakasih")
                else:
                    print("Transaksi anda dibatalkan")
                    print(f"Uang anda kurang sebanyak Rp {kurang}")
                break
    else:
        print('Exit Program')
        break
# Data Initialization

barang_barang = [
    {'Kode_Barang': 'A001', 'Nama': 'Gula', 'Stock': 10, 'Harga': 15000, 'Kategori': 'Sembako'},
    {'Kode_Barang': 'A002', 'Nama': 'Garam', 'Stock': 15, 'Harga': 5000, 'Kategori': 'Sembako'},
    {'Kode_Barang': 'A003', 'Nama': 'Terigu', 'Stock': 20, 'Harga': 15000, 'Kategori': 'Sembako'},
    {'Kode_Barang': 'A004', 'Nama': 'Kecap', 'Stock': 10, 'Harga': 20000, 'Kategori': 'Bumbu Dapur'},
    {'Kode_Barang': 'A005', 'Nama': 'Telur', 'Stock': 50, 'Harga': 2000,'Kategori': 'Sembako'},
    {'Kode_Barang': 'A006', 'Nama': 'Lada', 'Stock': 20, 'Harga': 2000,'Kategori': 'Bumbu Dapur'},
    {'Kode_Barang': 'A007', 'Nama': 'Shampoo', 'Stock': 10, 'Harga': 10000,'Kategori': 'Toiletries'}
]


def tampilkan_daftar_barang():
    print("\n----------- Menampilkan Daftar Semua Barang -----------\n")

    print(" No | Kode_Barang  | Nama       | Stock | Harga | Kategori ")
    for i, b in enumerate(barang_barang, start = 1):
        print(f"{i:<3} | {b['Kode_Barang']:<12} | {b['Nama']:<10} | {b['Stock']:<5} | {b['Harga']:<5} | {b['Kategori']:<9}")

def mencari_barang():
    print("\n----------- Mencari Barang Menggunakan Kode -----------\n")
    mencari_lagi = 'y'
    while mencari_lagi == 'y':
        
        kode = input("Masukkan Kode_Barang yang anda cari: ").lower()
        ditemukan = False
        
        for b in barang_barang:
            if b['Kode_Barang'].lower() == kode:
                print("Barang ditemukan")
                print('Kode Barang: ', b['Kode_Barang'])
                print('Nama       : ', b['Nama'])
                print('Stock      : ', b['Stock'])
                print('Harga      : ', b['Harga'])
                print('Kategori   : ', b['Kategori'])
                ditemukan = True
        if not ditemukan:
            print('Barang {} tidak ditemukan'.format(kode))
            tampilkan_daftar_barang()

        while True:
            mencari_lagi = input("Apakah anda ingin mencari barang lagi? Y/N = ").strip().lower()
            if mencari_lagi in ['y','n']:
                break
            else:
                print("Masukkan hanya 'Y' atau 'N' saja ")




def mencari_barang_dengan_nama():
    print("\n----------- Mencari Barang Menggunakan Kode -----------")
    mencari_lagi ='y'
    while mencari_lagi == 'y':

        nama_cari = input("Masukkan Nama Barang yang anda cari: ").lower()
        ditemukan = False

        for b in barang_barang:
            if b['Nama'].lower() == nama_cari:
                print("Barang ditemukan")
                print('Kode Barang: ', b['Kode_Barang'])
                print('Nama       : ', b['Nama'])
                print('Stock      : ', b['Stock'])
                print('Harga      : ', b['Harga'])
                print('Kategori.  : ', b['Kategori'])
                ditemukan = True 
        if not ditemukan:
            print('barang {} tidak ditemukan'.format(nama_cari))
            tampilkan_daftar_barang()
        
        while True:
            mencari_lagi = input("Apakah anda ingin mencari barang lagi? Y/N = ").strip().lower()
            if mencari_lagi in ['y','n']:
                break
            else:
                print("Masukkan hanya 'Y' atau 'N' saja ")



def submenu_lihat_barang():
    sub = ''
    while sub != '4':
        print("\n------------- Sub Menu Melihat Barang -------------\n")
        print("1. Menampilkan Semua Barang")
        print("2. Mencari Barang Menggunakan Kode Barang")
        print("3. Mencari Barang Menggunakan Nama")
        print("4. Kembali ke Menu Utama")

        try:
            sub = int(input("Pilih Index Submenu [1-4]: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-4.")
            continue

        if sub == 1:
            tampilkan_daftar_barang()
        elif sub == 2:
            mencari_barang()
        elif sub ==3:
            mencari_barang_dengan_nama()
        elif sub == 4:
            break
        else:
            print("Pilihan menu yang anda masukkan tidak valid")


def menambah_barang():
    print("\n----------- Menambahkan Barang ke Daftar Barang -----------\n")
    tambah_lagi = 'y'
    while tambah_lagi == 'y':
        kode = input("Masukkan Kode_Barang: ").strip().upper()
        terdaftar = False

        for a in barang_barang:
            if a['Kode_Barang'].upper() == kode:
                print('========== Barang telah terdaftar ==========')
                terdaftar = True 
                break

        if not terdaftar:
            nama = input("Masukkan Nama barang: ").strip().title()
            stock = int(input("Masukkan Stock Barang: "))
            harga = int(input("Masukkan Harga Barang: "))
            kategori = input("Masukkan jenis kategori barang tersebut: ").strip().title()
            barang_barang.append ({"Kode_Barang" : kode, "Nama" : nama, "Stock" : stock, "Harga" : harga, "Kategori" : kategori})
            print(f"Barang {kode} berhasil ditambahkan")
        
        while True:
            tambah_lagi = input("Mau menambah barang lain? Y/N = ").strip().lower()
            if tambah_lagi in ['y','n']:
                break
            else:
                print("Masukkan hanya 'Y' atau 'N' saja ")

        tampilkan_daftar_barang()


def submenu_menambah_barang():
    sub = ''
    while sub != "2":
        print("\n------------- Sub Menu Menambah Barang -------------\n")
        print("1. Menambah Barang ke Daftar Barang")
        print("2. Kembali ke Menu Utama")
        
        try:
            sub = int(input("Pilih Index Submenu [1-2]: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-2.")
            continue

        if sub == 1:
            menambah_barang()
        elif sub == 2:
            break
        else: 
            print("Pilihan menu yang anda masukkan tidak valid")


def update_barang():
    print("\n----------- Mengupdate Barang di Daftar Barang -----------\n")
    update_lagi = 'y'
    while update_lagi == 'y':
        kode = input("Masukkan Kode_Barang: ").strip().upper()
        terdaftar = False 
        
        for a in barang_barang:
            if a ['Kode_Barang'].upper() == kode:
                print("Barang ditemukan")
                print(f"Kode_Barang : {a['Kode_Barang']}")
                print(f"Nama        : {a['Nama']}")
                print(f"Stock       : {a['Stock']}")
                print(f"Harga       : {a['Harga']}")
                print(f"Kategori    : {a['Kategori']}")
                a['Nama'] = input("Masukkan Nama baru yang ingin diubah: ").strip().title()
                a['Stock'] = int(input("Masukkan Stock baru yang ingin diubah: "))
                a['Harga'] = int(input("Masukkan Harga baru yang ingin diubah: "))
                a['Kategori'] = input("Masukkan Jenis Kategori yang ingin diubah: ").strip().title()
                print(f" Barang '{a['Nama']}' berhasil diupdate.")
                terdaftar = True
                break
        if not terdaftar:
            print("barang dengan kode tersebut tidak terdaftar: ")

        while True:
            update_lagi = input("Mau mengubah barang lain? Y/N = ").strip().lower()
            if update_lagi in ['y','n']:
                break
            else:
                print("Masukkan hanya 'Y' atau 'N' saja ")
    tampilkan_daftar_barang()



def sub_menu_update():
    sub = ""
    while sub != "2":
        print("\n----------- Sub Menu Mengupdate Barang -----------\n")
        print("1. Mengupdate Barang")
        print("2. Kembali ke Menu Utama")
        
        try:
            sub = int(input("Pilih Index Submenu [1-2]: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-2.")
            continue

        if sub == 1:
            update_barang()
        elif sub == 2:
            break
        else:
            print("Pilihan menu yang anda masukkan tidak valid")


def delete_barang():
    print("\n----------- Menghapus Barang dari Daftar Barang -----------\n")
    delete_lagi = 'y'
    while delete_lagi == 'y':
        tampilkan_daftar_barang()

        try:
            index = int(input("Masukkan index barang yang anda ingin hapus: "))-1
        except ValueError:
            print("Input harus berupa angka sesuai dengan index atau nomer urut barang")
            continue
        
        if 0 <= index < len(barang_barang):
            removed = barang_barang.pop(index)
            print(f"Barang '{removed['Nama']}'' berhasil dihapus")
        else: 
            print('Index tidak valid')
        
        while True: 
            delete_lagi = input("Mau menghapus barang lain? Y/N = ").strip().lower()
            if delete_lagi in ['y','n']:
                break
            else:
                print("Input tidak valid. Masukkan hanya 'Y' ataupun 'N' ")
    tampilkan_daftar_barang()



def sub_menu_delete():
    sub = ""
    while sub != "2":
        print("\n----------- Sub Menu Menghapus Barang -----------\n")
        print("1. Menghapus Barang")
        print("2. Kembali ke Menu Utama")

        try:
            sub = int(input("Pilih Index Submenu [1-2]: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-2.")
            continue

        if sub == 1:
            delete_barang()
        elif sub == 2:
            break
        else:
            print("Pilihan menu yang anda masukkan tidak valid")


def penjualan_barang():
    cart = [] 
    print("\n----------- Penjualan Barang Toko Murah Hati -----------\n")
    tambah_lagi = 'y'

    while tambah_lagi == 'y':
        tampilkan_daftar_barang()

        while True:
            teks = (input("Masukkan index barang yang ingin anda beli: ")).strip()
            try: 
                index = int(teks)-1
            except ValueError:
                print(f"Index tidak dikenal. Masukkan angka 1-{len(barang_barang)}.")
                continue

            if 0 <= index < len(barang_barang):
                break
            else:
                print(f"Index tidak valid. Pilih 1-{len(barang_barang)}.")

        barang = barang_barang[index]
        print(f"\nBarang dipilih: {barang['Nama']} | Stok: {barang['Stock']} | Harga: {barang['Harga']} | Kategori: {barang['Kategori']}")
        
        try:
            qty = int(input("\nMasukkan jumlah barang yang anda inginkan: "))
        except ValueError:
            print("Input harus berupa angka untuk jumlah barang")
            continue

        if qty > barang['Stock']:
            print(f"Stock tidak cukup, stok barang {barang['Nama']} tinggal {barang['Stock']} buah")
        else:
            total = qty*barang['Harga']
            cart.append({"Kode": barang['Kode_Barang'],
                    "qty": qty,
                    "nama": barang['Nama'],
                    "harga": barang['Harga'],
                    "kategori": barang['Kategori'],
                    "total": total
            })
            barang['Stock'] -= qty
            print(f"{qty} {barang['Nama']} berhasil dimasukkan ke keranjang.")

            # Tampilkan isi cart
        print("Isi Cart :")
        print(" No | Kode_Barang  | Nama       | Stock | Harga | Kategori")
        for i, item in enumerate(cart, start=1):
            print(f"{i:<3} | {item['Kode']:<12} | {item['nama']:<10} | {item['qty']:<5} | {item['harga']:<5} | {item['kategori']:<9}")

        while True:
            tambah_lagi = input("Mau tambah yang lain? (Y/N) = ").strip().lower()
            if tambah_lagi in ['y', 'n']:
                break
            else:
                print("Input tidak valid. Masukkan hanya 'y' atau 'n'")


    print("\n-----------Daftar Keranjang Belanja -----------\n")
    print("Nama   | Qty | Harga  | Total Harga")
    total_bayar = 0
    for item in cart:
        print(f"{item['nama']:<6} | {item['qty']:<3} | {item['harga']:<5} | {item['total']}")
        total_bayar += item['total']

    print(f'Total yang harus dibayar adalah {total_bayar}')

    while True :
        try:
            uang = int(input('\nMasukkan Jumlah uang pembayaran: '))
            if uang < total_bayar:
                kurang = total_bayar-uang
                print('\nUang yang dimasukkan kurang', kurang)
            elif uang > total_bayar:
                kembalian = abs(uang - total_bayar)
                print('\nUang Kembalian ', kembalian, '\n\nTerimakasih telah berbelanja di Toko Murah Hati')
                break
            elif uang == total_bayar:
                print('\nTerimakasih telah berbelanja di Toko Murah Hati')
                break
        except ValueError:
            print('Input tidak Valid')
        

# ==========================================================================================

def sub_menu_penjualan():
    sub = ""
    while sub != "2":
        print("\n----------- Sub Menu Penjualan Barang -----------\n")
        print("1. Penjualan Barang")
        print("2. Kembali ke Menu Utama")
        
        try:
            sub = int(input("Pilih Index Submenu [1-2]: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-2.")
            continue
        
        if sub == 1:
            penjualan_barang()
        elif sub == 2:
            break
        else:
            print("Pilihan menu yang anda masukkan tidak valid")


def menu_utama():
    while True: 
        print('\n----------- Selamat Datang di Toko Murah hati-----------\n')
        print('Menu Utama : ')
        print("1. Menampilkan Daftar Barang")
        print("2. Menambahkan Barang")
        print("3. Mengubah Barang")
        print("4. Menghapus Barang")
        print("5. Penjualan Toko Murah Hati")
        print("6. Exit")

        
        try:
            pilihan = int(input("Masukkan Menu yang akan dijalankan: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-6.")
            continue

        if pilihan == 1:
            submenu_lihat_barang()
        elif pilihan == 2:
            submenu_menambah_barang()
        elif pilihan == 3:
            sub_menu_update()
        elif pilihan == 4:
            sub_menu_delete()
        elif pilihan == 5:
            sub_menu_penjualan()
        elif pilihan == 6:
            print("\n----------- Terimakasih, Semoga Hari Anda Menyenangkan -----------")
            break
        else: 
            print("Pilihan anda tidak valid, tolong masukkan 1-6")

if __name__ == "__main__":
    menu_utama()





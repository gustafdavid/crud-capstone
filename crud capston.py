datapasien = [
    {"id": "P001","nama": "Andreas","gender": "L","penyakit":"Jantung"},
    {"id": "P002","nama": "Beatrice","gender": "P","penyakit":"Kulit"},
    {"id": "P003","nama": "Cruise","gender": "L","penyakit":"Jiwa"},
    {"id": "P004","nama": "Dune","gender": "L","penyakit":"Ginjal"}
]

def pause():
    input("\nTekan Enter untuk melanjutkan...")

def caripasien(id_pasien):
    for p in datapasien:
        if p["id"].upper() == id_pasien.upper():
            return p
    return None

def print_table(data_list):
    print("\n" + "=" * 50)
    print(f"{'ID PASIEN':<10} | {'NAMA':<10} | {'GENDER':<8} | {'PENYAKIT':<10}")
    print("-" * 50)
    for p in data_list:
        print(f"{p['id']:<10} | {p['nama']:<10} | {p['gender']:<8} | {p['penyakit']:<10}")
    print("=" * 50)

def menu_create():
    while True:
        print('''        
            \n---- Menu Create ----
            1. Tambah Data Pasien
            2. Kembali
        ''')
        choice = input("Pilih menu (1-2): ").strip()
        if choice == "1":
            while True:
                id_baru = input("Input ID Pasien: ").strip().upper()
                if caripasien(id_baru):
                    print("ID Pasien sudah terdaftar")
                else:
                    break
            
            nama = input("Input Nama: ").strip().capitalize()
            while True:
                gender = input("Input Gender (L/P): ").strip().upper()
                if gender.upper() == "L" or "P":
                    break
                else:
                    print ('Pilihan tidak valid')
                    again = input("Cari Lagi? (Y/N): ").strip()
                    if again != 'Y':
                        break
                break
            penyakit = input("Input Jenis Penyakit: ").strip().capitalize()
            
            pasien_baru = {"id": id_baru, "nama": nama, "gender": gender, "penyakit": penyakit}
            
            print("\nRingkasan Data:")
            print_table([pasien_baru])
            
            confirm = input("Simpan data? (Y/N): ").strip().upper()
            if confirm == 'Y':
                datapasien.append(pasien_baru)
                print("Data tersimpan.")
            elif confirm != 'Y' or confirm != 'N':
                print ('Pilihan tidak valid')
            else:
                print("Data batal disimpan.")
            pause()   
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")
            pause()

def menu_read():
    while True:
        print('''
            ----- Menu Read -----
            1. Tampilkan seluruh data pasien
            2. Tampilkan data pasien tertentu
            3. Kembali
        ''')        
        
        choice = input("Pilih menu (1-3): ").strip()
        
        if choice == "1":
            if not datapasien:
                print("Data pasien belum ada.")
                pause()
            else:
                print_table(datapasien)
                pause()
        elif choice == "2":
            while True:
                search_id = input("Input ID pasien yang dicari: ").strip()
                patient = caripasien(search_id)
                if patient:
                    print("\nDetail Pasien:")
                    print_table([patient])
                    pause()
                    break
                else:
                    print("ID pasien tidak ditemukan.")
                    again = input("Cari Lagi? (Y/N): ").strip().upper()
                    if again != 'Y':
                        break
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")
            pause()

def menu_update():
    while True:
        print('''
            --- Menu Update ---
            1. Ubah Data
            2. Kembali
        ''')
        
        choice = input("Pilih menu (1-2): ").strip()
        
        if choice == "1":
            while True:
                search_id = input("Input ID pasien yang dicari: ").strip()
                patient = caripasien(search_id)
                if not patient:
                    print("ID pasien tidak ditemukan.")
                    again = input("Cari Lagi? (Y/N): ").strip().upper()
                    if again != 'Y':
                        patient = None
                        break
                else:
                    break
            
            if not patient:
                continue
                
            print("\nData saat ini:")
            print_table([patient])
            
            cont = input("Lanjut update? (Y/N): ").strip().upper()
            if cont != 'Y':
                continue
                
            while True:
                ubah_data = input("Pilih item data yang akan diubah (nama/gender/penyakit): ").strip().lower()
                if ubah_data in ["nama", "gender", "penyakit"]:
                    break
                else:
                    print("Item data tidak valid")
                    pause()
            
            data_update = input(f"Input nilai baru untuk {ubah_data}: ").strip()
            
            # Show proposed changes
            temp_patient = patient.copy()
            temp_patient[ubah_data] = data_update
            print("\nPerubahan data:")
            print_table([temp_patient])
            
            confirm = input("Update data? (Y/N): ").strip().upper()
            if confirm == 'Y':
                patient[ubah_data] = data_update
                print("Update data berhasil.")
                print_table([patient])
            else:
                print("Update dibatalkan.")
            pause()

        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")
            pause()

def menu_delete():
    while True:
        print('''
                --- Menu Delete ---
                1. Hapus Data
                2. Kembali
            ''')
        
        choice = input("Pilih menu (1-2): ").strip()
        
        if choice == "1":
            while True:
                search_id = input("Input ID pasien: ").strip()
                patient = caripasien(search_id)
                
                if not patient:
                    print("ID pasien tidak ditemukan.")
                    again = input("Cari Lagi? (Y/N): ").strip().upper()
                    if again != 'Y':
                        patient = None
                        break
                else:
                    break
            
            if not patient:
                continue
                
            print("\nData yang akan dihapus:")
            print_table([patient])
            
            confirm = input("Hapus data? (Y/N): ").strip().upper()
            if confirm == 'Y':
                datapasien.remove(patient)
                print("Data terhapus.")
            else:
                print("Penghapusan dibatalkan.")
            pause()

        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")
            pause()

def main_menu():
    while True:
        print("\n" + "="*30)
        print("      MAIN MENU PASIEN")
        print("="*30)
        print("1. Report")
        print("2. Tambah")
        print("3. Ubah")
        print("4. Hapus")
        print("5. Exit")
        
        choice = input("Pilih menu (1-5): ").strip()
        
        if choice == "1":
            menu_read()
        elif choice == "2":
            menu_create()
        elif choice == "3":
            menu_update()
        elif choice == "4":
            menu_delete()
        elif choice == "5":
            print("Terima kasih!")
            break
        else:
            print("Option is not valid")

main_menu()
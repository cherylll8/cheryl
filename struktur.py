import csv
class Node:
    def __init__(self, nim, nama, prodi, ipk):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.ipk = ipk
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_mahasiswa(self, nim, nama, prodi, ipk):
        new_node = Node(nim, nama, prodi, ipk)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def cari_mahasiswa(self, nim):
        curr = self.head
        while curr:
            if curr.nim == nim:
                return curr
            curr = curr.next
        return None

    def edit_mahasiswa(self, nim, nama_baru, prodi_baru, ipk_baru):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa:
            mahasiswa.nama = nama_baru
            mahasiswa.prodi = prodi_baru
            mahasiswa.ipk = ipk_baru
            return True
        return False

    def hapus_mahasiswa(self, nim):
        curr = self.head
        prev = None
        while curr:
            if curr.nim == nim:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def tampilkan_semua(self):
        curr = self.head
        while curr:
            print(f"{curr.nim}, {curr.nama}, {curr.prodi}, {curr.ipk}")
            curr = curr.next

    def simpan_ke_csv(self, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['NIM', 'Nama', 'Prodi', 'IPK']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            curr = self.head
            while curr:
                writer.writerow({'NIM': curr.nim, 'Nama': curr.nama, 'Prodi': curr.prodi, 'IPK': curr.ipk})
                curr = curr.next
        print("Data berhasil disimpan ke file CSV.")

# Implementasi
linked_list = LinkedList()

# Menambahkan 3 data mahasiswa
linked_list.tambah_mahasiswa("111", "Ani", "Informatika", "3,5")
linked_list.tambah_mahasiswa("222", "Budi", "Sistem Informasi", "3,2")
linked_list.tambah_mahasiswa("333", "Citra", "Teknik Komputer", "3,8")

# Mencari mahasiswa berdasarkan NIM
hasil = linked_list.cari_mahasiswa("222")
if hasil:
    print(f"Ditemukan: {hasil.nim}, {hasil.nama}, {hasil.prodi}, {hasil.ipk}")
else:
    print("Data tidak ditemukan.")

# Mengedit data salah satu mahasiswa
linked_list.edit_mahasiswa("222", "Budi Santoso", "Sistem Informasi", "3,4")

# Menghapus salah satu mahasiswa
linked_list.hapus_mahasiswa("111")

# Menampilkan semua data
linked_list.tampilkan_semua()

# Memastikan data tersimpan di file CSV dengan benar
linked_list.simpan_ke_csv("data_mahasiswa.csv")

# Laporan Praktikum 2
Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu:  Agung Nugroho, S.Kom., M.Kom.,

Mata Kuliah: Bahasa Pemograman

# Latihan 1 Menentukan Nilai Akhir
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Latihan%201.drawio.png)

Penjelasan:
- 

# Latihan 2 Status Gaji Karyawan
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/latihan%202.drawio.png)

Penjelasan:
- 

# Latihan 3 Penggunaan Kondisi or
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Latihan%203%20kondisi%20or.drawio.png)

Penjelasan:
- 

# kasus 1 Program Pemesanan Tiket Bioskop

# kode python
```python
# Harga tiket
harga = {'reguler': 50000, 'vip': 100000}
diskon_member = 0.20  # 20%

# Input tipe tiket dan status member
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ")
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")

# Menghitung total harga
total_harga = harga.get(tipe_tiket) * (1 - diskon_member if status_member == "ya" else 1)

# Menampilkan total harga
print(f"Total harga yang harus dibayar: Rp{total_harga:,.0f}")
```
# flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Tiket%20Bioskop.drawio.png)

Penjelasan:
1. 

# kasus 2 program kalkulator sederhana

# kode python
```python
# Program Kalkulator Sederhana

angka1 = int(input("Masukkan angka pertama: "))
operasi_bilangan = input("Masukkan operasi bilangan (+, -, *, /): ")
angka2 = int(input("Masukkan angka kedua: "))

# Menentukan operasi berdasarkan operator yang dipilih
if operasi_bilangan == '+':
    hasil = angka1 + angka2
elif operasi_bilangan == '-':
    hasil = angka1 - angka2
elif operasi_bilangan== '*':
    hasil = angka1 * angka2
else:
    operasi_bilangan == '/'
    hasil = angka1 / angka2

print("Hasil: " + str(hasil))
```
# flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Kalkulator.drawio.png)

Penjelasan:
1. input angka pertama
  - Program meminta untuk memasukkan angka pertama. Fungsi input() digunakan untuk mengambil input dari pengguna, dan int() mengonversi input tersebut menjadi tipe data integer.
2. input operasi bilangan
  - Program meminta untuk memasukkan jenis operasi yang ingin dilakukan (penjumlahan, pengurangan, perkalian, atau pembagian). Input ini disimpan sebagai string.
3. input angka kedua
  - Program meminta untuk memasukkan angka kedua, yang juga diubah menjadi tipe data integer.
4. Menentukan operasi yang ingin digunakan
  -Program menggunakan struktur kontrol if-elif-else untuk menentukan operasi yang dipilih
  -Jika memilih + maka program akan menjumlahkan angka 1 dan angka 2
  -Jika memilih - maka program akan mengurangkan angka 1 dengan angka 2
  -Jika memilih * maka program akan mengalikan angka 1 dengan angka 2
  -Jika memilih / maka program akan membagi angka 1 dengan angka 2
5. Menampilkan Hasil
  -Program mencetak hasil dari operasi yang telah dilakukan. Fungsi str() digunakan untuk mengonversi hasil (yang berupa angka) menjadi string agar bisa digabungkan dengan teks lainnya. 

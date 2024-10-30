# Laporan Praktikum 2
Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu:  Agung Nugroho, S.Kom., M.Kom.,

Mata Kuliah: Bahasa Pemograman

# Latihan 1 Menentukan Nilai Akhir
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Latihan%201.drawio.png)
## Hasil eksekusi program
![foto](https://github.com/Manueljds2311105/foto/blob/fb7df9fb3391d172694e883dd6cb6895461c2b32/Latihan%201%20Menentukan%20nilai%20akhir.png)

Penjelasan:
1. input data
- Kode ini meminta untuk memasukkan beberapa data: nama, nilai UTS (Ujian Tengah Semester), nilai UAS (Ujian Akhir Semester), dan nilai Tugas. Semua input ini diambil dalam bentuk string menggunakan fungsi input().
2. menghitung nilai akhir
- Nilai akhir dihitung dengan rumus yang menggabungkan nilai tugas, UTS, dan UAS dengan bobot yang berbeda:

    Tugas memiliki bobot 20% (0.2)

    UTS memiliki bobot 40% (0.4)

    UAS juga memiliki bobot 40% (0.4)
- Fungsi int() digunakan untuk mengonversi nilai yang diinput dari string ke integer sebelum melakukan perhitungan.
python
3. Menentukan keterangan lulus atau tidak
- Keterangan lulus atau tidak ditentukan berdasarkan nilai akhir. Jika nilai akhir lebih besar dari 60, maka keterangan adalah "LULUS", jika tidak, keterangan adalah "TIDAK LULUS".
4. Menentukan nilai huruf
- Nilai huruf ditentukan berdasarkan rentang nilai akhir:

    A untuk nilai lebih dari 80

    B untuk nilai lebih dari 70

    C untuk nilai lebih dari 50

    D untuk nilai lebih dari 40

    E untuk nilai 40 ke bawah
- Struktur if-elif-else digunakan untuk menentukan huruf yang sesuai.
5. Menampilkan hasil
- Setelah semua perhitungan selesai, kode ini mencetak hasilnya, termasuk nama, nilai UTS, UAS, tugas, nilai akhir, nilai huruf, dan keterangan lulus atau tidak.
# Latihan 2 Status Gaji Karyawan
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/latihan%202.drawio.png)
## Hasil eksekusi program
![foto](https://github.com/Manueljds2311105/foto/blob/fb7df9fb3391d172694e883dd6cb6895461c2b32/Latihan%202%20Membuat%20Program%20Status%20Gaji%20Karyawan.png)

Penjelasan:
1. input gaji
- Kode ini meminta untuk memasukkan nilai gaji. Nilai yang dimasukkan akan diubah menjadi tipe data integer dan disimpan dalam variabel gaji.
2. input status keluarga
- Kode ini meminta untuk menjawab apakah sudah berkeluarga atau tidak dengan memasukkan "Y" (ya) atau "T" (tidak). Jika memasukkan "Y", maka berkeluarga akan bernilai True, jika tidak maka akan bernilai False
3. input status kepemilikan rumah
- Kode ini mirip dengan kode sebelumnya, tetapi kali ini menanyakan apakah memiliki rumah. Jika menjawab "Y", maka punya_rumah akan bernilai True, jika tidak akan bernilai False.
4. pemeriksaan gaji
- Kode ini memeriksa apakah gaji pengguna lebih besar dari 3.000.000. Jika ya, maka akan melanjutkan ke kode berikutnya.
5. pesan jika gaji diatas umr
- Jika gaji lebih dari 3.000.000, maka program akan mencetak bahwa gaji sudah di atas UMR.
6. pemeriksaan status keluarga dan asuransi
- Jika sudah berkeluarga (berkeluarga bernilai True), maka program akan menyarankan untuk ikut asuransi dan menabung untuk pensiun. Jika tidak, program akan mencetak bahwa tidak perlu ikut asuransi.
7. pemeriksaan status kepemilikan rumah
- Jika memiliki rumah (punya_rumah bernilai True), maka program akan mencetak bahwa wajib membayar pajak rumah. Jika tidak, program akan mencetak tidak wajib membayar pajak rumah.
8. pesan untuk gaji dibawah umr
- Jika gaji pengguna tidak lebih dari 3.000.000, maka program akan mencetak bahwa gaji belum mencapai UMR.
# Latihan 3 Penggunaan Kondisi or
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Latihan%203%20kondisi%20or.drawio.png)
## Hasil eksekusi program
![foto](https://github.com/Manueljds2311105/foto/blob/fb7df9fb3391d172694e883dd6cb6895461c2b32/Latihan%203%20penggunaan%20kondisi%20or.png)

Penjelasan:
1. input bilangan
- kode meminta untuk memasukkan tiga bilangan bulat. Fungsi input() digunakan untuk mengambil masukan dari pengguna, dan int() digunakan untuk mengonversi masukan tersebut dari string menjadi bilangan bulat. Bilangan yang dimasukkan disimpan dalam variabel a, b, dan c.
2. pemeriksaan kondisi
- pernyataan if yang memeriksa tiga kondisi menggunakan operator logika or.
- Kondisi yang diperiksa adalah:

    Apakah jumlah a dan b sama dengan c (a + b == c)

    Apakah jumlah a dan b sama dengan c (a + b == c)  

    Apakah jumlah c dan a sama dengan b (c + a == b)
3. output hasil
- Jika salah satu dari kondisi di atas terpenuhi, program akan mencetak "BENAR".
- Jika tidak ada kondisi yang terpenuhi, program akan mencetak "SALAH".
# kasus 1 Program Pemesanan Tiket Bioskop
## kode python
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
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Tiket%20Bioskop.drawio.png)
## Hasil eksekusi program
![foto](https://github.com/Manueljds2311105/foto/blob/fb7df9fb3391d172694e883dd6cb6895461c2b32/Tiket%20Bioskop.py.png)

Penjelasan:
1. Harga Tiket
- Di sini, sebuah dictionary bernama harga didefinisikan untuk menyimpan harga tiket berdasarkan tipe. Tipe tiket yang tersedia adalah 'reguler' dengan harga Rp50.000 dan 'vip' dengan   harga Rp100.000.
2. Diskon untuk member
- Variabel 'diskon_member' didefinisikan dengan nilai 0.20, yang berarti ada diskon sebesar 20% bagi pemegang kartu member.
3. Input tipe tiket dan status member
- Kode meminta input untuk menentukan tipe tiket yang ingin dibeli (apakah 'reguler' atau 'vip') dan juga menanyakan apakah memiliki kartu member atau tidak.
4. Menghitung Harga Tiket
- Di sini, total harga dihitung berdasarkan tipe tiket yang dipilih. 'Fungsi harga.get(tipe_tiket)' digunakan untuk mendapatkan harga tiket sesuai dengan tipe yang dimasukkan oleh pengguna. Jika pengguna memiliki kartu member '(status_member == "ya")', maka total harga akan dikalikan dengan (1 - diskon_member) untuk menerapkan diskon. Jika tidak, total harga tetap sama
5. Menampilkan total harga
- Terakhir, kode ini menampilkan total harga yang harus dibayar dalam format yang lebih mudah dibaca, yaitu dengan menambahkan pemisah ribuan dan tanpa desimal. Misalnya, jika total harga adalah Rp80.000, maka output akan ditampilkan sebagai "Total harga yang harus dibayar: Rp80.000".
# kasus 2 program kalkulator sederhana

## kode python
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
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/c5e53c201c0a249ff091ac5e38264feaafc56e8a/Kalkulator.drawio.png)
## Hasil eksekusi program
![foto](https://github.com/Manueljds2311105/foto/blob/fb7df9fb3391d172694e883dd6cb6895461c2b32/Kalkulator%20sederhana.py.png)

Penjelasan:
1. input angka pertama
  - Program meminta untuk memasukkan angka pertama. Fungsi input() digunakan untuk mengambil input dari pengguna, dan int() mengonversi input tersebut menjadi tipe data integer.
2. input operasi bilangan
  - Program meminta untuk memasukkan jenis operasi yang ingin dilakukan (penjumlahan, pengurangan, perkalian, atau pembagian). Input ini disimpan sebagai string.
3. input angka kedua
  - Program meminta untuk memasukkan angka kedua, yang juga diubah menjadi tipe data integer.
4. Menentukan operasi yang ingin digunakan
  - Program menggunakan struktur kontrol if-elif-else untuk menentukan operasi yang dipilih:

    Jika memilih + maka program akan menjumlahkan angka 1 dan angka 2

    Jika memilih - maka program akan mengurangkan angka 1 dengan angka 2

    Jika memilih * maka program akan mengalikan angka 1 dengan angka 2

    Jika memilih / maka program akan membagi angka 1 dengan angka 2
5. Menampilkan Hasil
  - Program mencetak hasil dari operasi yang telah dilakukan. Fungsi str() digunakan untuk mengonversi hasil (yang berupa angka) menjadi string agar bisa digabungkan dengan teks lainnya. 

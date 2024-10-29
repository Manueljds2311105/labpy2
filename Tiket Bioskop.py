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
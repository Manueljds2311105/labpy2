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
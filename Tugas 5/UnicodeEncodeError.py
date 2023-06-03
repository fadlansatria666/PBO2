text = "é"  # Teks Unicode dengan karakter yang tidak dapat dienkripsi

encoded_text = text.encode('ascii')  # Mengenkripsi teks menggunakan skema enkoding ASCII
print(encoded_text)

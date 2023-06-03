text = "Café"  # Teks Unicode dengan karakter yang tidak dapat diterjemahkan ke dalam format tujuan

try:
    encoded_text = text.encode('ascii')  # Menerjemahkan teks menggunakan skema enkoding ASCII
except UnicodeTranslateError as e:
    print(f"Terjadi kesalahan dalam mentranslasikan teks: {e}")

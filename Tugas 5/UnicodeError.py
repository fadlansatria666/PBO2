text = b'\xc3\xa9'  # Data byte dengan karakter yang tidak dapat didekode

try:
    decoded_text = text.decode('ascii')  # Mendekode data menggunakan skema enkoding ASCII
except UnicodeDecodeError as e:
    print(f"Terjadi kesalahan dalam mendekode teks: {e}")

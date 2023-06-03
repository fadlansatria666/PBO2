data = b'\xc3\xa9'  # Data byte dengan karakter yang tidak dapat didekode

decoded_data = data.decode('ascii')  # Mendekode data menggunakan skema enkoding ASCII
print(decoded_data)

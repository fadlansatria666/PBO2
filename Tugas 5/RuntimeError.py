try:
    raise RuntimeError("Terjadi kesalahan saat menjalankan program.")
except RuntimeError as e:
    print("Terjadi RuntimeError:", e)

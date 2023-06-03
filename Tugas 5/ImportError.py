try:
    import module_that_does_not_exist
except ImportError:
    print("Modul yang diminta tidak ditemukan.")

def number_generator():
    try:
        for i in range(5):
            yield i
    except GeneratorExit:
        print("Generator dihentikan sebelum selesai.")

gen = number_generator()

for num in gen:
    print(num)
    if num == 2:
        gen.close()

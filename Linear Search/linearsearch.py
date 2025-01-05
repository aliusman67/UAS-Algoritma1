print("""
Nama: Ali Usman
NIM: 241011400899
Kelas: 01TPLE011
""")

def linear_search(arr, target):
    checked_indices = []  # Untuk melacak indeks yang telah diperiksa
    steps = 0             # Menghitung jumlah langkah pencarian

    for index, value in enumerate(arr):
        checked_indices.append(index)  # Catat indeks yang sedang diperiksa
        steps += 1  # Tambahkan jumlah langkah
        print(f"Langkah {steps}: Memeriksa indeks {index} dengan nilai {value}")
        if value == target:
            # Jika target ditemukan
            print(f"Target {target} ditemukan pada indeks {index}")
            print(f"Indeks yang diperiksa: {checked_indices}")
            print(f"Total langkah: {steps}")
            return index
    
    # Jika target tidak ditemukan
    print(f"Target {target} tidak ditemukan. Indeks yang diperiksa: {checked_indices}")
    print(f"Total langkah: {steps}")
    return -1

# Contoh penggunaan
unsorted_array = [15, 3, 7, 10, 22, 8, 5, 2]
print("Array:", unsorted_array)
target_value = 10
linear_search(unsorted_array, target_value)

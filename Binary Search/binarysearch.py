print("""
Nama: Ali Usman
NIM: 241011400899
Kelas: 01TPLE011
    """)


def binary_search(arr, target, low=0, high=None, depth=0):
    if high is None:
        high = len(arr) - 1  # Tentukan batas atas array jika tidak diberikan
    
    if low > high:
        print(f"Depth {depth}: Target {target} tidak ditemukan.")
        return -1
    
    mid = (low + high) // 2  # Cari elemen tengah
    print(f"Depth {depth}: Memeriksa indeks {mid} dengan nilai {arr[mid]}")

    if arr[mid] == target:
        print(f"Depth {depth}: Target {target} ditemukan pada indeks {mid}")
        return mid
    elif arr[mid] > target:
        # Jika target lebih kecil dari elemen tengah, cari di sisi kiri
        return binary_search(arr, target, low, mid - 1, depth + 1)
    else:
        # Jika target lebih besar dari elemen tengah, cari di sisi kanan
        return binary_search(arr, target, mid + 1, high, depth + 1)

# Contoh penggunaan
sorted_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("Array:", sorted_array)
target_value = 11
binary_search(sorted_array, target_value)

print("""

Nama: ALi Usman
NIM: 241011400899
Kelas: 01TPLE011

""")


# Contoh data pesanan transportasi online
orders = [
    {"order_id": 1, "pickup": "A", "destination": "B", "order_time": "2023-01-02 14:30:00"},
    {"order_id": 2, "pickup": "C", "destination": "D", "order_time": "2023-01-02 12:15:00"},
    {"order_id": 3, "pickup": "E", "destination": "F", "order_time": "2023-01-02 15:45:00"},
    {"order_id": 4, "pickup": "G", "destination": "H", "order_time": "2023-01-02 14:30:00"},
    {"order_id": 5, "pickup": "I", "destination": "J", "order_time": "2023-01-02 10:00:00"},
]

# Import library untuk memproses waktu
from datetime import datetime

# Fungsi untuk mengonversi waktu pemesanan menjadi objek datetime
def convert_time(order):
    return datetime.strptime(order["order_time"], "%Y-%m-%d %H:%M:%S")

# Fungsi Merge Sort
def merge_sort(data, key_func):
    if len(data) <= 1:
        return data

    # Pisahkan data menjadi dua bagian
    mid = len(data) // 2
    left_half = merge_sort(data[:mid], key_func)
    right_half = merge_sort(data[mid:], key_func)

    # Gabungkan dua bagian yang telah diurutkan
    return merge(left_half, right_half, key_func)

def merge(left, right, key_func):
    sorted_data = []
    i = j = 0

    # Bandingkan elemen-elemen dari dua bagian
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            sorted_data.append(left[i])
            i += 1
        else:
            sorted_data.append(right[j])
            j += 1

    # Tambahkan elemen yang tersisa
    sorted_data.extend(left[i:])
    sorted_data.extend(right[j:])
    return sorted_data

# Urutkan data berdasarkan waktu pemesanan
sorted_orders = merge_sort(orders, key_func=convert_time)

# Tampilkan hasil
print("Data Pesanan Setelah Diurutkan Berdasarkan Waktu Pemesanan:")
for order in sorted_orders:
    print(order)

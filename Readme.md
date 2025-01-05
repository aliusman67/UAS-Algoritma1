# Membuat file README.md dengan konten di atas
readme_content = """
# **UAS Algoritma dan Pemrograman 1**

Proyek ini dibuat sebagai bagian dari Ujian Akhir Semester (UAS) mata kuliah **Algoritma dan Pemrograman 1**. Program ini mengimplementasikan **algoritma Merge Sort** untuk mengurutkan data pesanan transportasi online berdasarkan waktu pemesanan.

---

## **Deskripsi Proyek**

Perusahaan transportasi online membutuhkan sistem yang efisien untuk mengelola jutaan data pesanan. Data ini mencakup:
- **ID Pesanan**: Identitas unik setiap pesanan.
- **Lokasi Pengambilan**: Titik di mana pelanggan dijemput.
- **Lokasi Tujuan**: Titik tujuan perjalanan.
- **Waktu Pemesanan**: Waktu ketika pesanan dibuat.

Tantangan utama adalah mengurutkan data pesanan berdasarkan **waktu pemesanan** secara efisien untuk memprioritaskan layanan. Program ini menggunakan **algoritma Merge Sort**, yang sangat cocok untuk dataset besar karena stabilitas dan efisiensinya.

---

## **Fitur Program**
1. **Sorting Stabil**: Pesanan dengan waktu yang sama tetap mempertahankan urutan awalnya.
2. **Efisiensi Tinggi**:
   - Kompleksitas waktu: \\( O(n \\log n) \\), cocok untuk dataset besar.
3. **Fleksibilitas**:
   - Dapat digunakan untuk data lain dengan mengubah kunci pengurutan.

---

## **Teknologi yang Digunakan**
- **Bahasa Pemrograman**: Python 3.x
- **Library**:
  - `datetime`: Untuk memproses waktu dalam format tanggal.

---

## **Cara Menjalankan Program**

1. **Kloning Repository**:
   ```bash
   git clone https://github.com/aliusman67/UAS-Algoritma1
   cd repo-uas-algoritma

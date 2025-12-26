Deskripsi
Dashboard ini merupakan proyek akhir analisis data yang berfokus pada ekosistem e-commerce di Brazil menggunakan Dataset Olist. Proyek ini memberikan wawasan mendalam mengenai performa penjualan, kategori produk unggulan, dan demografi pelanggan.

Proyek ini menggunakan beberapa dataset yang saling terkait:
olist_customers_dataset.csv: Informasi data pelanggan.
olist_orders_dataset.csv: Detail transaksi pesanan.
olist_order_items_dataset.csv: Item yang terjual dalam setiap pesanan.
olist_products_dataset.csv: Katalog produk.
product_category_name_translation.csv: Terjemahan kategori produk ke Bahasa Inggris.
all_data.csv: Data hasil penggabungan (merge) untuk kebutuhan visualisasi dashboard.

Struktur Folder
dashboard.py: Script utama untuk menjalankan dashboard Streamlit.
notebook.ipynb: Proses pembersihan, eksplorasi, dan analisis data (EDA).
requirements.txt: Daftar library Python yang dibutuhkan.
data/: Folder berisi dataset mentah (CSV).

Cara Menjalankan Secara Lokal
Clone Repository
git clone https://github.com/username-anda/repository-anda.git
cd repository-anda
Instal Library Pastikan Anda berada di direktori proyek, lalu jalankan:
pip install -r requirements.txt
Jalankan Aplikasi
streamlit run dashboard.py

Ringkasan Insight
Kategori Terpopuler: Kategori bed_bath_table dan health_beauty mendominasi total pesanan.
Tren Penjualan: Dashboard menunjukkan pertumbuhan transaksi yang stabil selama periode operasional.
Pendapatan: Total pendapatan mencapai lebih dari R$ 20 juta

# Project-ordering-python
This project about learning ordering in python (In Indonesia)

Ordering adalah mengurutkan data berdasarkan alphabet, numerik atau tanggal(date). Data diurutkan sesuai alphabet menggunakan sqlalchemy dengan metode order_by().
Untuk kasus dengan tipe data string, maka itu berarti pengurutan berdasarkan alphabetic. Misalnya ketika kita menampilkan semua data di kolom state.
Misalkan kita ingin mengurutkan kolom states secara ascending, maka kita harus menambahkan kode program berikut: 
- stmt = select([census.columns.state])
- results = connection.execute(stmt).fetchall()
- print(results[:10])

Jika kita ingin mengurutkan dari yang terbesar ke yang terkecil, kita dapat menambahkan desc().
Order by Multiple:
- Pisahkan beberapa kolom dengan koma
- Order berada di kolom pertama
- Lalu jika ada duplikat di kolom pertama, order berada di kolom kedua
- Ulangi sampai semua kolom telah di order

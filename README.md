Nama : Georgius Satria Adibrata  

NPM : 2506589976

Kelas : PBP D

I Love Fasilkom UI Yayy!

### Tugas 1 ###

1. <section> digunakan untuk mengelompokkan konten yang topiknya sama jadi satu blok yg bermakna, dalam hal ini section hobi dan edukasi. Secara visual bisa pakai <div>, tapi bedanya ada di makna semantik. <div> tidak mempunyai arti apa-apa, cuma buat keperluan CSS. <section> juga bisa pakai ID untuk navigasi di navbar dan google juga lebih gampang paham struktur & hierarki konten website.

<article> digunakan karena setiap kartu (education entry/hobby entry) adalah konten yang bisa beridiri sendiri. Misalnya jika kartu UI dengan semua infonya (University of Indonesia, Undergraduate.....) di copas ke halaman lain sendirian, pasti masih make sense. Tidak butuh info dari kartu SMA Gonzaga atau SMP Theresia.

<aside> tidak digunakan disini karena <aside> khusus untuk konten sampingan yang bisa dihapus. Disini hanya ada konten utama yang tidak bisa dihapus karena tidak ada konten lain yang tersisa untuk section itu. 


2. Saya menemui tantangan letak pada list, dimana saya ingin bullet pointnya di sebelah kanan, bukan di sebelah kiri. Akhirnya saya memakai tanda bullet point dengan tag <p>, yang secara semantik salah tapi secara visual oke-oke aja.

Untuk tantangan tata letak di mobile, sepertinya sudah aman ketika dicek di F12 DevTools. Ini dikarenakan struktur dasar sudah pakai flexbox dengan flex-direction: column (bukan row yang bisa jadi aneh), makanya saya tidak menemukan tantangan besar pas di tes di mobile.


3. Batasannya adalah bahwa ketika harus menambah entri nantinya harus mengedit kode HTML lagi. Jadi selanjutnya saya ingin membuat form untuk nambah/edit entri portofolio. Lalu mungkin ditambahkan interaktivitas lebih, contohnya filter mencari hobi gaming saja, sorting, atau pencarian. Interaktivitas yang ada untuk sekarang hanya navbar saja.


----- AI Disclosure -----

Untuk tugas ini saya menggunakan AI, gemini untuk membuat kodenya dan debugging, dan Claude untuk debugging juga dan menjelaskan ke saya kode apa yg dipakai oleh gemini (dalam bentuk komen). Dan juga claude dipakai untuk membantu saya menjawab pertanyaan reflektif agar jawaban saya lebih mantap.

Keterbatasan AI kadang hanya ketidaktelitian, contohnya Claude saya kasih screenshot bahwa section hobby saya ada di kanan, tapi dia mikirnya ada di kiri. Sepertinya untuk Claude kelemahannya adalah image recognition.
Chat lognya ada disini (Claude): https://claude.ai/share/9518a87a-b61b-4460-98e5-da4bcb35e8c5

Untuk Gemini, sepertinya kelemahannya adalah jika diberikan data yang terlalu banyak, ada ketidaktelitiannya. 
Chat log Gemini: https://share.gemini.google/SlHQylKABmZz

Untuk pembuatan fitur darkmode, saya tidak memakai AI, hanya mentonon tutorial di YouTube



### Tugas 2 ###

1. urls.py proyek yang ada di folder portofolio menerima request awal dari browser dan mengopernya ke urls.py milik aplikasi, yang ada di folder main.

urls.py aplikasi menentukan view mana yang bertugas menanganinya.

views.py mengambil data daru model lalu mengirimkannya ke template

models.py berkomunikasi dengan database untuk mengambil isi data

template adalah struktur html yang merapihkan data untuk ditampilkan di browser pengguna.

2. Data tidak langsung ditulis di template agar lebih gampang menambahkan data baru. Jika ditulis mulu tiap kali menambahkan data, akan terlalu repot dan memakan banyak waktu. Kalo make django, akan gampang menambahkan data, tidak perlu menduplikasikan kode mulu.

3. makemigrations adalah command untuk mencatat rencana, jika ada perubahan di models.py maka disimpan ke file migrasi.

migrate adalah command untuk mengeksekusi rencanya, perubahan tersebut diterapkan langsung ke database.

AI Disclosure: Saya menggunakan gemini untuk ide tampilan skills page. Lalu saya gunakan untuk mengajarkan css agar tampilannya bisa sesuai dengan ide dia. 
Link chat gemini: https://share.gemini.google/fNsVL2AthVLH

Saya juga menggunaskan gemini untuk bantu menjawab pertanyaan refleksi.
Link chat gemini: https://share.gemini.google/rNJdf5AClrND

### Tugas 3 ###
1. Kita menggunakan model form karena: 
- Akan lebih gampang untuk menambahkan field-fieldnya lagi, jadi gausah dihardcode satu per satu di html. 
- Validasi dilakukan secara otomatis secara tipe data di models.py
- Data langsung masuk ke database
- Input aman dari data berbahaya seperti serangan SQL injection atau cross site scripting
- Jika input gak valid, akan langsung disampaikan pesan eror ke pengguna

Wajib menambahkan csrf_token karena tanpanya, situs web yg berbahaya bisa menggunakan status login (session/cookies) pengguna yg sedang aktif untuk mengirimkan request jahat seperti ganti kata sandi atau menghapus data tanpa pengetahuan pengguna.

2. JSON lebih disukai karena:
- Ukuran filenya lebih kecil
- Native dengan java script sehingga parsing lebih cepet
- Struktur key-value dan array yg sederhana
- Gampang dibaca oleh manusia

3. Alur fungsi view:
- Client mengirimkan request 
- Fungsi view di django menerima request terus ngambil data dari database
- Serialization, data dari json diubah menjadi tipe data python standar
- Data hasil serialisasi dibungkus ke dalam objek
- Response, django mengirimkan string json tersebut kembali ke client untuk diolah di front end

Kita perlu proses serialization karena alasan ketidakcocokan tipe data:
- Bentuk data django harus diubah karena tidak dipahami oleh web browser atau bahasa pemograman lain
- Bentuk data json adalah teks berbasis string murni yg ketat dan hanya mendukung tipe data dasar
- Serialization ini menerjemahkan data dari Django (QuerySet) dan mengestrak nilai2nya menjadi struktur data dasar python (dict/list) yang kemudian bisa diubah ke json secara aman. 


AI Disclosure:
Saya menggunakan AI untuk membantu penulisan kode, dan untuk mengetahui sintaks dan struktur dari form data delivery. Dan untuk membantu menjawab pertanyaan refleksi. 

Chat log Gemini: maap sepertinya tenggelem, kmrn lupa ngisi 😭😭

### Tugas 4 ###

Saya menggunakan claude untuk membantu memperjelas alur kerja dan untuk debugging.
Chat Log: https://claude.ai/share/253c889d-e340-446e-a077-1c1241bdc080

### Tugas 5 ###
Pertanyaan reflektif:
1. Untuk menejelaskan kenapa teknik ini penting, kita bayangkan apa yang terjadi jika kita tidak memakai debouncing. Misal kita mengetik kata "Laptop" di kolom pencarian. 
L --> Kirim request "L"
a --> Kirim request "a"
.... dan seterusnya, itu ada 6 kali pencarian.

Debouncing digunakan untuk menghindari hal ini, jadi dia menunggu user selesai ngetik, baru dikirim request-nya. Sistem akan menunggu jeda waktu yang singkat (misalnya sekitar 300-500 ms) setelah tombol terakhir ditekan. Lalu jika ada tombol yang ditekan lagi dalam kurun waktu singkat tersebut, timer diulang dari 0.

Hasilnya jika setiap tombol diketik sebelum jeda waktu 300-500 ms itu, server tidak akan mengirim request, lalu jika usernya sudah selesai ngetik, baru server mengirim request, jadi total hanya satu request saja. 

Ini penting karena beberapa poin:
- Hemat beban server dan database: Kalo ada ribuan2 pengguna yg memakai website ini, server dapat menerima puluhan ribu request dalam waktu yg sama, dan ini sangat membebani server. 

- Mencegah race condition: Bisa saja pencarian huruf lebih awal butuh waktu yg lebih lama daripada pencarian huruf setelahnya. Misal kita search 'laptop', kan harus kyk melalui kata 'lap' dulu ya, bisa jadi pencarian 'lap' ini baru selesainya lama, lebih lama daripada pencarian laptop. Hasilnya yang keluar malah pencarian 'lap'. Ini akan membuat user bingung.

- Menghemat kuota dan baterai pengguna: Mengirim terlalu banyak request menguras batere dan kuota

- Aplikasi lebih smooth: Karena browser gk ngirim terlalu banyak request dalam kurun waktu singkat, maka tampilannya gak akan patah-patah (ngelag)

2. Jadi keyword await ini menyuruh JavaScript menunggu sampai proses pengambilan data dari server sudah selesai, baru secara otomatis dia mengubah bentuk Promise menjadi data balasan (Response) yang asli.

Jika kita tidak pakai await, kode akan langsung dijalankan tanpa menunggu proses pengambilan data selesai. Akibatnya variabelnya bukan data dari server, tapi objek Promise yang masih pending. Lalu malah dapet eror seperti TypeError: Cannot read properties of undefined (tidak bisa membaca data) karena memangh datanya belom ada.

3. XSS adalah serangan dari peretas dimana peretas menyisipkan kode JavaScript jahat ke situs web agar berjalan otomatis di browser pengguna lain (misalnya utk mencuri cookie atau session).

- Django template lebih aman karena dia secara otomatis melakukan auto escaping pada sintaks {{ data }}. Karakter2 berbahaya seperti <script> diubah menjadi teks murni sehingga tidak dijalankan browser.

- AJAX/JavaScript tidak mempunyai proteksi otomatis, kalo masukkin kode menggunakan metode yg membaca HTML seperti innerHTML atau .html, browser akan merender dan mengeksekusi kode javascript jahat secara langsung.


AI Disclosure:
Dalam tugas ini, saya kebanyakan copy paste dari tutorial, lalu diganti saja contextnya sesuai bagian portofolio yang saya bikin. Namun jika kode terlalu besar atau masih ada masalah ketika saya coba ganti contextnya, saya pakai AI untuk membantu. Saya juga memakai AI untuk debugging error dan untuk menjelaskan pertanyaan reflektif.



Chat Log:

Gemini: https://gemini.google.com/share/d/18uLghTQA4_N8pNEYrR5WrwGvRWteFOQT?usp=sharing
Claude: https://claude.ai/share/6021e8a6-7d56-4d2f-8a14-93a03ff2c89e
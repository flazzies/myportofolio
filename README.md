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
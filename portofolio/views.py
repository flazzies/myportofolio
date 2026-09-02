from django.shortcuts import render #import from library

#Jika ada pengunjung (request), fungsi mengambil 
#file tampilan bernama index.html, terus di render (disajikan ke browser pengunjung)
def landing_page(request): 
    return render(request, "index.html")
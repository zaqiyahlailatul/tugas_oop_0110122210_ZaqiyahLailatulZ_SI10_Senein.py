from gempa import Gempa
Gempa_pertama = Gempa('Banten', 1.2)
Gempa_kedua = Gempa('Palu', 6.1)
Gempa_ketiga = Gempa('Cianjur', 5.6)
Gempa_keempat = Gempa('Jayapura', 3.3)
Gempa_kelima = Gempa('Garut', 4.0)

Gempa_pertama.Dampak()
Gempa_kedua.Dampak()
Gempa_ketiga.Dampak()
Gempa_keempat.Dampak()
Gempa_kelima.Dampak()

print(Gempa.GEMPA,
    "\n---------------------")
Gempa_pertama.cetak()
Gempa_kedua.cetak()
Gempa_ketiga.cetak()
Gempa_keempat.cetak()
Gempa_kelima.cetak()
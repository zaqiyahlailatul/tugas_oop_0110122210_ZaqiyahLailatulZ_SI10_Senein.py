class Gempa :
    # Variable data
    lokasi = ''
    skala = ''
    GEMPA = "Dampak dari terjadinya Gempa"

    # Method 
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        self.dampak = ""
    def Dampak(self):
        if (self.skala <= 2):
            self.dampak = "Tidak terasa"
        elif (self.skala >= 2 and self.skala < 4):
            self.dampak = "Bangunan retak-retak"
        elif (self.skala >= 4 and self.skala <6):
            self.dampak = "Bangunan roboh"
        else :
            self.dampak = "Bangunan roboh dan berpotensi tsunami"


    def cetak(self):
        print(
            '\n======================='
            '\nLokasi\t\t: ', self.lokasi,
            '\nSkala\t\t: ', self.skala,
            '\nDampak Gempa\t ', self.dampak,
            '\n----------------------------'
        )




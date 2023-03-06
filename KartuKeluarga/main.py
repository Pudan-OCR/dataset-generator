from PIL import Image, ImageFont, ImageDraw, ImageOps
from faker import Faker
from random import randint
import random
from datetime import datetime

posK = (2960, 32)
posNo = (1470,215)
posNKK = (715,317)
posAlamat = (715,375)
posRTRW = (715,433)
posDK = (715,491)
posKec = (2615,326)
posKab = (2615,380)
#posKP = (2615,442)
posKP = (2615,432)
posProv = (2615,478)
posTanggal = (730,1988)
posTTD = (1610,2241)
posName = [(210,715),(210,765),(210,815),(210,865),(210,915),(211,965),(211,1015),(211,1065),(212,1115),(212,1165)]
posNIK = [(1069,710),(1069,760),(1069,810),(1069,860),(1069,910),(1070,960),(1070,1010),(1070,1060),(1071,1110),(1071,1160)]
posJK = [(1365, 710),(1365,760),(1365,810),(1365,860),(1365,910),(1366,960),(1366,1010),(1366,1060),(1367,1110),(1367,1160)]
posTemLah = [(1565,709),(1565,759),(1565,809),(1566,859),(1566,909),(1566,959),(1567,1009),(1567,1059),(1568,1109),(1568,1159)]
posTanLah = [(1973,706),(1973,756),(1973,806),(1974,856),(1974,906),(1974,956),(1975,1006),(1975,1056),(1976,1106),(1976,1156)]
posAgama = [(2143,705),(2143,755),(2143,805),(2144,855),(2144,905),(2144,955),(2145,1005),(2145,1055),(2146,1105),(2146,1155)]
posPendidikan = [(2370,703),(2370,753),(2370,803),(2371,853),(2371,903),(2371,953),(2372,1003),(2372,1053),(2373,1103),(2373,1153)]
posJePek = [(2870,701),(2870,751),(2870,801),(2871,851),(2871,901),(2871,951),(2872,1001),(2872,1051),(2873,1101),(2873,1151)]
posStatPer = [(215,1400),(215,1450),(215,1500),(216,1550),(216,1600),(216,1650),(217,1700),(217,1750),(218,1800),(218,1850)]
posSHDK = [(530,1398),(530,1448),(530,1498),(531,1548),(531,1598),(531,1648),(532,1698),(532,1748),(533,1798),(533,1848)]
posKew = [(925,1396),(925,1446),(925,1496),(926,1546),(926,1596),(926,1646),(927,1696),(927,1746),(928,1796),(928,1846)]
posNoPas = [(1295,1394),(1295,1444),(1295,1494),(1296,1544),(1296,1594),(1296,1644),(1297,1694),(1297,1744),(1298,1794),(1298,1844)]
posNoKit = [(1697,1392),(1697,1442),(1697,1492),(1698,1542),(1698,1592),(1698,1642),(1699,1692),(1699,1742),(1700,1792),(1700,1842)]
posAyah = [(2099,1390),(2099,1440),(2099,1490),(2100,1540),(2100,1590),(2100,1640),(2101,1690),(2101,1740),(2102,1790),(2102,1840)]
posIbu = [(2817,1386),(2817,1436),(2817,1486),(2818,1536),(2818,1586),(2818,1636),(2819,1686),(2819,1736),(2820,1786),(2820,1836)]

faker = Faker('id_ID')
fakerLuar = Faker()


def kDrawer(draw,xy,nama):
    font = ImageFont.truetype("Lexend-Light.ttf", 60)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=2)
    return draw
def noDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 83)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=2)
    return draw
def nkkDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 37)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def locDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 37)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def tanggalDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 42)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def ttdDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 42)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def namaDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def nikDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def jkDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def temlahDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def tanlahDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def agamaDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def pendidikanDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def jepekDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def statperDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def shdkDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def kewDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def nopasDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def nokitDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def ayahDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw
def ibuDrawer(draw,xy,nama):
    font = ImageFont.truetype("arial.ttf", 29)
    draw.text(xy, nama, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
    return draw

def main():
    jenisKelamin = ['LAKI-LAKI','PEREMPUAN']
    agama = ['KRISTEN','KATOLIK','ISLAM','HINDU','BUDDHA','KONGHUCU']
    statusPerkawinan = ['KAWIN','BELUM KAWIN']
    statusHubungan = ['KEPALA KELUARGA', 'ISTRI', 'ANAK']
    pendidikan = ['TIDAK/BELUM SEKOLAH','TAMAT SD/SEDERAJAT','SLTP/SEDERAJAT','SLTA/SEDERAJAT','D-I/D-II','D-IV/STRATA I','STRATA II','STRATA III','BELUM TAMAT SD/SEDERAJAT','AKADEMI/DIPLOMA III/S. MUDA']
    pekerjaan2 = ['PEGAWAI NEGERI SIPIL','PEGAWAI NEGERI SIPIL (PNS)','BELUM/TIDAK BEKERJA','WIRASWASTA','PETANI/PEKEBUN', 'NELAYAN/PERIKANAN']
    pekerjaan = ['PEGAWAI NEGERI SIPIL','PELAJAR/MAHASISWA','PEGAWAI NEGERI SIPIL (PNS)','BELUM/TIDAK BEKERJA','WIRASWASTA','PETANI/PEKEBUN', 'NELAYAN/PERIKANAN']
    kewarganegaraan = ['WNI','WNA']
    abjat = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y','Z']
    base = Image.open('kk_cleanup(2).jpg')
    txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    nPerson = randint(1,10)
    print(nPerson)
    noKK = ''
    for i in range(16):
        noKK += str(randint(0,9))

    #----------INI LOGIC----------
    #inisialisasi info kk
    tNo = ''
    tNamaKepalaKeluarga = ''
    tAlamat = ''
    tRTRW = ''
    tDesaKelurahan = ''
    tKecamatan = ''
    tKabupatenKota = ''
    tKodePos = ''
    tProvinsi = ''
    tDikeluarkanTanggal = ''

    #inisialisasi tabel
    tNama = [0 for i in range(nPerson)]
    tNik = [0 for i in range(nPerson)]
    tJenisKelamin = [0 for i in range(nPerson)]
    tTempatLahir = [0 for i in range(nPerson)]
    tTanggalLahir = [0 for i in range(nPerson)]
    tAgama = [0 for i in range(nPerson)]
    tPendidikan = [0 for i in range(nPerson)]
    tJenisPekerjaan = [0 for i in range(nPerson)]
    tStatusPerkawinan = [0 for i in range(nPerson)]
    tStatusHubungan = [0 for i in range(nPerson)]
    tKewarganegaraan = [0 for i in range(nPerson)]
    tNoPaspor = [0 for i in range(nPerson)]
    tNoKitas = [0 for i in range(nPerson)]
    tAyah = [0 for i in range(nPerson)]
    tIbu = [0 for i in range(nPerson)]
    tNamaIstri = []
    tNamaAyah = ''
    specialCase = False

    # Khusus jika 1 orang
    if(nPerson == 1):
        tStatusHubungan[0] = "KEPALA KELUARGA"
        tJenisKelamin[0] = random.choice(jenisKelamin)
        tKewarganegaraan[0] = "WNI"
        tAgama[0] = random.choice(agama)
        tPendidikan[0] = random.choice(pendidikan)
        if(tPendidikan[0]=="TIDAK/BELUM SEKOLAH"):
            tJenisPekerjaan[0] = random.choice(pekerjaan2)
        else:
            tJenisPekerjaan[0] = random.choice(pekerjaan)
        tStatusPerkawinan[0] = "BELUM KAWIN"
        if(tKewarganegaraan[0]=="WNI"):
            if(tJenisKelamin[0]=="LAKI-LAKI"):
                tNama[0] = faker.name_male().upper()
            else:
                tNama[0] = faker.name_female().upper()
        else:
            if(tJenisKelamin[0]=="LAKI-LAKI"): 
                tNama[0] = fakerLuar.name_male().upper()
            else:
                tNama[0] = fakerLuar.name_female().upper()
        tNamaKepalaKeluarga = tNama[0]
        tTanggalLahir[0] = faker.date('%d-%m-%Y')
        keyAwal = ''
        keyAkhir = ''
        for i in range(6):
            keyAwal += str(randint(0,9))
            if (i<4):
                keyAkhir += str(randint(0,9))
        tNo = keyAwal
        for i in range(10):
            tNo += str(randint(0,9))
        if(tJenisKelamin[0] == "LAKI-LAKI"):
            temp = str(tTanggalLahir[i])
            temp = temp.replace('-','',2)
            temp = temp[:4] +temp[6:]
            tNik[0] = keyAwal + temp + keyAkhir
        else:
            temp = str(tTanggalLahir[0])
            temp = temp.replace('-','',2)
            temp = temp[:4] +temp[6:]
            temp2 = str(int(temp[:2]) + 40)
            temp = temp2 + temp[2:]
            tNik[0] = keyAwal + temp + keyAkhir
        if(tKewarganegaraan[0] == "WNI"):
            tTempatLahir[0] = faker.city()

        else:
            tTempatLahir[0] = fakerLuar.city()
            noKitas = str(randint(0,9)) + random.choice(abjat)
            for j in range(2):
                noKitas += str(randint(0,9))
            noKitas+=random.choice(abjat)
            for j in range(5):
                noKitas += str(randint(0,9))
            noKitas += '-' + random.choice(abjat)
            tNoKitas[0] = noKitas
            noPaspor = random.choice(abjat)
            for j in range(7):
                noPaspor += str(randint(0,9))
            tNoPaspor[0] = noPaspor

    #-------------khusus----------------------------------------------------------------------------
    else:


    # Penentuan Status Hubungan Dalam Keluarga (Hirarki)

    # Orang pertama pastilah kepala keluarga
    # selainnya adalah istri dan anak (jika ada)
    
        tStatusHubungan[0] = "KEPALA KELUARGA"

        #Tentukan jumlah istri
        findNIstri = randint(0,11)
        nIstri = 1                                  # 41,6% kemungkinan beristri 1
        if(findNIstri==11 and (nPerson-1)>=4):       # 8,3% kemungkinan beristri 4
            nIstri = 4
        elif(findNIstri>8 and (nPerson-1)>=3):    # 16,6% kemungkinan beristri 3
            nIstri = 3
        elif(findNIstri>5 and (nPerson-1)>=2):    # 24,9% kemungkinan beristri 2
            nIstri = 2
        elif(findNIstri == 0):                   # 8,3% kemungkinan tidak memiliki istri(cerai)
            nIstri = 0

        if(nIstri != 0):
            for i in range(nIstri):
                tStatusHubungan[i+1] = "ISTRI"

        nAnak = nPerson-(nIstri+1)
        if(nAnak>0):
            for i in range(nAnak):
                tStatusHubungan[i+1+nIstri] = "ANAK"
    
    #-----------------------HIRARKI-----------------------------

    # Penentuan Jenis Kelamin (JK)
        tJenisKelamin[0] = "LAKI-LAKI"
        for i in range(nPerson-1):
            if (tStatusHubungan[i+1] == "ISTRI"):               # Istri pasti perempuan (ini indonesia)
                tJenisKelamin[i+1] = "PEREMPUAN"
            else:
                tJenisKelamin[i+1] = random.choice(jenisKelamin)

    #-------------------------JK-------------------------------

    # Penentuan Kewarganegaraan (Kew)
        tKewarganegaraan[0] = "WNI"
        suamiAsing = randint(1,100) == 6                             # 1% kemungkinan suaminya orang asing
        specialCase = suamiAsing
        if(suamiAsing):
            tJenisKelamin[0] = "PEREMPUAN"
            tJenisKelamin[1] = "LAKI-LAKI"
            tStatusHubungan[1] = "SUAMI"        
            tKewarganegaraan[1] = "WNA"                               
            for i in range(nPerson-2):
                tKewarganegaraan[i+2] = "WNI"
        else:
            for i in range(nPerson-1):
                if(tStatusHubungan[i+1] == "ISTRI" and (randint(1,10) == 10)):   # 10% kemungkinan si istri merupakan WNA
                    tKewarganegaraan[i+1] = "WNA"                               
                else:
                    tKewarganegaraan[i+1] = "WNI"                   # sang anak pasti (90%) WNI karena tinggal di kampung

    #------------------------KEW-------------------------------


    # Penentuan Agama

        whatAgama = randint(1,10)
    # 50% memiliki agama yang sama 1 keluarga
        if(whatAgama<=5):
            chooseAgama = random.choice(agama)
            for i in range(nPerson):
                tAgama[i] = chooseAgama
    # 30% sisanya setidaknya orang tuanya memiliki agama yang sama 
        elif (whatAgama<=8):
            chooseParentAgama = random.choice(agama)
            for i in range(nPerson):
                if(tStatusHubungan[i] != "ANAK"):
                    tAgama[i] = chooseParentAgama
                else:
                    #50-50 ngikut ortu
                    if(randint(1,2) == 1):
                        tAgama[i] = chooseParentAgama
                    else:
                        tAgama[i] = random.choice(agama)
    # Sisanya pure random karena aja
        else:
            for i in range(nPerson):
                tAgama[i] = random.choice(agama)

    #--------------------AGAMA---------------------------


    # Penentuan pendidikan

    #  pendidikan beragam tanpa aturan karena memang kenyataannya begitu
        for i in range(nPerson):
            tPendidikan[i] = random.choice(pendidikan)

    #-------------PENDIDIKAN-------------------


    # Penentuan Jenis Pekerjaan

        for i in range(nPerson):
            if(tPendidikan[i]=="TIDAK/BELUM SEKOLAH"):
                tJenisPekerjaan[i] = random.choice(pekerjaan2)
            else:
                tJenisPekerjaan[i] = random.choice(pekerjaan)

    #------------------JEPEK--------------------

    # Penentuan Status Perkawinan

    # Random, untuk anak, pasti untuk ortu
        for i in range(nPerson):
            if(tStatusHubungan[i]=="KEPALA KELUARGA" or tStatusHubungan[i]=="ISTRI"):
                tStatusPerkawinan[i] = "KAWIN"
            else:
                tStatusPerkawinan[i] = random.choice(statusPerkawinan)



    #-------------StatPer------------------------

    # Penentuan nama

        for i in range(nPerson):
            if(tKewarganegaraan[i]=="WNI"):
                if(tJenisKelamin[i]=="LAKI-LAKI"):
                    tNama[i] = faker.name_male().upper()
                else:
                    tNama[i] = faker.name_female().upper()
            else:
                if(tJenisKelamin[i]=="LAKI-LAKI"): 
                    tNama[i] = fakerLuar.name_male().upper()
                else:
                    tNama[i] = fakerLuar.name_female().upper()

            if(tStatusHubungan[i]=="ISTRI"):
                tNamaIstri.append(tNama[i])
            elif(tStatusHubungan[i]=="KEPALA KELUARGA" and specialCase):
                tNamaIstri.append(tNama[i])
                tNamaKepalaKeluarga = tNama[i]
            elif(tStatusHubungan[i]=="KEPALA KELUARGA" and not specialCase):
                tNamaAyah = tNama[i]
                tNamaKepalaKeluarga = tNama[i]

    #-------------------NAMA--------------------

    # Penentuan tanggal lahir

        for i in range(nPerson):
            tTanggalLahir[i] = faker.date('%d-%m-%Y')
        tTanggalLahir.append(faker.date('%d-%m-%Y'))
        tTanggalLahir.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
        tDikeluarkanTanggal = tTanggalLahir[nPerson]
        tTanggalLahir.pop()

    #-----------------TANLAH-------------------


    # Penentuan NIK

        keyAwal = ''
        keyAkhir = ''
        for i in range(6):
            keyAwal += str(randint(0,9))
            if (i<4):
                keyAkhir += str(randint(0,9))

        for i in range(nPerson):
            if(tJenisKelamin[i] == "LAKI-LAKI"):
                temp = str(tTanggalLahir[i])
                temp = temp.replace('-','',2)
                temp = temp[:4] +temp[6:]
                tNik[i] = keyAwal + temp + keyAkhir
            else:
                temp = str(tTanggalLahir[i])
                temp = temp.replace('-','',2)
                temp = temp[:4] +temp[6:]
                temp2 = str(int(temp[:2]) + 40)
                temp = temp2 + temp[2:]
                tNik[i] = keyAwal + temp + keyAkhir
        # No KK nya
        tNo = keyAwal
        for i in range(10):
            tNo += str(randint(0,9))

    #----------------NIK-------------------


    # Penentuan Tempat Lahir

        for i in range(nPerson):
            if(tKewarganegaraan[i] == "WNI"):
                tTempatLahir[i] = faker.city().upper()
            else:
                tTempatLahir[i] = fakerLuar.city().upper()


    #-------------------TEMLAH-----------------------

    # Penentuan noKitas

    # 1-2-5
        for i in range(nPerson):
            if(tKewarganegaraan[i]=="WNA"):
                noKitas = str(randint(0,9)) + random.choice(abjat)
                for j in range(2):
                    noKitas += str(randint(0,9))
                noKitas+=random.choice(abjat)
                for j in range(5):
                    noKitas += str(randint(0,9))
                noKitas += '-' + random.choice(abjat)
                tNoKitas[i] = noKitas
                noPaspor = random.choice(abjat)
                for j in range(7):
                    noPaspor += str(randint(0,9))
                tNoPaspor[i] = noPaspor


    #-------------------KITAS------------------------

    # Penentuan Nama Ortu
        for i in range(nPerson):
            if(tStatusHubungan[i] == "ANAK"):
                tAyah[i] = tNamaAyah
                tIbu[i] = random.choice(tNamaIstri)
            else:
                if(tKewarganegaraan[i] == "WNI"):
                    tAyah[i] = faker.name_male().upper()
                    tIbu[i] = faker.name_female().upper()
                else:
                    tAyah[i] = fakerLuar.name_male().upper()
                    tIbu[i] = fakerLuar.name_female().upper()

    #------------------ORTU------------------------------


    # Mengisi detail info kk (bagian atas kk)
    tProvinsi = faker.state().upper()
    tKodePos = str(faker.postcode())
    tKabupatenKota = faker.city().upper()
    tKecamatan = faker.city().upper()
    tDesaKelurahan = faker.city().upper()

    haveRTRW = randint(1,10) > 7
    if(haveRTRW):
        tRTRW = str(randint(0,1)) + str(randint(0,9)) + '/' + str(randint(0,1)) + str(randint(0,9))
    else:
        tRTRW = "-/-"

    tAlamat = faker.street_address().upper()

    #----------------------------------------------------------------------------------------------------------------
    draw = noDrawer(draw,posNo,tNo)
    draw = locDrawer(draw,posAlamat,tAlamat)
    draw = locDrawer(draw,posRTRW,tRTRW)
    draw = locDrawer(draw,posDK,tDesaKelurahan)
    draw = locDrawer(draw,posKec,tKecamatan)
    draw = locDrawer(draw,posKab,tKabupatenKota)
    draw = locDrawer(draw,posKP,tKodePos)
    draw = locDrawer(draw,posProv,tProvinsi)
    draw = nkkDrawer(draw,posNKK,tNamaKepalaKeluarga)
    draw = ttdDrawer(draw,posTTD,tNamaKepalaKeluarga)
    for i in range(nPerson):
        draw = namaDrawer(draw,posName[i],tNama[i])
       
        draw = nikDrawer(draw,posNIK[i],tNik[i])
        
        draw = jkDrawer(draw,posJK[i],tJenisKelamin[i])

        draw = temlahDrawer(draw,posTemLah[i],tTempatLahir[i])
        
        draw = tanlahDrawer(draw,posTanLah[i],tTanggalLahir[i])

        draw = agamaDrawer(draw,posAgama[i],tAgama[i])

        draw = pendidikanDrawer(draw,posPendidikan[i],tPendidikan[i])

        draw = jepekDrawer(draw,posJePek[i],tJenisPekerjaan[i])

        draw = statperDrawer(draw,posStatPer[i],tStatusPerkawinan[i])

        draw = shdkDrawer(draw,posSHDK[i],tStatusHubungan[i])

        draw = kewDrawer(draw,posKew[i],tKewarganegaraan[i])

        if(tNoPaspor[i] != 0):
            draw = nopasDrawer(draw,posNoPas[i],tNoPaspor[i])
            draw = nokitDrawer(draw,posNoKit[i],tNoKitas[i])

        if(nPerson != 1):
            draw = ayahDrawer(draw,posAyah[i],tAyah[i])

            draw = ibuDrawer(draw,posIbu[i],tIbu[i])

    draw = tanggalDrawer(draw,posTanggal,tDikeluarkanTanggal)

    out = Image.alpha_composite(base, txt_layer)
    out.show()
    out = out.save("1.png")

#print(faker.address())
main()

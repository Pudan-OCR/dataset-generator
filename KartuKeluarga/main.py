from PIL import Image, ImageFont, ImageDraw, ImageFilter
from faker import Faker
from random import randint
import random
from datetime import datetime


import math

def rotate_dot(x, y, angle):
    # Convert angle to radians
    angle_rad = math.radians(angle)

    # Calculate the sine and cosine of the angle
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)

    # Perform the rotation transformation
    new_x = x * cos_angle - y * sin_angle
    new_y = x * sin_angle + y * cos_angle

    return new_x, new_y

    



def createKKOnly(path):
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

    listBoundingBox = [[(1115,70), (2520,60),(2520, 190), (1115,200), "KARTU KELUARGA"],  
                    [(262,305), (670,305),(670,355), (262,355), "Nama Kepala Keluarga"],
                    [(262,365), (400,365),(400,415), (262,415), "Alamat"],
                    [(261,422), (402,422),(402,471), (261,471), "RT/RW"],
                    [(262, 484), (546, 484),(546, 529), (262, 529), "Desa/Kelurahan"],
                    [(2284, 318), (2485, 318), (2485, 360), (2284, 360), "Kecamatan"],
                    [(2284, 370), (2572, 370), (2572, 419), (2284, 419), "Kabupaten/Kota"],
                    [(2284, 419), (2467, 419), (2467, 467), (2284, 467), "Kode Pos"],
                    [(2284, 471), (2435, 471), (2435, 519), (2284, 519), "Provinsi"],
                    [(483, 581), (758, 581), (758, 630), (483, 630), "Nama Lengkap"],
                    [(585, 650), (655, 650), (655, 699), (585, 699), "(1)"],
                    [(1156, 574), (1240, 574), (1240, 626), (1156, 626), "NIK"],
                    [(1164, 650), (1235, 650), (1235, 696), (1164, 696), "(2)"],
                    [(1399, 554), (1519, 554), (1519, 602), (1399, 602), "Jenis"],
                    [(1420, 650), (1496, 650), (1496, 694), (1420, 694), "(3)"],
                    [(1726, 649), (1792, 649), (1792, 692), (1726, 692), "(4)"],
                    [(2015, 648), (2081, 648), (2081, 689), (2015, 689), "(5)"],
                    [(2217, 647), (2279, 647), (2279, 688), (2217, 688), "(6)"],
                    [(2580, 644), (2645, 644), (2645, 684), (2580, 684), "(7)"],
                    [(3140, 642), (3203, 642), (3203, 679), (3140, 679), "(8)"],
                    [(1970, 552), (2125, 552), (2125, 600), (1970, 600), "Tanggal"],
                    [(2181, 574), (2322, 574), (2322, 623), (2181, 623), "Agama"],
                    [(2500, 574), (2720, 574), (2720, 612), (2500, 612), "Pendidikan"],
                    [(3020, 568), (3323, 564), (3323, 612), (3020, 616), "Jenis Pekerjaan"],
                    [(126, 588), (193, 588), (193, 630), (126, 630), "No."],
                    [(146, 708), (173, 708), (173, 740), (146, 740), "1"],
                    [(146, 760), (173, 760), (173, 792), (146, 792), "2"],
                    [(146, 807), (173, 807), (173, 839), (146, 839), "3"],
                    [(146, 859), (173, 859), (173, 891), (146, 891), "4"],
                    [(146, 907), (173, 907), (173, 939), (146, 939), "5"],
                    [(146, 957), (173, 957), (173, 989), (146, 989), "6"],
                    [(147, 1007), (174, 1007), (174, 1039), (147, 1039), "7"],
                    [(147, 1057), (174, 1057), (174, 1089), (147, 1089), "8"],
                    [(148, 1107), (175, 1107), (175, 1139), (148, 1139), "9"],
                    [(148, 1157), (185, 1157), (185, 1189), (148, 1189), "10"],
                    [(1636, 581), (1882, 581), (1882, 619), (1636, 619), "Tempat Lahir"],
                    [(1378, 606), (1536, 606), (1536, 644), (1378, 644), "Kelamin"],
                    [(1988, 600), (2104, 600), (2104, 642), (1988, 642), "Lahir"],
                    [(127, 1270), (197, 1270), (197, 1310), (127, 1310), "No."],
                    [(154, 1393), (174, 1393), (174, 1424), (154, 1424), "1"],
                    [(153, 1443), (175, 1443), (175, 1474), (153, 1474), "2"],
                    [(153, 1494), (175, 1494), (175, 1526), (153, 1526), "3"],
                    [(153, 1544), (175, 1544), (175, 1576), (153, 1576), "4"],
                    [(153, 1594), (175, 1594), (175, 1626), (153, 1626), "5"],
                    [(153, 1644), (175, 1644), (175, 1676), (153, 1676), "6"],
                    [(153, 1694), (175, 1694), (175, 1726), (153, 1726), "7"],
                    [(153, 1744), (175, 1744), (175, 1776), (153, 1776), "8"],
                    [(153, 1794), (175, 1794), (175, 1826), (153, 1826), "9"],
                    [(151, 1844), (185, 1844), (185, 1875), (151, 1875), "10"],
                    [(547, 1238), (874, 1239), (874, 1287), (546, 1284), "Status Hubungan"],
                    [(1508, 1235), (1854, 1235), (1854, 1280), (1508, 1280), "Dokumen Imigrasi"],
                    [(2629, 1228), (2943, 1228), (2943, 1273), (2629, 1273), "Nama Orang Tua"],
                    [(300, 1246), (423, 1246), (423, 1284), (300, 1284), "Status"],
                    [(330, 1341), (393, 1341), (393, 1382), (330, 1382), "(9)"],
                    [(670, 1339), (753, 1339), (753, 1380), (670, 1380), "(10)"],
                    [(1045, 1337), (1133, 1337), (1133, 1378), (1045, 1378), "(11)"],
                    [(1435, 1335), (1521, 1335), (1521, 1376), (1435, 1376), "(12)"],
                    [(1840, 1333), (1923, 1333), (1923, 1374), (1840, 1374), "(13)"],
                    [(2390, 1331), (2478, 1331), (2478, 1372), (2390, 1372), "(14)"],
                    [(3095, 1329), (3183, 1329), (3183, 1370), (3095, 1370), "(15)"],
                    [(924, 1263), (1255, 1263), (1255, 1311), (924, 1311), "Kewarganegaraan"],
                    [(2380, 1284), (2484, 1284), (2484, 1329), (2380, 1329), "Ayah"],
                    [(3105, 1277), (3172, 1277), (3172, 1322), (3105, 1322), "Ibu"],
                    [(254, 1294), (472, 1294), (472, 1332), (254, 1332), "Perkawinan"],
                    [(567, 1291), (860, 1291), (860, 1331), (567, 1331), "Dalam Keluarga"],
                    [(1374, 1294), (1582, 1294), (1582, 1331), (1374, 1331), "No. Paspor"],
                    [(1720, 1288), (2040, 1284), (2040, 1329), (1721, 1333), "No. KITAS/KITAP"],
                    [(275, 1979), (663, 1979), (663, 2024), (275, 2024), "Dikeluarkan Tanggal"],
                    [(2604, 1993), (3270, 1982), (3271, 2038), (2605, 2049), "A DINAS KEPENUDUDUKAN DAN"],
                    [(1551, 2021), (1966, 2021), (1966, 2069), (1551, 2069), "KEPALA KELUARGA"],
                    [(275, 2038), (455, 2038), (455, 2076), (275, 2076), "LEMBAR"],
                    [(1551, 2021), (1966, 2021), (1966, 2069), (1551, 2069), "KEPALA KELUARGA"],
                    [(754, 2035), (1107, 2035), (1107, 2080), (754, 2080), "I.Kepala Keluarga"],
                    [(2703, 2045), (3027, 2041), (3027, 2090), (2703, 2094), "CATATAN SIPIL"],
                    [(747, 2083), (860, 2083), (860, 2135), (747, 2135), "II.RT"],
                    [(740, 2149), (1099, 2149), (1099, 2194), (740, 2194), "III.Desa/Kelurahan"],
                    [(739, 2204), (1015, 2204), (1015, 2246), (739, 2246), "IV.Kecamatan"],
                    [(1589, 2280), (1948, 2277), (1949, 2325), (1590, 2329), "Tanda Tangan/Cap Jempol"],
                    [(2516, 2222), (3217, 2214), (3218, 2273), (2517, 2281), "Drs. PANCARIA SEMBIRING, MDA"],
                    [(2636, 2277), (3143, 2273), (3143, 2318), (2636, 2322), "NIP.19601027198703 1 006"]]

    def kDrawer(draw,xy,text):
        font = ImageFont.truetype("Lexend-Light.ttf", 60)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=2,spacing=120)
        bblist = [(2885, 29),(right,top),(right,bottom),(2885, 87),"K "+text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=2)
        return draw
    def noDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 83)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=2,spacing=120)
        bblist = [((1292,210)),(right,top),(right,bottom),(1292,290),"No. "+text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=2)
        return draw
    def nkkDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 37)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def locDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 37)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def tanggalDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 42)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def ttdDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 42)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def namaDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 30)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def nikDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 30)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def jkDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def temlahDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def tanlahDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def agamaDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def pendidikanDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def jepekDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def statperDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def shdkDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def kewDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def nopasDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def nokitDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def ayahDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw
    def ibuDrawer(draw,xy,text):
        font = ImageFont.truetype("arial.ttf", 29)
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor='lt', stroke_width=1,spacing=120)
        bblist = [(left,top),(right,top),(right,bottom),(left,bottom),text]
        listBoundingBox.append(bblist)
        draw.text(xy, text, font=font, fill=(0, 0, 0, 255), anchor='lt', spacing=120, stroke_width=1)
        return draw


    faker = Faker('id_ID')
    fakerLuar = Faker()

    jenisKelamin = ['LAKI-LAKI','PEREMPUAN']
    agama = ['KRISTEN','KATOLIK','ISLAM','HINDU','BUDDHA','KONGHUCU']
    statusPerkawinan = ['KAWIN','BELUM KAWIN']
    statusHubungan = ['KEPALA KELUARGA', 'ISTRI', 'ANAK']
    pendidikan = ['TIDAK/BELUM SEKOLAH','TAMAT SD/SEDERAJAT','SLTP/SEDERAJAT','SLTA/SEDERAJAT','D-I/D-II','D-IV/STRATA I','STRATA II','STRATA III','BELUM TAMAT SD/SEDERAJAT','AKADEMI/DIPLOMA III/S. MUDA']
    pekerjaan2 = [
    "TIDAK BEKERJA",
    "IBU RUMAH TANGGA",
    "PENSIUN",
    "PEGAWAI NEGERI",
    "TENTARA",
    "POLISI",
    "PERDAGANGAN",
    "PETANI",
    "PETERNAK"
    "NELAYAN",
    "INDUSTRI",
    "KONSTRUKSI",
    "TRANSPORTASI",
    "KARYAWAN SWASTA",
    "KARYAWAN BUMN",
    "KARYAWAN BUMD",
    "KARYAWAN HONORER",
    "BURUH HARIAN",
    "PRT",
    "TUKANG KAYU",
    "PENJAHIT",
    "PENATA RAMBUT",
    "PENATA RIAS",
    "PENATA BUSANA",
    "MEKANIK",
    "DOKTER GIGI",
    "SENIMAN",
    "PENDETA",
    "PASTUR",
    "WARTAWAN",
    "USTADZ",
    "DOSEN",
    "GURU",
    "PILOT",
    "PENGACARA",
    "NOTARIS",
    "ARSITEK",
    "AKUNTAN",
    "KONSULTAN",
    "DOKTER",
    "BIDAN",
    "PERAWAT",
    "APOTEKER",
    "PSIKOLOG",
    "PELAUT",
    "PENELITI",
    "SOPIR",
    "WIRASWASTA"]
    pekerjaan = [
    "TIDAK BEKERJA",
    "IBU RUMAH TANGGA",
    "PELAJAR/MAHASISWA",
    "PENSIUN",
    "PEGAWAI NEGERI",
    "TENTARA",
    "POLISI",
    "PERDAGANGAN",
    "PETANI",
    "PETERNAK"
    "NELAYAN",
    "INDUSTRI",
    "KONSTRUKSI",
    "TRANSPORTASI",
    "KARYAWAN SWASTA",
    "KARYAWAN BUMN",
    "KARYAWAN BUMD",
    "KARYAWAN HONORER",
    "BURUH HARIAN",
    "PRT",
    "TUKANG KAYU",
    "PENJAHIT",
    "PENATA RAMBUT",
    "PENATA RIAS",
    "PENATA BUSANA",
    "MEKANIK",
    "DOKTER GIGI",
    "SENIMAN",
    "PENDETA",
    "PASTUR",
    "WARTAWAN",
    "USTADZ",
    "DOSEN",
    "GURU",
    "PILOT",
    "PENGACARA",
    "NOTARIS",
    "ARSITEK",
    "AKUNTAN",
    "KONSULTAN",
    "DOKTER",
    "BIDAN",
    "PERAWAT",
    "APOTEKER",
    "PSIKOLOG",
    "PELAUT",
    "PENELITI",
    "SOPIR",
    "WIRASWASTA"]
    kewarganegaraan = ['WNI','WNA']
    abjat = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y','Z']
    base = Image.open('kk_cleanup(2).jpg')
    txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    nPerson = randint(1,10)
    noKK = ''
    for i in range(16):
        noKK += str(randint(0,9))


    #----------INI LOGIC----------
    #inisialisasi info kk
    tK = ''
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
        tK = keyAwal
        for i in range(10):
            tNo += str(randint(0,9))
        for i in range(7):
            tK += str(randint(0,9))
        if(tJenisKelamin[0] == "LAKI-LAKI"):
            temp = str(tTanggalLahir[0])
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
            templateTempatLahir = faker.city().upper()
            while(len(templateTempatLahir)>20):
                templateTempatLahir = faker.city().upper()
            tTempatLahir[0] = templateTempatLahir

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
        tK = keyAwal
        for i in range(10):
            tNo += str(randint(0,9))
        for i in range(7):
            tK += str(randint(0,9))

    #----------------NIK-------------------


    # Penentuan Tempat Lahir

        for i in range(nPerson):
            if(tKewarganegaraan[i] == "WNI"):
                templateTempatLahir = faker.city().upper()
                while(len(templateTempatLahir)>20):
                    templateTempatLahir = faker.city().upper()
                tTempatLahir[i] = templateTempatLahir
            else:
                templateTempatLahir = fakerLuar.city().upper()
                while(len(templateTempatLahir)>20):
                    templateTempatLahir = fakerLuar.city().upper()
                tTempatLahir[i] = templateTempatLahir


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
                if(len(tNamaIstri)>=1):
                    tIbu[i] = random.choice(tNamaIstri)
                else:
                    tIbu[i] = faker.name_female().upper()
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
    draw = kDrawer(draw,posK,tK)
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
            if(tAyah[i]!= 0):
                draw = ayahDrawer(draw,posAyah[i],tAyah[i])

            if(tIbu[i]!=0):
                draw = ibuDrawer(draw,posIbu[i],tIbu[i])

    draw = tanggalDrawer(draw,posTanggal,tDikeluarkanTanggal)
    out = Image.alpha_composite(base, txt_layer)
    out = out.convert('RGB')
    out.save(path)
    # for each in listBoundingBox:
    #     new_txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
    #     new_draw = ImageDraw.Draw(new_txt_layer)
    #     poly = [each[0],each[1],each[2],each[3]]
    #     new_draw = new_draw.polygon(poly, outline ="blue")
    #     out = Image.alpha_composite(out, new_txt_layer) 
    # out.show() 
    return listBoundingBox

def addBlur(img):
    img = img.filter(ImageFilter.GaussianBlur(random.uniform(1.0, 2.0)))
    return img

def rotateImg(img, angle):
    img = img.rotate(angle, expand=True)
    return img

def rescaleImg(img,scale):
    width, height = img.size
    new_width = int(width*scale)
    new_height = int(height*scale)
    return img.resize(new_width,new_height)

def saltAndPepper(img, dense):  
    row , col = img.size
    num_of_pix = int(row*col*dense)
    for _ in range(num_of_pix):
        x = random.randint(0, row - 1)
        y = random.randint(0, col - 1)
        n1 = random.randint(0, 64)
        n2 = random.randint(0, 64)
        n3 = random.randint(0, 64)
        img.putpixel((x,y), (n1, n2, n3, 255))
    return img
    
def createKKComplete(path):
    import matlab.engine
    listBoundingBox = createKKOnly(path)
    backgroundNumber = randint(1,5)
    backgroundPath = "background/"+str(backgroundNumber)+".jpg"
    # dense = randint(1,20)/100
    angle = randint(-3,3)
    img = Image.open(path)
    img = img.convert('RGBA')
    width, height = img.size

    # add salt and pepper
    denseSaltPepper = float(randint(1,20)/100)
    img = saltAndPepper(img,denseSaltPepper)

    # add blur to image
    img = addBlur(img)

    # rotate image
    img = rotateImg(img,angle)
    
    width_after_rotate, heigh_after_rotate = img.size
    width_differ = width_after_rotate - width
    height_differ = heigh_after_rotate - height
    img = img.convert('RGB')
    img.save(path)

    #img.save(path)
    new_img = img
    new_img = new_img.convert("RGBA")

    # rotate bounding box to match new_image
    for bb in listBoundingBox:
        #poly = []
        for i in range(4):
            dot = bb[i]
            x,y = rotate_dot(dot[0],dot[1],angle*(-1))
            if(angle>0):
                new_dot = (x,y+height_differ)
            else:
                new_dot = (x+width_differ,y)
            bb[i] = new_dot
            #poly.append(new_dot)
    #     new_txt_layer = Image.new("RGBA", new_img.size, (255, 255, 255, 0))
    #     new_draw = ImageDraw.Draw(new_txt_layer)      
    #     new_draw = new_draw.polygon(poly, outline ="blue")
    #     new_img = Image.alpha_composite(new_img, new_txt_layer)
    # new_img.show()
    
    # resize image(lower quality) and add the image to new background
    eng = matlab.engine.start_matlab()
    scaling, s_height, s_width = eng.fullModified(path,backgroundPath, nargout=3)

    img_from_matlab = Image.open(path)
    img_from_matlab = img_from_matlab.convert("RGBA")
    # rescaling and reposition the bounding box
    for bb in listBoundingBox:
        #poly = []
        for i in range(4):
            dot = bb[i]
            new_dot = (int(dot[0]*scaling+s_width), int(dot[1]*scaling)+s_height)
            bb[i] = new_dot
            #poly.append(new_dot)
    #     new_txt_layer = Image.new("RGBA", img_from_matlab.size, (255, 255, 255, 0))
    #     new_draw = ImageDraw.Draw(new_txt_layer)      
    #     new_draw = new_draw.polygon(poly, outline ="blue")
    #     img_from_matlab = Image.alpha_composite(img_from_matlab, new_txt_layer)
    # img_from_matlab.show()
    return listBoundingBox
    #upload the bounding box to txt file


def writeBBToTxt(path,listbb:list):
    f= open(path,"w+")
    for row in listbb:
        text = str(int(row[0][0]))+','+str(int(row[0][1]))+','+str(int(row[1][0]))+','+str(int(row[1][1]))+','+str(int(row[2][0]))+','+str(int(row[2][1]))+','+str(int(row[3][0]))+','+str(int(row[3][1]))+','+row[4]
        f.write(text+"\n")
    f.close()

n=10
for i in range(n):
    pathImg = "result/image/img_" + str(i+1) + ".jpg"
    pathBB = "result/label/gt_img_" + str(i+1) + ".txt"
    listbb = createKKComplete(pathImg)
    writeBBToTxt(pathBB,listbb)
    print(i)
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from faker import Faker
import argparse
import math

PROVINSI = [
    "NANGGROE ACEH DARUSSALAM",
    "SUMATERA UTARA",
    "SUMATERA SELATAN",
    "SUMATERA BARAT",
    "BENGKULU",
    "RIAU",
    "KEPULAUAN RIAU",
    "JAMBI",
    "LAMPUNG",
    "BANGKA BELITUNG",
    "KALIMANTAN BARAT",
    "KALIMANTAN TIMUR",
    "KALIMANTAN SELATAN",
    "KALIMANTAN TENGAH",
    "KALIMANTAN UTARA",
    "BANTEN",
    "DKI JAKARTA",
    "JAWA BARAT",
    "JAWA TENGAH",
    "DAERAH ISTIMEWA YOGYAKARTA",
    "JAWA TIMUR",
    "BALI",
    "NUSA TENGGARA TIMUR",
    "NUSA TENGGARA BARAT",
    "GORONTALO",
    "SULAWESI BARAT",
    "SULAWESI TENGAH",
    "SULAWESI UTARA",
    "SULAWESI TENGGARA",
    "SULAWESI SELATAN",
    "MALUKU UTARA",
    "MALUKU",
    "PAPUA BARAT",
    "PAPUA",
    "PAPUA TENGAH",
    "PAPUA PEGUNUNGAN",
    "PAPUA SELATAN",
    "PAPUA BARAT DAYA",
]

GOLDA = ["A", "B", "AB", "O", "-"]
GENDER = ["LAKI-LAKI", "PEREMPUAN"]

AGAMA = [
    "ISLAM",
    "KRISTEN",
    "KATOLIK",
    "HINDU",
    "KONGHUCU",
    "BUDHA"
]

PERKAWINAN = ["BELUM KAWIN", "KAWIN"]

PEKERJAAN = [
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
    "WIRASWASTA"
]

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

class KTPGenerator:
    def __init__(self, img_path, args) -> None:
        self.fake = Faker('id_ID')
        self.path = img_path
        self.args = args
        self.base = Image.open(self.path).convert("RGBA")
        self.txt_layer = None
        self.boundingbox = []
        self.predicted = []
        self.SKEW = 3
        self.NUM = 10
        self.BLUR = 2
        self.SALTPEPPER = 500000

    def skew(self):
        agl = args.skew if args.skew != None else self.SKEW
        if agl == 0:
            return
        angle = random.uniform(-agl, agl)
        width, heigh = self.out.size
        self.out = self.out.rotate(angle, expand=True)
        width_after_rotate, heigh_after_rotate = self.out.size
        width_differ = width_after_rotate - width
        height_differ = heigh_after_rotate - heigh

        for i in range(len(self.boundingbox)):
            for j in range(4):
                dot = self.boundingbox[i][j]
                x,y = rotate_dot(dot[0],dot[1],angle*(-1))
                if(angle>0):
                    self.boundingbox[i][j] = (x,y+height_differ)
                else:
                    self.boundingbox[i][j] = (x+width_differ,y)
    
    def blur(self):
        rad = args.blur if args.blur != None else self.BLUR
        if rad == 0:
            return
        self.txt_layer = self.txt_layer.filter(ImageFilter.GaussianBlur(2))
    
    def saltAndPepper(self):
        max = args.salt_and_pepper if args.salt_and_pepper != None else self.SALTPEPPER
        row , col = self.out.size
        num_of_pix = random.randint(100000 , max)
        for _ in range(num_of_pix):
            x = random.randint(0, row - 1)
            y = random.randint(0, col - 1)
            n1 = random.randint(0, 64)
            n2 = random.randint(0, 64)
            n3 = random.randint(0, 64)
            self.out.putpixel((x,y), (n1, n2, n3, 255))

    def save(self, i):
        self.out.save(f'out/image/img_{i}.jpg')
        f=open(f'out/label/gt_img_{i}.txt')
        for i in range(len(self.boundingbox)):
            txt = ""
            for point in self.boundingbox[i]:
                for each in point:
                    txt += str(int(each)) + ','
            txt += self.predicted[i]
            f.write(txt+"\n")
        f.close()

    def showBoundingBox(self):
        for poly in self.boundingbox:
            bb_layer = Image.new("RGBA",self.out.size, (255,255,255,0))
            temp_draw = ImageDraw.Draw(bb_layer)
            temp_draw = temp_draw.polygon(poly,outline="blue")
            self.out = Image.alpha_composite(self.out,bb_layer)
        self.out.show()
    
    def create(self):
        self.txt_layer = Image.new("RGBA", self.base.size, (255, 255, 255, 0))
        self.boundingbox = [[(73, 271), (307, 271), (307, 379), (73, 379)],
                            [(73, 449), (263, 449), (263, 501), (73, 501)],
                            [(85, 530), (585, 530), (585, 589), (85, 589)],
                            [(82, 615), (491, 615), (491, 664), (82, 664)],
                            [(1416, 609), (1752, 609), (1752, 667), (1416, 667)],
                            [(70, 691), (301, 691), (301, 752), (70, 752)],
                            [(234, 772), (471, 772), (471, 834), (234, 834)],
                            [(232, 851), (530, 857), (528, 918), (231, 912)],
                            [(234, 938), (594, 938), (594, 997), (234, 997)],
                            [(66, 1027), (296, 1016), (299, 1080), (69, 1091)],
                            [(70, 1105), (644, 1105), (644, 1163), (70, 1163)],
                            [(68, 1183), (378, 1189), (376, 1254), (67, 1247)],
                            [(65, 1268), (638, 1271), (637, 1332), (64, 1329)],
                            [(68, 1346), (533, 1356), (532, 1417), (67, 1407)]]
        self.predicted = ["NIK","Nama","Tempat/Tgl Lahir","Jenis Kelamin","Gol Darah","Alamat","RT/RW","Kel/Des","Kecamatan",
                          "Agama","Status Perkawinan","Pekerjaan","Kewarganegaraan","Berlaku Hingga"]
        draw = ImageDraw.Draw(self.txt_layer)

        font_judul = ImageFont.truetype("./font/arlrdbd.ttf", 90)
        font_nik = ImageFont.truetype("./font/OCR A Extended.ttf", 128)
        font_data = ImageFont.truetype("./font/arial-bold.ttf", 65)  

        provinsi    = "PROVINSI " + random.choice(PROVINSI)
        kabupaten   = random.choice(["KABUPATEN ", "KOTA "]) + self.fake.city().upper()
        nik         = f'{random.randint(0,9999999999999999):016}'
        nama        = self.fake.first_name().upper() + " " + self.fake.last_name().upper()
        ttl         = self.fake.city().upper() + ", " + self.fake.date(pattern="%d-%m-%Y")
        gender      = random.choice(GENDER)
        golda       = random.choice(GOLDA)
        alamat      = self.fake.street_address().upper()
        rt_rw       = f'{random.randint(0,999):03}' + '/' + f'{random.randint(0,999):03}'
        kelurahan   = self.fake.city().upper()
        kecamatan   = self.fake.city().upper()
        agama       = random.choice(AGAMA)
        perkawinan  = random.choice(PERKAWINAN)
        pekerjaan   = random.choice(PEKERJAAN)
        kewarganegaraan = random.choice(["WNI", "WNA"])
        berlaku     = random.choice(["SEUMUR HIDUP", self.fake.date(pattern="%d-%m-%Y")])
        tempat      = self.fake.city().upper()
        tgl         = self.fake.date(pattern="%d-%m-%Y")
        
        draw.text((1463, 55), provinsi, font=font_judul, fill=(12,42,59,255), anchor='mt')
        left,top,right,bottom = draw.textbbox((1463,55),provinsi, font= font_judul, anchor='mt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(provinsi)

        draw.text((1463, 149), kabupaten, font=font_judul, fill=(12,42,59,255), anchor='mt')
        left,top,right,bottom = draw.textbbox((1463, 149),kabupaten, font= font_judul, anchor='mt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(kabupaten)

        draw.text((703, 280), nik, font=font_nik, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((703, 280),nik, font= font_nik, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(nik)

        draw.text((775, 453), nama, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 453),nama, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(nama)

        draw.text((775, 535), ttl, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 535),ttl, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(ttl)

        draw.text((775, 613), gender, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 613),gender, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(gender)

        draw.text((1852, 641), golda, font=font_data, fill=(12,42,59,255), anchor='lm')
        left,top,right,bottom = draw.textbbox((1852, 641),golda, font= font_data, anchor='lm')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(golda)

        draw.text((775, 699), alamat, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 699),alamat, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(alamat)

        draw.text((775, 781), rt_rw, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 781),rt_rw, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(rt_rw)

        draw.text((775, 861), kelurahan, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 861),kelurahan, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(kelurahan)

        draw.text((775, 943), kecamatan, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 943),kecamatan, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(kecamatan)

        draw.text((775, 1023), agama, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 1023),agama, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(agama)

        draw.text((775, 1109), perkawinan, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 1109),perkawinan, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(perkawinan)

        draw.text((775, 1187), pekerjaan, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 1187),pekerjaan, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(pekerjaan)

        draw.text((775, 1269), kewarganegaraan, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 1269),kewarganegaraan, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(kewarganegaraan)

        draw.text((775, 1351), berlaku, font=font_data, fill=(12,42,59,255), anchor='lt')
        left,top,right,bottom = draw.textbbox((775, 1351),berlaku, font= font_data, anchor='lt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(berlaku)

        draw.text((2387, 1227), tempat, font=font_data, fill=(12,42,59,255), anchor='mt')
        left,top,right,bottom = draw.textbbox((2387, 1227),tempat, font= font_data, anchor='mt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(tempat)

        draw.text((2387, 1313), tgl, font=font_data, fill=(12,42,59,255), anchor='mt')
        left,top,right,bottom = draw.textbbox((2387, 1313),tgl, font= font_data, anchor='mt')
        bb = [(left,top),(right,top),(right,bottom),(left,bottom)]
        self.boundingbox.append(bb)
        self.predicted.append(tgl)
        self.blur()
        self.out = Image.alpha_composite(self.base, self.txt_layer)


    def generate(self):
        n = args.number if args.number != None else self.NUM
        for i in range(n):
            self.create()
            self.saltAndPepper()
            self.skew()
            self.save(i)

    def test(self):
        self.create()
        self.saltAndPepper()
        self.skew()
        self.showBoundingBox()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-t", "--test", type=bool, help="True for test")
    argParser.add_argument("-n", "--number", type=float, help="Number of generated dataset (default = 10)")
    argParser.add_argument("-s", "--skew", type=int, help="Max skew angle in degree (default= 3, 0 to switch off")
    argParser.add_argument("-b", "--blur", type=float, help="Max gaussian blur radius (default = 1.2, 0 to switch off")
    argParser.add_argument("-sp", "--salt_and_pepper", type=int, help="Salt and pepper density (default = 5000)")
    args = argParser.parse_args()

    Generator = KTPGenerator("test.jpg", args=args)

    if args.test == True:
        Generator.test()
    else:
        Generator.generate()
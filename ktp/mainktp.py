from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from faker import Faker
import argparse

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

class KTPGenerator:
    def __init__(self, img_path, args) -> None:
        self.fake = Faker('id_ID')
        self.path = img_path
        self.args = args
        self.base = Image.open(self.path).convert("RGBA")
        self.txt_layer = None
        self.SKEW = 3
        self.NUM = 10
        self.BLUR = 2
        self.SALTPEPPER = 500000

    def skew(self):
        agl = args.skew if args.skew != None else self.SKEW
        if agl == 0:
            return
        self.out = self.out.rotate(random.uniform(-agl, agl), expand=True)
    
    def blur(self):
        rad = args.blur if args.blur != None else self.BLUR
        if rad == 0:
            return
        self.out = self.out.filter(ImageFilter.GaussianBlur(random.uniform(1.5, rad)))
    
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
        self.out.save(f'out/{i}.png')
    
    def create(self):
        self.txt_layer = Image.new("RGBA", self.base.size, (255, 255, 255, 0))
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
        draw.text((1463, 149), kabupaten, font=font_judul, fill=(12,42,59,255), anchor='mt')
        draw.text((703, 280), nik, font=font_nik, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 453), nama, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 535), ttl, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 613), gender, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((1852, 641), golda, font=font_data, fill=(12,42,59,255), anchor='lm')
        draw.text((775, 699), alamat, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 781), rt_rw, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 861), kelurahan, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 943), kecamatan, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 1023), agama, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 1109), perkawinan, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 1187), pekerjaan, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 1269), kewarganegaraan, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((775, 1351), berlaku, font=font_data, fill=(12,42,59,255), anchor='lt')
        draw.text((2387, 1227), tempat, font=font_data, fill=(12,42,59,255), anchor='mt')
        draw.text((2387, 1313), tgl, font=font_data, fill=(12,42,59,255), anchor='mt')

        self.out = Image.alpha_composite(self.base, self.txt_layer)


    def generate(self):
        n = args.number if args.number != None else self.NUM
        for i in range(n):
            self.create()
            self.saltAndPepper()
            self.blur()
            self.skew()
            self.save(i)

    def test(self):
        self.create()
        self.saltAndPepper()
        self.blur()
        self.skew()
        self.out.show()

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
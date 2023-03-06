from PIL import Image, ImageFont, ImageDraw
import random
from faker import Faker

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
    def __init__(self, img_path) -> None:
        self.fake = Faker('id_ID')
        self.path = img_path
        self.base = Image.open(self.path).convert("RGBA")
        self.txt_layer = None                      

    def save(self, i):
        self.out = Image.alpha_composite(self.base, self.txt_layer)
        # self.out.show()
        self.out.save(f'out/{i}.png')

    def generate(self, n:int):
        for i in range(n):
            self.txt_layer = Image.new("RGBA", self.base.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(self.txt_layer)

            font_judul = ImageFont.truetype("arlrdbd.ttf", 90)
            font_nik = ImageFont.truetype("OCR A Extended.ttf", 128)
            font_data = ImageFont.truetype("arial-bold.ttf", 65)  

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
            
            draw.text((1463, 55), provinsi, font=font_judul, fill=(0, 0, 0, 255), anchor='mt')
            draw.text((1463, 149), kabupaten, font=font_judul, fill=(0, 0, 0, 255), anchor='mt')
            draw.text((703, 280), nik, font=font_nik, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 453), nama, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 535), ttl, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 613), gender, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((1852, 641), golda, font=font_data, fill=(0, 0, 0, 255), anchor='lm')
            draw.text((775, 699), alamat, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 781), rt_rw, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 861), kelurahan, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 943), kecamatan, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 1023), agama, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 1109), perkawinan, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 1187), pekerjaan, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 1269), kewarganegaraan, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((775, 1351), berlaku, font=font_data, fill=(0, 0, 0, 255), anchor='lt')
            draw.text((2387, 1227), tempat, font=font_data, fill=(0, 0, 0, 255), anchor='mt')
            draw.text((2387, 1313), tgl, font=font_data, fill=(0, 0, 0, 255), anchor='mt')

            self.save(i)


Generator = KTPGenerator("test.jpg")
Generator.generate(10)



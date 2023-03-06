from PIL import Image, ImageFont, ImageDraw
import random
from faker import Faker

TYPES = ["A", "BI", "BII", "C", "D"]
GOLDA = ["A", "B", "AB", "O"]
GENDER = ["PRIA", "WANITA"]
PEKERJAANS = [
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
    "SOPIR"
]

POLDAS = [
    "ACEH",
    "BALI",
    "BANTEN",
    "BENGKULU",
    "YOGYAKARTA",
    "GORONTALO",
    "JAMBI",
    "JABAR",
    "JATENG",
    "JATIM",
    "KALBAR",
    "KALSEL",
    "KALTENG",
    "KALTIM",
    "KALUT",
    "BABEL",
    "KEPRI",
    "LAMPUNG",
    "MALUKU",
    "MALUT",
    "METRO JAYA",
    "NTB",
    "NTT",
    "PAPUA",
    "PAPBAR",
    "RIAU",
    "SULBAR",
    "SULSEL",
    "SULTENG",
    "SULTRA",
    "SULUT",
    "SUMBAR",
    "SUMSEL",
    "SUMUT"
]

# SIM: 85.60 mm x 53.98 mm  (sama juga untuk KTP)
# Resize image -> 720 x 453 px (asumsi pinggiran SIM tepat pada tepi image)  

class SIMGenerator:
    def __init__(self, img_path) -> None:
        self.fake = Faker('id_ID')
        self.path = img_path
        self.base = Image.open(self.path)
        self.txt_layer = None                   # Image.new("RGBA", self.base.size, (255, 255, 255, 0))
        self.draw = None                        # ImageDraw.Draw(self.txt_layer)

    def typeDrawer(self, type):
        font = ImageFont.truetype("arial.ttf", 56)
        self.draw.text((550, 85), type, font=font, fill=(0, 0, 0, 255), anchor='lt',  stroke_width=2)

    def namaDrawer(self, name):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 177), name, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def ttlDrawer(self, ttl):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 205), ttl, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def golGenderDrawer(self, golgen):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 233), golgen, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def almtDrawer(self, line1, line2, line3):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 261), line1, font=font, fill=(0, 0, 0, 255), anchor='lt')
        self.draw.text((250, 289), line2, font=font, fill=(0, 0, 0, 255), anchor='lt')
        self.draw.text((250, 317), line3, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def profDrawer(self, prof):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 343), prof, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def polDrawer(self, pol):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 370), pol, font=font, fill=(0, 0, 0, 255), anchor='lt')

    def noDrawer(self, no):
        font = ImageFont.truetype("./font/arial-bold.ttf", 25)
        self.draw.text((565, 150), no, font=font, fill=(0, 0, 0, 255), anchor='mm')

    def tglBwhDrawer(self, tgl):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((590, 432), tgl, font=font, fill=(0, 0, 0, 255), anchor='mm')

    def save(self, i):
        self.out = Image.alpha_composite(self.base, self.txt_layer)
        self.out.save(f'out/{i}.png')

    def generate(self, n:int):
        for i in range(n):
            # INITIATION
            self.txt_layer = Image.new("RGBA", self.base.size, (255, 255, 255, 0))
            self.draw = ImageDraw.Draw(self.txt_layer)

            type    = random.choice(TYPES)
            name    = self.fake.first_name().upper() + " " + self.fake.last_name().upper()
            ttl     = self.fake.city().upper() + ", " + self.fake.date(pattern="%d-%m-%Y")
            golgen  = random.choice(GOLDA) + "-" + random.choice(GENDER)
            line1   = self.fake.street_address().upper()
            line2   = self.fake.street().upper()
            line3   = self.fake.state().upper()
            prof    = random.choice(PEKERJAANS)
            pol     = random.choice(POLDAS)
            no      = f'{random.randint(0,9999):04}'+'-'+ f'{random.randint(0,9999):04}' +'-'+f'{random.randint(0,999999):06}'
            tgl     = self.fake.date(pattern="%d-%m-%Y")
            
            self.typeDrawer(type)
            self.namaDrawer(name)
            self.ttlDrawer(ttl)
            self.golGenderDrawer(golgen)
            self.almtDrawer(line1, line2, line3)
            self.profDrawer(prof)
            self.polDrawer(pol)
            self.noDrawer(no)
            self.tglBwhDrawer(tgl)

            self.save(i)


Generator = SIMGenerator("./test.jpg")
Generator.generate(10)



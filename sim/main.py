from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from faker import Faker
import argparse
import math

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

class SIMGenerator:
    SKEW = 3
    NUM = 10
    BLUR = 1.2
    SALTPEPPER = 10000
    WHITE = (255, 255, 255, 255)
    BLACK = (0, 0, 0, 255)

    def __init__(self, img_path, args) -> None:
        self.fake = Faker('id_ID')
        self.path = img_path
        self.base = Image.open(self.path)
        self.txt_layer = None                   # Image.new("RGBA", self.base.size, (255, 255, 255, 0))
        self.draw = None                        # ImageDraw.Draw(self.txt_layer)
        self.args = None
        self.boundingbox = []
        self.predicted = []
        self.rec_labels = ""
        self.rec_counter = 1

    def addLabel(self, draw, font, anchor, xy, text, stroke):
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor=anchor,stroke_width=stroke)
        bb = [(left-7,top-7),(right+7,top-7),(right+7,bottom+7),(left-7,bottom+7)]
        self.boundingbox.append(bb)
        self.predicted.append(text)

    def addLabel2(self, draw, font, anchor, xy, text, stroke, leftTop, leftBottom):
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor=anchor,stroke_width=stroke)
        bb = [(leftTop[0]-7,leftTop[1]-7),(right+7,top-7),(right+7,bottom+7),(leftBottom[0]-7,leftBottom[1]+7)]
        self.boundingbox.append(bb)
        self.predicted.append(text)

    def typeDrawer(self, type):
        font = ImageFont.truetype("arial.ttf", 56)
        self.draw.text((550, 85), type, font=font, fill=(0, 0, 0, 220), anchor='lt',  stroke_width=2)
        self.addLabel(self.draw,font,'lt',(550, 85),type,2)
        

    def namaDrawer(self, name):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 177), name, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 177),name,1,(220, 175),(219, 193))
    

    def ttlDrawer(self, ttl):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 205), ttl, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 205),ttl,1,(220, 202),(219, 223))


    def golGenderDrawer(self, golgen):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 233), golgen, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 233),golgen,1,(217, 229),(216, 251))

    def almtDrawer(self, line1, line2, line3):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 261), line1, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 261),line1,1,(216, 260),(215, 279))
       
        self.draw.text((250, 289), line2, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel(self.draw,font,'lt',(250, 289),line2,1)
        
        self.draw.text((250, 317), line3, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel(self.draw,font,'lt',(250, 317),line3,1)
        

    def profDrawer(self, prof):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 343), prof, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 343),prof,1,(217, 340),(216, 360))
        

    def polDrawer(self, pol):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((250, 370), pol, font=font, fill=(0, 0, 0, 220), anchor='lt')
        self.addLabel2(self.draw,font,'lt',(250, 370),pol,1,(218, 367),(217, 389))
    

    def noDrawer(self, no):
        font = ImageFont.truetype("./font/arial-bold.ttf", 25)
        self.draw.text((565, 150), no, font=font, fill=(0, 0, 0, 220), anchor='mm')
        self.addLabel(self.draw,font,'mm',(565, 150),no,1)
    

    def tglBwhDrawer(self, tgl):
        font = ImageFont.truetype("./font/arial-bold.ttf", 23)
        self.draw.text((590, 432), tgl, font=font, fill=(0, 0, 0, 220), anchor='mm')
        self.addLabel(self.draw,font,'mm',(590, 432),tgl,1)
        

    def skewNoise(self):
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
        self.out = self.out.filter(ImageFilter.GaussianBlur(random.uniform(0, rad)))

    def saltAndPepper(self):
        max = args.salt_and_pepper if args.salt_and_pepper != None else 5000
        row , col = self.out.size
        num_of_pix = random.randint(300 , max)
        for _ in range(num_of_pix):
            x = random.randint(0, row - 1)
            y = random.randint(0, col - 1)
            n = random.randint(64, 128)
            self.out.putpixel((x,y), (n, n, n, 255))
            
    def save(self, i):
        self.out = self.out.convert('RGB')
        self.out.save(f'detection/image/img_{i}.jpg')
        f=open(f'detection/label/gt_img_{i}.txt','w+')
        for i in range(len(self.boundingbox)):
            # recogniton images
            points = self.boundingbox[i]
            x1, y1 = points[0]
            x3, y3 = points[2]
            cropped_img = self.out.crop((x1, y1, x3, y3))
            cropped_img.save(f'recognition/train/word_{self.rec_counter}.png')
            self.rec_labels += f"recognition/train/word_{self.rec_counter}.png\t{self.predicted[i]}\n"
            self.rec_counter += 1

            # detection label
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
        self.draw = ImageDraw.Draw(self.txt_layer)
        self.boundingbox = [[(185, 26), (442, 28), (441, 74), (185, 72)],
                            [(482, 47), (675, 52), (675, 83), (482, 79)],
                            [(187, 67), (448, 70), (448, 100), (187, 97)]]
        self.predicted = ["INDONESIA","DRIVING LICENSE","SURAT IZIN MENGEMUDI"]

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

        self.out = Image.alpha_composite(self.base, self.txt_layer)

    def generate(self):
        n = args.number if args.number != None else self.NUM
        rec_label_file = open(f'recognition/rec_gt_train.txt', 'w+')
        for i in range(n):
            self.create()
            self.saltAndPepper()
            self.blur()
            self.skewNoise()
            self.save(i)
        rec_label_file.write(self.rec_labels)
        rec_label_file.close()

    def test(self):
        print("Hrusnya ga disini")
        self.create()
        self.saltAndPepper()
        self.blur()
        self.skewNoise()
        self.showBoundingBox()

if __name__ == "__main__":
    # MAIN PROGRAM
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-t", "--test", type=bool, help="True for test")
    argParser.add_argument("-n", "--number", type=int, help="Number of generated dataset (default = 10)")
    argParser.add_argument("-s", "--skew", type=int, help="Max skew angle in degree (default= 3, 0 to switch off")
    argParser.add_argument("-b", "--blur", type=float, help="Max gaussian blur radius (default = 1.2, 0 to switch off")
    argParser.add_argument("-sp", "--salt_and_pepper", type=int, help="Salt and pepper density (default = 5000)")
    args = argParser.parse_args()
    
    Generator = SIMGenerator("./test.jpg", args=args)
    
    if args.test == True:
        Generator.test()
    else:
        Generator.generate()

"""
TODO
skewNoise [v]
greyishText [v]
pinkNoise
whiteNoise
blurNoise
"""
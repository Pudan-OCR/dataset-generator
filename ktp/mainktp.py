from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from faker import Faker
import argparse
import math
import os

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

def get_latest_folder(path):
    # Normalize the path to handle different path separators (e.g., / or \)
    normalized_path = os.path.normpath(path)

    # Split the path into individual folder names
    folders = normalized_path.split(os.path.sep)

    # Filter out empty strings (in case of multiple separators)
    folders = [folder for folder in folders if folder]

    # Get the latest folder name (the last element of the list)
    latest_folder = folders[-1]

    return latest_folder

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
        self.rec_labels = ""
        self.rec_counter = 1
        self.detection_path = args.detection_path if args.detection_path != None else "detection/"
        self.recogniton_path = args.recognition_path if args.recognition_path != None else "recognition"
        self.is_detection = args.is_detection if args.is_detection != None else False
        self.is_recognition = args.is_recognition if args.is_recognition != None else False

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
        self.out = self.out.convert('RGB')
        if (self.is_detection):
            detection_file_path = f'{self.detection_path}image/img_{i}.jpg'
            self.out.save(detection_file_path)
            f=open(f'{self.detection_path}label/gt_img_{i}.txt','w+')

        for i in range(len(self.boundingbox)):
            # recognition images & labels
            if (self.is_recognition):
                points = self.boundingbox[i]
                x1, y1 = points[0]
                x3, y3 = points[2]
                cropped_img = self.out.crop((x1, y1, x3, y3))
                cropped_img.save(f'{self.recogniton_path}/word_{self.rec_counter}.png')
                self.rec_labels += f"{get_latest_folder(self.recogniton_path)}/word_{self.rec_counter}.png\t{self.predicted[i]}\n"
                self.rec_counter += 1

            # detection labels
            if self.is_detection:
                txt = ""
                for point in self.boundingbox[i]:
                    for each in point:
                        txt += str(int(each)) + ','
                txt += self.predicted[i]
                f.write(txt+"\n")
        
        if (self.is_detection):
            f.close()

    def showBoundingBox(self):
        for poly in self.boundingbox:
            bb_layer = Image.new("RGBA",self.out.size, (255,255,255,0))
            temp_draw = ImageDraw.Draw(bb_layer)
            temp_draw = temp_draw.polygon(poly,outline="blue")
            self.out = Image.alpha_composite(self.out,bb_layer)
        self.out.show()

    def addLabel(self, draw, font, anchor, xy, text):
        pad = 25
        left,top,right,bottom = draw.textbbox(xy,text, font= font, anchor=anchor)
        bb = [(left-pad,top-pad),(right+pad,top-pad),(right+pad,bottom+pad),(left-pad,bottom+pad)]
        self.boundingbox.append(bb)
        self.predicted.append(text)
    
    def create(self):
        self.txt_layer = Image.new("RGBA", self.base.size, (255, 255, 255, 0))
        bounding_boxes = [[(68, 265), (312, 265), (312, 384), (68, 384)],
                            [(63, 440), (273, 440), (273, 511), (63, 511)],
                            [(75, 520), (595, 520), (595, 599), (75, 599)],
                            [(72, 605), (501, 605), (501, 674), (72, 674)],
                            [(1406, 599), (1762, 599), (1762, 677), (1406, 677)],
                            [(60, 681), (311, 681), (311, 762), (60, 762)],
                            [(224, 762), (481, 762), (481, 844), (224, 844)],
                            [(222, 841), (540, 847), (538, 928), (221, 922)],
                            [(224, 928), (604, 928), (604, 1007), (224, 1007)],
                            [(56, 1017), (306, 1016), (309, 1100), (59, 1101)],
                            [(60, 1095), (654, 1095), (654, 1173), (60, 1173)],
                            [(58, 1173), (388, 1179), (386, 1264), (57, 1257)],
                            [(55, 1258), (648, 1261), (647, 1342), (54, 1339)],
                            [(58, 1336), (543, 1346), (542, 1427), (57, 1417)]]

        pad = 8
        transformed_boxes = []
        for bbox in bounding_boxes:
            transformed_box = [(bbox[0][0] - pad, bbox[0][1] - pad),
                            (bbox[1][0] + pad, bbox[1][1] - pad),
                            (bbox[2][0] + pad, bbox[2][1] + pad),
                            (bbox[3][0] - pad, bbox[3][1] + pad)]
            transformed_boxes.append(transformed_box)

        self.boundingbox = transformed_boxes
        
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
        self.addLabel(draw,font_judul,'mt',(1463,55),provinsi)
        
        draw.text((1463, 149), kabupaten, font=font_judul, fill=(12,42,59,255), anchor='mt')
        self.addLabel(draw,font_judul,'mt',(1463, 149),kabupaten)

        draw.text((703, 280), nik, font=font_nik, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_nik,'lt',(703, 280),nik)

        draw.text((775, 453), nama, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 453),nama)

        draw.text((775, 535), ttl, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 535),ttl)

        draw.text((775, 613), gender, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 613),gender)

        draw.text((1852, 641), golda, font=font_data, fill=(12,42,59,255), anchor='lm')
        self.addLabel(draw,font_data,'lm',(1852, 641),golda)

        draw.text((775, 699), alamat, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 699),alamat)

        draw.text((775, 781), rt_rw, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 781),rt_rw)

        draw.text((775, 861), kelurahan, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 861),kelurahan)

        draw.text((775, 943), kecamatan, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 943),kecamatan)

        draw.text((775, 1023), agama, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 1023),agama)

        draw.text((775, 1109), perkawinan, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 1109),perkawinan)

        draw.text((775, 1187), pekerjaan, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 1187),pekerjaan)

        draw.text((775, 1269), kewarganegaraan, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 1269),kewarganegaraan)


        draw.text((775, 1351), berlaku, font=font_data, fill=(12,42,59,255), anchor='lt')
        self.addLabel(draw,font_data,'lt',(775, 1351),berlaku)


        draw.text((2387, 1227), tempat, font=font_data, fill=(12,42,59,255), anchor='mt')
        self.addLabel(draw,font_data,'mt',(2387, 1227),tempat)

        draw.text((2387, 1313), tgl, font=font_data, fill=(12,42,59,255), anchor='mt')
        self.addLabel(draw,font_data,'mt',(2387, 1313),tgl)

        self.blur()
        self.out = Image.alpha_composite(self.base, self.txt_layer)


    def generate(self):
        n = args.number if args.number != None else self.NUM
        if (self.is_detection):
            os.makedirs(f"{self.detection_path}image/", exist_ok=True)
            os.makedirs(f"{self.detection_path}label/", exist_ok=True)

        if (self.is_recognition):
            os.makedirs(f"{self.recogniton_path}", exist_ok=True)
            rec_label_file = open(f'{self.recogniton_path}_label.txt', 'w+')
        
        for i in range(n):
            self.create()
            self.saltAndPepper()
            self.skew()
            self.save(i)

        if (self.is_recognition):
            rec_label_file.write(self.rec_labels)
            rec_label_file.close()

    def test(self):
        self.create()
        self.saltAndPepper()
        #self.skew()
        self.showBoundingBox()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-t", "--test", action='store_true', help="True for test")
    argParser.add_argument("-n", "--number", type=int, help="Number of generated dataset (default = 10)")
    argParser.add_argument("-s", "--skew", type=int, help="Max skew angle in degree (default= 3, 0 to switch off")
    argParser.add_argument("-b", "--blur", type=float, help="Max gaussian blur radius (default = 1.2, 0 to switch off")
    argParser.add_argument("-sp", "--salt_and_pepper", type=int, help="Salt and pepper density (default = 5000)")
    argParser.add_argument("-dp", "--detection_path", type=str, help="Path to save image (default = detection/)")
    argParser.add_argument("-rp", "--recognition_path", type=str, help="Path to save recognition dataset (default = recognition/)")
    argParser.add_argument("-id", "--is_detection", action='store_true', help="generate detection (default: true)")
    argParser.add_argument("-ir", "--is_recognition", action='store_true', help="generate recognition (default: true)")
    args = argParser.parse_args()

    Generator = KTPGenerator("test.jpg", args=args)

    if args.test == True:
        args.number = 1
        Generator.test()
    else:
        Generator.generate()
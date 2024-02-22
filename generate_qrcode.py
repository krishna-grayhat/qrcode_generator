#  ----------------simple qrcode color----------------------------

# import qrcode as qr

# img = qr.make("https://www.youtube.com/@user-gv6ty3zk4")

# img.save("grayhat_youtube.png")






# ---------------------Stylish qrcode---------------------------

import qrcode

from PIL import Image


qr_link = input("Enter THe link = ")
qr_color = input("Which color do you want in qr = ")
qr_back_color = input("background color for qrcode = ")

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )

qr.add_data(qr_link)

qr.make(fit=True)

img = qr.make_image(fill_color=qr_color,back_color=qr_back_color)

img.save("stylish_qrcode.png")
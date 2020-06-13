import qrcode as qr

s = 'https://www.warmanduterre.com/'

img  = qr.make(s)
img.show()
img.save('qrcode_test.png')

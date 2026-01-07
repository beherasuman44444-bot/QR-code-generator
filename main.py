import qrcode
url = input("enter your url:  ").strip()
fill_path = "C:\\Users\\beher\\OneDrive\\Desktop\\qecode.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(fill_path)
print("Qrcode is generated")
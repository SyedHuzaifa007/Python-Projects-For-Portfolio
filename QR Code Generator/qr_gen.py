import qrcode

# Input Data 
input_data = " "

# Instance Of QR Code 
qr_code = qrcode.QRCode(version = 1, box_size = 10, border = 5)

# Adding Input Data 
qr_code.add_data(input_data)
qr_code.make(fit = True)

# Converting QR Code Into Image

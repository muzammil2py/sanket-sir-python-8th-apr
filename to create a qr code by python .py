import qrcode
# Data to be encoded in the QR code
data = "https://www.youtube.com/@mujjumaggie"
# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)
# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)
# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')
# Save the image to a file
img.save("qr_code.png")
print("QR code generated and saved as 'qr_code.png'")
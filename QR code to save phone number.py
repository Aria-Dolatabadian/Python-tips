import qrcode

# Replace with your actual name, phone number, and email
name = "name"
phone_number = "123456789"
email = "your.email@example.com"

# Create a vCard format string
vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone_number}
EMAIL:{email}
END:VCARD"""

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(vcard)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("contact_qr.png")

print("QR code generated and saved as 'contact_qr.png'")

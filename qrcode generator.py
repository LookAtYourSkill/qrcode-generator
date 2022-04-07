import qrcode as qrcode

input_data = input('Für welchen Link soll ein QR Code generiert werden? :')
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(str(input_data))
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
name = input('Wie soll der QR Code heißen?: ')
img.save('DEN PFAD HIER EINFÜGEN' + str(name) + '.png')
print('QR Code Successfully created\n'
      'Du hast dich für ' + str(input_data) + ' entscheiden!')

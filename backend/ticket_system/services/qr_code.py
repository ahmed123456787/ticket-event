import qrcode



def generate_qr_code(data: str, filename: str):
    return qrcode.make(data).save(filename, 'PNG')
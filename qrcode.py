
from docx import Document
import pyqrcode

def generate_qrcode(data, filename):
    qr = pyqrcode.create(data)
    qr.png(filename, scale=2)

# Usage example
generate_qrcode("Hello, World!", "qr.png")


def save_qr_to_docx(filename):

    # Create a Word document
    doc = Document()
    
    # Add barcode image to the document
    doc.add_picture(filename)

    # Save the document
    doc.save('qr_doc.doc')

 # Usage example
save_qr_to_docx("qr.png")


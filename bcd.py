import tkinter as tk
from PIL import ImageTk, Image
import barcode
from barcode.writer import ImageWriter

def create_receipt_with_barcode():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Bill Receipt with Barcode")

    # Generate the barcode
    barcode_value = "1234567890"
    barcode_image = barcode.Code128(barcode_value, writer=ImageWriter()).render()

    # Save the barcode image to a file
    barcode_image_filename = "barcode.png"
    barcode_image.save(barcode_image_filename)

    # Load the barcode image using PIL
    image = Image.open(barcode_image_filename)

    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)

    # Create a label with the barcode image
    barcode_label = tk.Label(window, image=photo)
    barcode_label.pack(pady=10)

    # Create a label with the barcode value
    value_label = tk.Label(window, text="Barcode Value: " + barcode_value)
    value_label.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Call the function to create the receipt with barcode example
create_receipt_with_barcode()

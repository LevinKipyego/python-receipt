from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

def create_bill(items):
    # Create a sample stylesheet for different font styles
    styles = getSampleStyleSheet()

    # Define custom paragraph styles
    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    content_style = ParagraphStyle(
        "content",
        parent=styles["Normal"],
        fontSize=12,
        leading=14,
        textColor=colors.black
    )

    # Create a list to hold the flowable elements of the document
    elements = []

    # Add a title
    title = Paragraph("Bill", title_style)
    elements.append(title)

    # Add a table for the bill items
    table_data = [["Item", "Quantity", "Price", "Total"]]
    for item in items:
        table_data.append([item["item"], item["quantity"], item["price"], item["total"]])

    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ])

    table = Table(table_data, style=table_style)
    elements.append(table)

    # Create a PDF document
    doc = SimpleDocTemplate("bill.pdf", pagesize=letter)

    # Build the document with the elements
    doc.build(elements)

# Example usage
items = [
    {"item": "Apple", "quantity": 5, "price": 1.25, "total": 6.25},
    {"item": "Banana", "quantity": 3, "price": 0.75, "total": 2.25},
    {"item": "Orange", "quantity": 2, "price": 0.90, "total": 1.80}
]

create_bill(items)
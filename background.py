
from datetime import datetime
from prettytable import PrettyTable


 # Define ANSI escape sequences for formatting
bold = "\033[1m"
underline = "\033[4m"
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
end_format = "\033[0m"

# ...

def make_receipt():
    # ...
    items=[]
    total=0
    while True:
        item=input("Enter item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break

        qty=float(input('quantity:'))
        each=float(input('@:'))
        total= qty * each
        itm={'Item':item,'Quantity':qty,'Each':each,'Total':total}
        items.append(itm)

    text = f"{bold}{green}elgon link tech{end_format}"
    print(f"{bold}{green}elgon link tech{end_format}")
    print('PO BOX 1078 ,KITALE, KENYA')
    print("Mobile:+254713685943,email:cyberpunk123@gmail.com")
    print('\t\t\tCASH SALE')
    print(datetime.now())
    '''print('Item\tQty\tEach\tTotal')
    print('*'*54)
    print(f'{item}\t\t{qty}\t\t{each}\t\t{total}')


    for item in items:
        print(f"{item['Item']}\t\t{item['Quantity']}\t\t{item['Each']}\t\t{item['Total']}")
    '''
    table = PrettyTable()
    table.field_names = ["Item", "Quantity", "Price", "Total"]

    for item in items:
        table.add_row([item["Item"], item["Quantity"], item["Each"], item["Total"]])

        # Set the font style of the table
        table.align = "l"  # Align the text to the left
        table.header_style = "upper"  # Convert header to uppercase
        table.format = True  # Enable formatting
        # Get the table as a string
        # table_string = table.get_string()


    # Open a file in write mode
    with open('receipt.doc', 'w') as f:
        # Redirect the standard output to the file
        import sys
        sys.stdout = f

        print(f"{bold}{green}elgon link tech{end_format}", file=f)
        print('PO BOX 1078 ,KITALE, KENYA', file=f)
        print("Mobile:+254713685943,email:cyberpunk123@gmail.com", file=f)
        print('\t\tCASH SALE', file=f)
        print(datetime.now(), file=f)
        print(table, file=f)
        # ...

        # Redirect the standard output back to the console
        sys.stdout = sys.__stdout__

    # Print a message to indicate the file has been created
    print("Receipt saved as receipt.txt")


make_receipt()








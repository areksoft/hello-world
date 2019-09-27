print("""      Areksoft Technologies
      Level-1, Phoenix Building, Uppal,
      Telangana, India.500039
      Phone: +91 9398949451
      Email: info@areksoft.com""")

print("""Bill To
       Customer Name
       Customer Address
       Phone""")

grandTotal = []
items_Description = []
items_SlNo = []
items_Quantity = []

amount = int(input('Sl No: '))
if amount>=1:
    itemsDesc = input("Enter the item name")
    items = int(input('Enter the price '))
    items_Description.append(itemsDesc)
    grandTotal.append(items)
    print()
amount = int(input('Sl No: '))
for n in range(amount):
    itemsDesc = input("Enter the item name")
    items = int(input('Enter the price '))
    items_Description.append(itemsDesc)
    grandTotal.append(items)
    print()
print(items_Description,grandTotal)
subtotal = sum(grandTotal)
print("Subtotal = ",subtotal)
discount = int(input("Enter the discount"))
discountAmount = subtotal-discount
GSTpercentage = int(input("GST is %"))
GST = discountAmount * GSTpercentage/100
Total = discountAmount+GST
print(Total)
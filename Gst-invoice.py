print("""      Areksoft Technologies
      Level-1, Phoenix Building, Uppal,
      Telangana, India.500039
      Phone: +91 9398949451
      Email: info@areksoft.com""")

print("""Bill To
       Customer Name
       Customer Address
       Phone""")

n = int(input("Entert the rows"))
def details():
    global s, x, y, z
    s = int(input("Enter the Sl.No"))
    x = input("Enter the Description")
    y = input("Enter the Quantity")
    z = int(input("Enter the amount"))

details()

print("SL.No -",s,"| Description -",x,"| Quantity -",y,"|Amount -",z,"|")
subtotal = z
Discount = int(input("Enter the discount"))
print("Discount = ",Discount)
ADisc = z - Discount
GST = ADisc * 18/100
Taxes = GST
print("Including GST =", Taxes)
Total = ADisc + Taxes
print("Total Amount = ",Total)
Paid = int(input("Enter the paid amount"))
Balance = Total - Paid
print("Balance Amount =",Balance)





# calculating vat/tax/gst

def add_vat(price,vat_rate):
    return price * (vat_rate/100)


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10) + price
    print(f"Original: {price}, Final with VAT: {final_amount}")

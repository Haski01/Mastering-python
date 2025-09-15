# put of order

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if "Out of Stock" in flavour:
        continue
    if "Discontinued" in flavour:
        print(f"{flavour} item found")
        break

    print(f"{flavour} item found")
    
print(f"Out side of loop")
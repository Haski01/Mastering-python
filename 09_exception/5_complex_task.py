class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"ginger": 30,"masala": 40, "clove": 90}

    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} is not available")
        
        if not isinstance(cups,int):
            raise InvalidChaiError("Cup must be in number")

        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")

    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you! visiting again...")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
bill("clove", 5)
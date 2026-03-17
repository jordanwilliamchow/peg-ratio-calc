def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def peg_ratio():
    print("\nPEG Ratio Calculator:")
    price_per_share = input("\nType in price per share.\n$")
    while is_float(price_per_share) == False:
        price_per_share = input("\nA number was not typed in. Please tpye in price per share.\n$")
    growth_rate = input("\nType in expected growth rate.\n%")
    while is_float(growth_rate) == False:
        growth_rate = input("\nA number was not typed in. Please tpye in a expected growth rate.\n%")
    peg = f"{(float(price_per_share) / float(growth_rate)):.2f}"
    print("\nThe PEG ratio is: " + peg + ".\n")
peg_ratio()




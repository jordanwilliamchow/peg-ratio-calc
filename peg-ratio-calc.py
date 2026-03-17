def peg_ratio():
    print("\nPEG Ratio Calculator:")
    price_per_share = float(input("\nType in price per share.\n"))
    growth_rate = float(input("\nType in expected growth rate.\n"))
    peg = f"{(price_per_share / growth_rate):.2f}"
    print("\nThe PEG ratio is: " + peg + ".\n")
peg_ratio()




# Fuction for check of numbers
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function for PEG ratio calculation and user inputs
def peg_ratio():
    print("\nPEG Ratio Calculator:")
    # User input for price per share
    price_per_share = input("\nType in price per share.\n$")
    while is_float(price_per_share) == False:
        price_per_share = input("\nA number was not typed in. Please tpye in price per share.\n$")
    # User input for growth rate
    growth_rate = input("\nType in expected growth rate.\n%")
    while is_float(growth_rate) == False:
        growth_rate = input("\nA number was not typed in. Please tpye in a expected growth rate.\n%")
    # Check if there is a dividend
    dividend_checker = input("\nIs there a dividend? YES or NO?\n").lower()
    while dividend_checker != "yes" and dividend_checker != "no":
        dividend_checker = input("\nThis is not a  valid input, please state if there is a dividend? YES or NO?\n")
    if dividend_checker == "yes":
        # User input for for dividends
        dividends = input("\nType in a dividend.\n%")
        while is_float(dividends) == False:
            dividends = input("\nA number was not typed in. Please tpye in a dividend, if none input 0.\n%")
    elif dividend_checker == "no":
        dividends = 0
    # Calculation of PEG ratio
    peg = f"{(float(price_per_share) / (float(growth_rate) + float(dividends))):.2f}"
    print("\nThe PEG ratio is: " + peg + ".\n")

# Call the function
peg_ratio()




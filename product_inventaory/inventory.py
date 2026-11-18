def calculate_total_price(price,quantity):
    if price<0:
        raise ValueError("Price cannot be negative")
    if quantity<0:
        raise ValueError("Quantity cannot be negative")
    return price*quantity
def apply_discount(total,disc_perc):
    if total<0 :
        raise ValueError("Total cannot be negative")
    if not 0<=disc_perc<=100:
        raise ValueError("Discount Percent must be between 0 to 100")
    return total*disc_perc/100
def check_stock(available,requested):
    if available<0 or requested <0:
        raise ValueError("Stock cannot be negative")
    if available >= requested:
        return "Stock is available"
    else:
        raise ValueError("Stock is not available ")
if __name__=="__main__":
    tp=calculate_total_price(500,4)
    print(f"Total Price : {tp:.2f}")
    disc_price=apply_discount(2000,10)
    print(f"Discount Amount : {disc_price:.2f}")
    check_stock(10,8)

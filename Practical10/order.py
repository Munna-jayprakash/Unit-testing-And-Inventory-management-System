def calculate_discount(price,discount):
    if price <0:
        raise ValueError("Price cannot be negative")
    if not 0<= discount <=100:
        raise ValueError("Discount must be between 0 to 100")
    return price*discount/100
def calculate_gst(price,gst_rate):
    if price<0:
        raise ValueError("Prie cannot be negative")
    if not 0<=gst_rate<=100:
        raise ValueError("GST must be between 0 to 100")
    return price*gst_rate/100
def calculate_ordeer_total(price ,discount ,gst_rate ):
    dis_amt=calculate_discount(price,discount)
    dis_price=price-dis_amt
    gst_amt=calculate_gst(dis_price,gst_rate)
    return dis_price+gst_amt
if __name__=="__main__":
    total=calculate_ordeer_total(1000,10,10)
    print(f"Final order amount :₹{total:.2f}")

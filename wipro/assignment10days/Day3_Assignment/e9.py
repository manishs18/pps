'''
9.  The policy followed by a company to process customer orders is given by the following rules:
    (a) If a customer order is less than or equal to that in stock and has credit is OK, supply has requirement.
    (b) If has credit is not OK do not supply. Send him intimation.
    (c) If has credit is Ok but the item in stock is less than has order, supply what is in stock. Intimate to him data the balance will be shipped.
'''


def process_order(order):
    if not order["credit_status"]: 
        return "Order cannot be processed: Credit not OK. Intimation sent to the customer."
    elif order["order_quantity"] <= order["stock"]:
        return f"Order processed: Supplied {order['order_quantity']} units."
    else: 
        return (f"Partial order processed: Supplied {order['stock']} units. "
                f"Balance of {order['order_quantity'] - order['stock']} units will be shipped later.")

def main():
    order_quantity = int(input("Enter the quantity ordered: "))
    stock = int(input("Enter the available stock: "))
    credit_status = input("Is credit OK? (yes/no): ") == "yes"

    order = {
        "order_quantity": order_quantity,
        "stock": stock,
        "credit_status": credit_status
    }

    result = process_order(order)
    print(result)

main()

from customer import Customer


def main():
    print('Welcome to Wake-Mart.')
    print('Please register.')
    name = str(input('Enter your name:'))
    customer1 = Customer(name)
    customer1.input_cards_info()
    print('Registration completed. ')
    items_total = scan_prices()
    total_coupons = scan_coupons()
    total_to_pay = items_total - total_coupons
    print('Please pay this amount: $', total_to_pay)
    make_payment(customer1, total_to_pay)


def read_price_list():

    print('')
    print('Price list:')
    input_file = open('price_list.txt', 'r')
    line = input_file.readline()
    master_list_master = []
    for line in input_file:
            price_list1 = []
            price_list2 = []
            master_list = []
            number = line
            price_list1.append(number[0:4])
            price_list2.append(number[5:9])
            master_list = price_list1 + price_list2
            master_list_master.append(master_list)
            tuple_price1 = tuple(price_list1) + tuple(price_list2)
            print(tuple_price1)

    input_file.close()
    master_list_master_dic = dict(master_list_master)
    return master_list_master_dic


def scan_prices():
    master_list_master_dic = read_price_list()
    print('')
    item_selected = ''
    value_price = 0.0
    total = 0.0
    while item_selected != '9999':
        item_selected = str(input("Enter 4-digit item code [or 9999 to stop]: ") )
        if item_selected in master_list_master_dic.keys():
            print('Item found. Price:$', master_list_master_dic[item_selected])
            value_price = float(master_list_master_dic[item_selected])
            total = total + value_price
        else:
            print('Item is not here ')
    print('this is the total of items you selected', total)
    return total


def read_coupons_list():
    print('')
    print('Coupon list:')
    input_file = open('coupon_list.txt', 'r')
    line = input_file.readline()
    master_list_master = []
    for line in input_file:
            coupon_list1 = []
            coupon_list2 = []
            master_list = []
            number = line
            coupon_list1.append(number[0:4])
            coupon_list2.append(number[5:9])
            master_list = coupon_list1 + coupon_list2
            master_list_master.append(master_list)
            tuple_price1 = tuple(coupon_list1) + tuple(coupon_list2)
            print(tuple_price1)
    input_file.close()
    master_list_master_dic = dict(master_list_master)
    return master_list_master_dic


def scan_coupons():
    master_list_master_dic = read_coupons_list()
    print('')
    coupons_selected = ''
    value_price = 0.0
    total = 0.0
    while coupons_selected != '9999':
        coupons_selected = str(input("Enter 4-digit coupon code [or 9999 to stop]: ") )
        if coupons_selected in master_list_master_dic.keys():
            print('Coupon found. Value: $', master_list_master_dic[coupons_selected])
            value_price = float(master_list_master_dic[coupons_selected])
            total = total + value_price
        else:
            print('Coupon not found ')
    print('this is the total of coupons you selected', total)
    return total


def make_payment(customer1, amount_due):
    print('')
    print("Payment options:")
    payment = int(input("Enter 1 for Credit Card, 2 for debit Card:"))
    while payment == 1:
        three_security_code = str(input('Please enter 3-digit security code: : '))
        test = customer1.verify_credit_card(three_security_code)
        if test == 2:
            print('Security code incorrect. Payment rejected.')
            print('Please choose payment method.')
            payment = int(input("Enter 1 for Credit Card, 2 for debit Card:"))
        elif test == 1:
            last_four_digits_card = customer1.credit_card_last_four()
            print('result back to main of last four cc', last_four_digits_card)
            print('The amount of $ ', amount_due,' will be charged to card number ending with ', last_four_digits_card)
            exit()
    while payment == 2:
        four_digit_pin = str(input('Please enter 4-digit PIN : '))
        test1 = customer1.verify_debit_card(four_digit_pin)
        if test1 == 1:
            last_four_digits_card = customer1.debit_card_last_four()
            print('The amount of $ ', amount_due,' will be charged to card number ending with ', last_four_digits_card)
            exit()
        elif test1 == 2:
            print('PIN incorrect. Payment rejected.')
            print('Please choose payment method.')
            payment = int(input("Enter 1 for Credit Card, 2 for debit Card:"))

main()



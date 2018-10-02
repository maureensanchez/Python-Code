class Customer:

    def __init__(self, customer_name):

        """ constructor of class Car """

        self.__name = customer_name
        self.__credit_card_num = ''
        self.__credit_security_code = ''
        self.__debit_card_num = ''
        self.__debit_pin = ''

    def input_cards_info(self):

        """ User enters payment methods information """

        self.__credit_card_num = input('Enter credit card number : ')
        self.__credit_security_code = input('Enter 3-digit security code :')
        self.__debit_card_num = input('Enter debit card number: ')
        self.__debit_pin = input('Enter 4-digit PIN :')


    def verify_credit_card(self, three_security_code ):

        if three_security_code == self.__credit_security_code:
            check = 1
        else:
            check = 2
        print(check)
        return check

    def verify_debit_card(self, four_digit_pin):

        if four_digit_pin == self.__debit_pin:
            check = 1
        else:
            check = 2
        return check

    def credit_card_last_four(self):

        last_four = self.__credit_card_num[-4:]
        print(last_four)
        return last_four

    def debit_card_last_four(self):

        last_four = self.__debit_card_num [-4:]
        return last_four



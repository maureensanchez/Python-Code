from cards import Cards


class CreditCard(Cards):

    def __init__(self,card_number, customer_name ):
        super().__init__(card_number, customer_name)
        self.__interest_rate = 0.0
        self.__credit_limit = 0

    def input_info(self):
        self.__interest_rate = (input("Enter interest rate: "))
        self.__credit_limit = (input("Enter credit limit: "))

    def display_info(self):
        print("Interest rate: ", self.__interest_rate)
        print("Credit Limit: ", self.__credit_limit)


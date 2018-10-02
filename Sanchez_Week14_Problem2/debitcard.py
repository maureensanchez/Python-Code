from cards import Cards


class DebitCard(Cards):

    def __init__(self, card_number, customer_name):
        super().__init__(card_number, customer_name)
        self.__pin = 0.0
        self.__fund_available = 0

    def input_info(self):
        self.__pin = (input("Enter PIN:  "))
        self.__fund_available = (input("Enter fund available:  "))

    def display_info(self):
        print("PIN: ", self.__pin)
        print("Available fund: : ", self.__fund_available)

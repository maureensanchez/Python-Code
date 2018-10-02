class Cards:

    def __init__(self, card_number, customer_name):
        self.__id = card_number
        self.__name = customer_name

    def display_id_name(self):
        print("Card number: ", self.__id)
        print("Name: ", self.__name)

    def input_info(self):
        raise NotImplementedError("Method input_info not implemented")

    def display_info(self):
        raise NotImplementedError("Method display_info not implemented")


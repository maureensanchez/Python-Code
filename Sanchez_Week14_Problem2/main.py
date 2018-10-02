from creditcards import CreditCard

from debitcard import DebitCard


def main():

    card_number = str(input("Enter card number: "))
    customer_name = str(input("Enter name: "))
    choice = int(input("Enter 1 for credit card, 2 for debit card:"))
    if choice == 1:
        customer1 = CreditCard(card_number, customer_name)
        customer1.input_info()
        customer1.display_id_name()
        customer1.display_info()
    elif choice == 2:
        customer1 = DebitCard(card_number, customer_name)
        customer1.input_info()
        customer1.display_id_name()
        customer1.display_info()

main()

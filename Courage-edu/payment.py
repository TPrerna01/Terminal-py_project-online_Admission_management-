from query import ExeQueries
from datetime import datetime

class Payment:
    def __init__(self):
        self.queryhandler = ExeQueries()

    def payment(self):
        ad_id = 'admission_id'
        admission_id = self.queryhandler.get_last_user_id('admission', column = ad_id)
        while True:
            print("\nTo get the admission its compulasuary to pay.\n")
            try:
                card = input("Enter card number [16 digit]:")
                amount = int(input("Enter the payment : "))
                if len(card) != 16:
                    print("\nInvalid card  number : \n")
                    break
                payment_date = datetime.now()
            except :
                print("\nInvalid input\n")

            if card and amount:
                    payment_data = {'admission_id' : admission_id, 'amount': amount, 'payment_date': payment_date }
                    try:
                        # user_id = self.queryhandler.select_data('user')
                        self.queryhandler.insert_data('payment', payment_data)
                        print("\nPayment Successful\n")

                        break
                    except Exception as e:
                        print(f"\nError occurred while inserting feedback: {e}\n")
            else:
                print("\nAll the fields must be filled correctly\n")

    

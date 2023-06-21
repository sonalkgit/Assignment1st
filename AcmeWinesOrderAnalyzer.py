import re
from datetime import datetime
import sys
import csv

class Orders:

    def __init__(self, order_id, user):
            self.order_id = order_id
            self.users = user
#class users 
class Users:
     
     #constructor
     def __init__(self,state,zip_code,date_str,email):
        self.date_str = date_str
        
        self.email = email
        self.zip_code = zip_code
        self.state = state

     #method to check valid state or not
     # No wine can ship to New Jersey, Connecticut, Pennsylvania, Massachusetts, Illinois, Idaho or Oregon 
     def is_restricted_state(self,state):
         RESTRICTED_STATES = ["NJ", "CT", "PA", "MA", "IL", "ID", "OR"]
         if state not in RESTRICTED_STATES:
            return True
         return False
     
     #method to check valid zip code or not
     #Wine can not ship to any zipcode that has two consecutive numbers next to each other

     def check_consecutive_numbers(self,zip_code):
        
         for i in range(len(zip_code) - 1):
                if int(zip_code[i]) + 1 == int(zip_code[i+1]) or int(zip_code[i]) - 1 == int(zip_code[i+1]):
                    return True  # Found two consecutive numbers
         return False
     
     #Wine can not ship to anyone born on the first Monday of the month.
     def is_first_monday(self,date_str):
                
            date = datetime.strptime(date_str, "%m/%d/%Y")
                
            return date.weekday() == 0 and date.day <= 7
     
     #Everyone ordering must be 21 or older
     def is_21_or_older(self,date_str):
        birth_date = datetime.strptime(date_str, "%m/%d/%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age >= 21
    
     #Email address must be valid
     def is_valid_email(self,email):
                
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(email_regex, email) is not None

#AcmeWines class
class AcmeWines:
     def __init__(self,orders_file):
        self.orders_file = orders_file
        self.valid_orders = []
        self.invalid_orders = []

     #this function process the orders 
     def process_orders(self):
            
            with open(self.orders_file, 'r') as file_in:
                reader = csv.reader(file_in)
                next(reader)  # Skip header row
                
                #iterating each row from csv file
                for row in reader:
                    id = row[0]
                    state = row[4]
                    zip_code = row[5]
                    birthday = row[2]
                    email = row[3]

                    user = Users( state, zip_code, birthday, email)

                    
                    order = Orders(id, user)

                    #appending order data to valid or invalid order list
                    if not self.is_valid_order(order):
                        self.invalid_orders.append(order.order_id)
                    else:
                        self.valid_orders.append(order.order_id)

     #method to validate order 
     def is_valid_order(self, order):
              #user_obj = Users()
              if order.users.is_valid_email(order.users.email) and order.users.is_restricted_state(order.users.state) and \
                    not order.users.is_first_monday(order.users.date_str) and order.users.is_21_or_older(order.users.date_str) and \
                    not order.users.check_consecutive_numbers(order.users.zip_code): 
                   
                   return True
              return False
     
     #writing data to csv files 
     def save_results(self):
                with open('valid.csv', 'w') as valid_file:
                    valid_file.write('\n'.join(self.valid_orders))

                with open('invalid.csv', 'w') as invalid_file:
                    invalid_file.write('\n'.join(self.invalid_orders))
        
if __name__ == '__main__':
    
    
    if len(sys.argv) < 2:
        print("please provide the input file name")
    
    orders_file = sys.argv[1]
    analyzer = AcmeWines(orders_file)

    analyzer.process_orders()
    analyzer.save_results()

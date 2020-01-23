'''
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        octa = oct(i)[2:]
        hexa = hex(i)[2:]
        bina = bin(i)[2:]
        print(f"{i}  {octa}  {hexa}  {bina}")

    

if __name__ == '__main__':
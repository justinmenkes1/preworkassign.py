#Question One
def hello_name(username):
    """Display a simple greeting."""
    print("hello_" + username + "!")
hello_name("USERNAME")

def first_odds():
    odd_numbers = list(range(1,100,2))
    print(odd_numbers)
first_odds()

def max_num_in_list(a_list):
    a_list = [1,2,3,4,5,6,7,8,9,10]
    max_num= max(a_list)
    return(max_num)
    
print(max_num_in_list)



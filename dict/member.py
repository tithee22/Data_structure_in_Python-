#Checking Membership in a Dictionary

def check(dict):
    for key, value in dict.items():
        if value=="momo":
            print('value "momo" exists in the dictionary')
            break
    else:
        print('value "momo" does not exist in the dictionary')
   
# Example dictionary
new_dic = {'name': 'momo', 'age': 28 }

check(new_dic)



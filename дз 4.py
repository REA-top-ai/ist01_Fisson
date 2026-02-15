first_name = 'Виталий'
last_name = 'Красилов'
# new_account = last_name[5:]
# print(new_account)
# temp_password = last_name[2:6]
# print(temp_password)
def account_generation(first_name, last_name):
    return first_name[:3] + last_name[:3]
new_account = account_generation(first_name, last_name)
print(new_account)



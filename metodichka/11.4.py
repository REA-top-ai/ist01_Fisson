dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_i_want = 'dalmatian'
for i in dog_breeds_available_for_adoption:
    print(i)
    if i == dog_breed_i_want:
        print('У них есть собака, которую я хочу')
        break

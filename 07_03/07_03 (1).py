contains_a = lambda word: 'a' in word
print(contains_a('apple'))

long_string = lambda s: len(s) > 12
print(long_string('apple'))

end_in_a = lambda s: s[-1] == 'a' if len(s) > 0 else False
print(end_in_a('apple'))

even_or_odd = lambda num: "четное" if num % 2 == 0 else "нечетное"
print(even_or_odd (9))

multiple_of_three = lambda num: "кратное трем" if num % 3 == 0 else "не кратное"
print(multiple_of_three(10))

rate_movie = lambda rating: "Мне понравился этот фильм" if rating > 8.5 else "Этот фильм был не очень хорошим"
print(rate_movie(9.2))

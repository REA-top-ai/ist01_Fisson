def repeat_stuff(stuff, num_repeats):
   print()
repeat_stuff("Row", 3)

def repeat_stuff(stuff, num_repeats):
        return stuff * num_repeats

def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats
lyrics = repeat_stuff("Row", 3) + "Your Boat."
print("lyrics:", lyrics)
song = repeat_stuff("Row")
print("song:", song)
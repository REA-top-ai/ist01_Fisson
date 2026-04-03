def get_force(train_mass, train_acceleration):
    return train_mass*train_acceleration
train_mass = 22680
train_acceleration = 10
train_force = get_force
print(train_force)
print(f"Поезд GE поставляет {train_force} ньютонов силы")

def get_energy(mass, c = 3 * 10**8):
    return mass * c**2
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print(f'1 кг бомбы составляют {bomb_energy} Джоулей')


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")


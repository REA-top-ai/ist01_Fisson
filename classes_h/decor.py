from functools import wraps


def is_alive(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.health <= 0:
            print(f"{self.name} мертв и не может действовать!")
            return None
        return func(self, *args, **kwargs)

    return wrapper


def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        result = func(self, *args, **kwargs)
        print(f"[LOG] Действие завершено")
        return result

    return wrapper


def easter_health_boost(factor=2):
    def decorator(cls):
        original_init = cls.__init__

        @wraps(cls)
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.original_max_health = self.health
            self.health = int(self.health * factor)
            print(f"[EVENT] Пасхальное событие! Здоровье {self.name} увеличено в {factor} раз! Теперь: {self.health}")

        cls.__init__ = new_init
        return cls

    return decorator


def easter_mana_boost_for_mage(extra_mana=5):
    def decorator(cls):
        original_init = cls.__init__

        @wraps(cls)
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            if self.hero_class == "волшебник":
                self.original_mana = self.mana
                self.mana += extra_mana
                print(f"[EVENT] Священный посох! Мана {self.name} увеличена на {extra_mana}! Теперь: {self.mana}")

        cls.__init__ = new_init
        return cls

    return decorator


def critical_hit(chance=0.3):
    import random
    def decorator(func):
        @wraps(func)
        def wrapper(self, damage, *args, **kwargs):
            if random.random() < chance:
                damage = damage * 2
                print(f"[CRITICAL] {self.name} наносит КРИТИЧЕСКИЙ урон! x2!")
            return func(self, damage, *args, **kwargs)

        return wrapper

    return decorator


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        if hero_class == "волшебник":
            self.health = 60
            self.mana = 50
        elif hero_class == "воин":
            self.health = 100
            self.mana = 10
        else:
            raise ValueError("Класс героя должен быть 'волшебник' или 'воин'")

        self.spells_names = {}
        self.items = {}

    @is_alive
    def attack(self, damage):
        print(f"{self.name} нанес урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Теперь здоровья: {self.health}")

    @is_alive
    def cast_spell(self, spell_name):
        if spell_name not in self.spells_names:
            print(f"{self.name} не знает заклинание {spell_name}")
            return

        spell = self.spells_names[spell_name]

        if self.mana < spell['mana_cost']:
            print(f"Недостаточно маны! Нужно: {spell['mana_cost']}, есть: {self.mana}")
            return

        self.mana -= spell['mana_cost']

        if spell['attack_damage'] > 0:
            print(f"{self.name} применил {spell_name} и нанес {spell['attack_damage']} урона!")

        if spell['health_increase'] > 0:
            self.health += spell['health_increase']
            print(f"{self.name} применил {spell_name} и восстановил {spell['health_increase']} здоровья!")

        print(f"Осталось маны: {self.mana}")

    def add_spell(self, spell_name, mana_cost, attack_damage=0, health_increase=0):
        self.spells_names[spell_name] = {
            'mana_cost': mana_cost,
            'attack_damage': attack_damage,
            'health_increase': health_increase
        }
        print(f"{self.name} выучил заклинание {spell_name}!")

    def add_item(self, item_name, param, value):
        if len(self.items) >= 6:
            print(f"Нельзя добавить больше 6 предметов!")
            return

        self.items[item_name] = {param: value}

        if param == "здоровье":
            self.health += value
            print(f"{self.name} надел {item_name} +{value} к здоровью!")
        elif param == "мана":
            self.mana += value
            print(f"{self.name} надел {item_name} +{value} к мане!")

        if param == "здоровье":
            print(f"Теперь здоровья: {self.health}")
        elif param == "мана":
            print(f"Теперь маны: {self.mana}")


@easter_health_boost(factor=2)
@easter_mana_boost_for_mage(extra_mana=5)
class EasterHero(Hero):
    pass


print("=" * 50)
print("ОБЫЧНЫЕ ГЕРОИ")
print("=" * 50)

mage = Hero("Гэндальф", "волшебник")
warrior = Hero("Арагорн", "воин")

mage.add_spell("Огненный шар", 20, 35, 0)
mage.add_spell("Лечение", 15, 0, 25)
warrior.add_spell("Мощный удар", 5, 30, 0)

print("\n--- Обычный волшебник ---")
print(f"Здоровье: {mage.health}, Мана: {mage.mana}")
mage.cast_spell("Огненный шар")
mage.heal(20)
mage.attack(15)

print("\n--- Обычный воин ---")
print(f"Здоровье: {warrior.health}, Мана: {warrior.mana}")
warrior.cast_spell("Мощный удар")
warrior.attack(25)

print("\n--- Проверка декоратора is_alive ---")
warrior.health = 0
warrior.attack(10)
warrior.cast_spell("Мощный удар")

print("\n" + "=" * 50)
print("ПАСХАЛЬНЫЕ ГЕРОИ (С БОНУСАМИ)")
print("=" * 50)

easter_mage = EasterHero("Пасхальный Гэндальф", "волшебник")
easter_warrior = EasterHero("Пасхальный Арагорн", "воин")

easter_mage.add_spell("Пасхальное яйцо", 10, 50, 30)
print(f"\nЗдоровье: {easter_mage.health}, Мана: {easter_mage.mana}")
easter_mage.cast_spell("Пасхальное яйцо")

print(f"\nЗдоровье воина: {easter_warrior.health}, Мана воина: {easter_warrior.mana}")

print("\n" + "=" * 50)
print("ДОБАВЛЕНИЕ ПРЕДМЕТОВ")
print("=" * 50)
easter_mage.add_item("Кольцо здоровья", "здоровье", 20)
easter_mage.add_item("Амулет маны", "мана", 15)

print("\n" + "=" * 50)
print("ИТОГОВЫЕ ПАРАМЕТРЫ")
print("=" * 50)
print(f"Пасхальный волшебник - Здоровье: {easter_mage.health}, Мана: {easter_mage.mana}")
print(f"Пасхальный воин - Здоровье: {easter_warrior.health}, Мана: {easter_warrior.mana}")
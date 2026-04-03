from datetime import datetime

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def calculate_programmer_bonus():
    bonuses = []
    for employee in employees:
        if "программист" in employee[1]:
            bonus = employee[3] * 0.03
            bonuses.append([employee[0], bonus])
    return bonuses

def calculate_holiday_bonus():
    bonuses = []
    for employee in employees:
        if employee[1] in ["Менеджер", "Аналитик", "Ведущий программист", "Старший аналитик", "Архитектор"]:
            bonuses.append([employee[0], 2000])
        else:
            bonuses.append([employee[0], 2000])
    return bonuses

def calculate_indexation():
    current_date = datetime.now()
    indexation_results = []
    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        years_worked = (current_date - hire_date).days / 365
        if years_worked > 10:
            indexation = employee[3] * 0.07
        else:
            indexation = employee[3] * 0.05
        indexation_results.append([employee[0], indexation])
    return indexation_results

def vacation_schedule():
    current_date = datetime.now()
    vacation_list = []
    for employee in employees:
        hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
        months_worked = (current_date - hire_date).days / 30
        if months_worked > 6:
            vacation_list.append(employee[0])
    return vacation_list

print("Премия программистам (3%):")
for bonus in calculate_programmer_bonus():
    print(f"{bonus[0]}: {bonus[1]} руб.")

print("\nПремия к 8 марта и 23 февраля (2000 руб.):")
for bonus in calculate_holiday_bonus():
    print(f"{bonus[0]}: {bonus[1]} руб.")

print("\nИндексация зарплат:")
for indexation in calculate_indexation():
    print(f"{indexation[0]}: {indexation[1]} руб.")

print("\nСотрудники для отпуска (более 6 месяцев):")
for employee in vacation_schedule():
    print(employee)
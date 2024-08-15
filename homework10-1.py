from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створюємо модель
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Задаємо змінні
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

# Цільова функція - максимізація виробництва (кількість лимонаду + кількість фруктового соку)
model += lemonade + fruit_juice, "Total Products"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water constraint"
model += 1 * lemonade <= 50, "Sugar constraint"
model += 1 * lemonade <= 30, "Lemon juice constraint"
model += 2 * fruit_juice <= 40, "Fruit puree constraint"

# Розв'язуємо задачу
model.solve()

# Виведення результатів
lemonade_value = value(lemonade)
fruit_juice_value = value(fruit_juice)
total_products = lemonade_value + fruit_juice_value

print(f"Optimal amount of lemonade to produce: {lemonade_value}")
print(f"Optimal amount of fruit juice to produce: {fruit_juice_value}")
print(f"Total products produced: {total_products}")

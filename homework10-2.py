import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2

# Візуалізація результатів
def visualize_results(x_random, y_random, density):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)
    ax.scatter(x_random, y_random, color="red", s=1)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) від {a} до {b}\nКількість точок: {density}")
    
    plt.grid()
    plt.show()

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo(a, b, num_samples):
    # Генерація випадкових точок
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Кількість точок під кривою
    under_curve = np.sum(y_random < f(x_random))

    # Площа під кривою
    area_under_curve = (b - a) * f(b) * under_curve / num_samples

    # Обчислення інтеграла за допомогою функції quad
    result, error = spi.quad(f, a, b)

    print(f"Площа обчислена методом Монте-Карло: {area_under_curve}")
    print(f"Площа обчислена функцією quad: {result}")
    print(f"Похибка: {abs(area_under_curve - result)}")

    visualize_results(x_random, y_random, num_samples)

if __name__ == "__main__":
    # Запуск для різної кількості точок
    for density in [100, 1000, 10000, 100000]:
        print(f"\n\tResults for points amount: {density}")
        monte_carlo(a, b, density)

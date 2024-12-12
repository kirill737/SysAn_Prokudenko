import json

# Вычисляет степень уверенности
def calc_membership(value, membership_func):
    for i in range(len(membership_func) - 1):
        x0, y0 = membership_func[i]
        x1, y1 = membership_func[i + 1]
        if x0 <= value <= x1:
            return y0 if y0 == y1 else y0 + (y1 - y0) * (value - x0) / (x1 - x0)
    return 0

# Выполняет фаззификацию
def fuzzify(input_val, fuzzy_sets):
    membership_vals = {}
    for label, points in fuzzy_sets.items():
        membership_vals[label] = round(calc_membership(input_val, points), 2)
    print(f"Фаззификация значения {input_val}: {membership_vals}\n")
    return membership_vals

# Сопоставляет входные термы выходным с учётом переходной таблицы
def map_to_output(input_membership, transition_rules):
    output_membership = {}
    for input_label, input_mu in input_membership.items():
        output_label = transition_rules[input_label]
        if output_label in output_membership:
            output_membership[output_label] = max(output_membership[output_label], input_mu)
        else:
            output_membership[output_label] = input_mu
    print(f"Сопоставление на выходное множество: {output_membership}\n")
    return output_membership

# Объединяет функции принадлежности выходных термов
def combine_outputs(output_membership, output_sets):
    combined_points = []
    for label, mu in output_membership.items():
        points = output_sets[label]
        for x, y in points:
            combined_points.append((x, min(mu, y)))
    return combined_points

# Выполняет дефаззификацию методом центра тяжести
def mamdani_defuzzify(points):
    aggregated = {}
    for x, y in points:
        if x in aggregated:
            aggregated[x] = max(aggregated[x], y)
        else:
            aggregated[x] = y
    numerator = sum(x * y for x, y in aggregated.items())
    denominator = sum(y for y in aggregated.values())
    return numerator / denominator if denominator != 0 else 0

# Основной алгоритм управления с использованием метода Мамдани
def main(temp_data: str, reg_data: str, rules_data: str, input_temp: float):
    temp_sets = json.loads(temp_data)
    reg_sets = json.loads(reg_data)
    rules_map = json.loads(rules_data)

    # Фаззификация
    temp_membership = fuzzify(input_temp, temp_sets)
    # Сопоставление термов
    reg_membership = map_to_output(temp_membership, rules_map)
    # Агрегация выходных функций принадлежности
    combined = combine_outputs(reg_membership, reg_sets)
    # Дефаззификация
    final_value = mamdani_defuzzify(combined)
    print(f"Итоговое значение после дефаззификации: {final_value}\n")
    return final_value

temperatures = """{
    "холодно": [
        [0, 1],
        [16, 1],
        [20, 0],
        [50, 0]
    ],
    "комфортно": [
        [16, 0],
        [20, 1],
        [22, 1],
        [26, 0]
    ],
    "жарко": [
        [0, 0],
        [22, 0],
        [26, 1],
        [50, 1]
    ]
}"""

regulator = """{
    "слабо": [
        [0, 1],
        [6, 1],
        [10, 0],
        [20, 0]
    ],
    "умеренно": [
        [6, 0],
        [10, 1],
        [12, 1],
        [16, 0]
    ],
    "интенсивно": [
        [0, 0],
        [12, 0],
        [16, 1],
        [20, 1]
    ]
}"""

transition = """{
    "холодно": "интенсивно",
    "комфортно": "умеренно",
    "жарко": "слабо"
}"""

print("--Тест с холодной температурой--")
main(temperatures, regulator, transition, 10)

print("--Тест с умеренной температурой--")
main(temperatures, regulator, transition, 20)

print("--Тест с жаркой температурой--")
main(temperatures, regulator, transition, 30)

count = 0
value_1 = 0
while True:
    value_user = int(input("Enter value: "))
    if value_user > 0:
        value_1 += value_user
        count += 1
    elif value_user == 0 and value_1 == 0 and count == 0:
        print("Первый ввод не должен быть равен 0")
    else:
        print(f"Average value: {value_1 / count}")
        break


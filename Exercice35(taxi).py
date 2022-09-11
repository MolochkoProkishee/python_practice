import constant
price_base = constant.PRICE_BASE_RATE
price_extra_meter = constant.PRICE_EXTRA_METERS
extra_meter = constant.EXTRA_METERS
def all_price (distace):
    x = price_base + (distace / extra_meter * price_extra_meter)
    return round(x, 2)
user_enter = all_price(float(input("Введите расстояние которе вы проехали в км: ")))
print(f"Ваша стоимость составила: {user_enter} $")

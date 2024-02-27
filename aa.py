def rental_car_cost(d):
    total = 40 * d
    if d >= 7:
        total = total - 50
        return total
    elif d >= 3:
        total = total - 20
        return total
    return total


print(rental_car_cost(4))

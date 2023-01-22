# Task 2G -

# / Def hotel_cost(night) |  Hotel p/n = £140  | hotel_cost return 140*nights
# // Def plane_ride_cost(str(city)) | Function return

def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return 0


def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20

    return cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print(trip_cost("Los Angeles", 5, 600))

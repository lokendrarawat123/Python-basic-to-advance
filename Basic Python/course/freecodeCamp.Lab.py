distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = False

# 1. Sabai vanda paila falsy value check garne
if not distance_mi:
    print(False)

# 2. Distance 1 mile vanda kam vaye
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

# 3. Distance 1 vanda mathi tara 6 vanda kam vaye
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# 4. Distance 6 vanda mathi vaye
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
import secrets

def generate_secure_lottery():
    pool = list(range(1, 36))
    main_numbers = []
    
    for _ in range(5):
        index = secrets.randbelow(len(pool))
        main_numbers.append(pool.pop(index))
    
    main_numbers.sort()
    bonus_number = secrets.randbelow(10) + 1
    
    return main_numbers, bonus_number

# ५० वटा Set जेनेरेट गर्नका लागि:
total_sets = 50

print(f"--- Generating {total_sets} Secure Lottery Sets ---\n")

for i in range(1, total_sets + 1):
    main_nums, bonus_num = generate_secure_lottery()
    print(f"Set {i:02d}: Main {main_nums} | Bonus: [{bonus_num}]")
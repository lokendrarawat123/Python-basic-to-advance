def create_character(name, strength, intelligence, charisma):
    # 1. Name Type Validation
    if not isinstance(name, str):
        # Test 2 check
        return "The character name should be a string"
    
    # 2. Empty Name Validation
    if name == "":
        # Test 4 check
        return "The character should have a name"
    
    # 3. Name Length Validation
    if len(name) > 10:
        # Test 6 check
        return "The character name is too long"
    
    # 4. Spaces in Name Validation
    if " " in name:
        # Test 8 check
        return "The character name should not contain spaces"

    # Stats lai list ma rakhne validate garna sajilo hunchha
    stats = [strength, intelligence, charisma]

    # 5. Stats Type Validation
    for s in stats:
        # Test 10 check: Ensures they are integers and NOT booleans
        if not isinstance(s, int) or isinstance(s, bool):
            return "All stats should be integers"

    # 6. Minimum Stat Value Validation
    for s in stats:
        # Test 12 check
        if s < 1:
            return "All stats should be no less than 1"
            
    # 7. Maximum Stat Value Validation
    for s in stats:
        # Test 14 check
        if s > 4:
            return "All stats should be no more than 4"

    # 8. Total Points Validation
    # Test 16 check
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # 9. Successful Output Generation (Test 18 & 19)
    str_line = "STR " + ("●" * strength) + ("○" * (10 - strength))
    int_line = "INT " + ("●" * intelligence) + ("○" * (10 - intelligence))
    cha_line = "CHA " + ("●" * charisma) + ("○" * (10 - charisma))

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"
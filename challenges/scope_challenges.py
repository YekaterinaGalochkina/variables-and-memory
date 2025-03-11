def challenge_01():
    # 1 local
    outer_value = 42
    print(f"The value from outside is: {outer_value}")
    

def challenge_02():
    # 2 global
    print(f"The value from outside is: {outer_value}")


def challenge_03():
    # 3 The variable is not declared, so it gives an error
    print(f"The value from outside is: {inner_value}")
    inner_value = 42


def challenge_04():
    # 4 Same variable name as global, declared locally after variable was used, -> error
    print(f"The value from outside is: {outer_value}")
    outer_value = 42

outer_value = 1729
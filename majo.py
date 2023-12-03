def reassign(fx: int) -> None:
    print(f"{fx = }, {id(fx) = }")
    fx = 10
    print(f"{fx = }, {id(fx) = }")


x = 5
print(f"{x = }, {id(x) = }")
reassign(x)
print(f"{x = }, {id(x) = }")
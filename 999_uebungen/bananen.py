haufen = 4  # 13, 40, 121
for _ in range(3):
    haufen = (haufen - 1) * 2 / 3
    print(int(haufen))

# (ursprungshaufen - 1) * 2/3
# das passiert 3 mal


# 4, 7, ?


# Probe:
# probe = 4
# for _ in range(4):
#     if probe % 3 == 1:
#         probe = probe - ((probe - 1) / 3)
#         print(probe)


# Lösung Jana
# def bananen_min():
#     x = 1
#     while  True:
#       anzahl, gültig = x, True
#       for i in range(4):
#         if (anzahl - 1) % 3: break
#         anzahl = (anzahl - 1) * 2 // 3
#       else:
#         return x
#       x += 1

# print (" Die mindeste Anzahl von Bananen ist:",bananen_min() )
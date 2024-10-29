haufen = 4  # 13, 40, 121
for _ in range(3):
    haufen = ((haufen / 2) * 3) + 1
    print(int(haufen))

# (ursprungshaufen - 1) * 2/3
# das passiert 3 mal


# 4, 7, ?



# Probe:
# haufen2 = x
# for _ in range(4):
#     if haufen2 % 3 == 1:
#         haufen2 = haufen2 - ((haufen2 - 1) / 3)
#         print(haufen2)

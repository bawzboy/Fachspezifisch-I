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

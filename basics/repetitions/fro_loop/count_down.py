print("How far are we from the cave?")
distance = int(input())
for steps in range(distance, 0, -1):# 0, -1 count backwords
    print(f"{steps} steps remaing")

print("We have reached the cave!")
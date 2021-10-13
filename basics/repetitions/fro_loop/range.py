print("What level of brightness is required?")
level = int(input())
print("\nAdjusting brightness....\n")
for brightness in range(2,level + 1, 2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Boop's brightness level: {'*' * brightness}")

print()
print("Adjustment complete!")

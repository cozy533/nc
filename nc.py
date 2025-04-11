#!/usr/bin/env python3

nums = []
totals = {}

print("\nEnter numbers. To stop, enter an empty line.")

while(True):
    num = input("-> ")
    try:
        num = int(num)
    except ValueError:
        try:
            num = float(num)
        except ValueError:
            if(num == ''):
                print("Done.")
                break
            else:
                print(f"Skipping invalid input: '{num}'")
                continue

    nums.append(num)

    # Show progress
    print(nums)

nums.sort()

for num in nums:
    count = nums.count(num)
    totals[num] = count

print(f"\nTotal numbers: {len(nums)}")
print(f"Total unique numbers: {len(totals)}\n")

for num, count in totals.items():
    print(f"{num}: {count}")

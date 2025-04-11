#!/usr/bin/env python3

nums = []
totals = {}

print("\nBegin entries. To delete the last entry, enter 'del'. To stop, enter an empty line.")

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
            elif(num == 'del'):
                try:
                    nums.pop()
                except IndexError:
                    print('No entries currently exist.')
                    continue
                print(nums)
                continue
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

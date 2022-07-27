if __name__ == '__main__':
    with open('./modules/data/first_code.txt') as f:

        depths = [int(line) for line in f]
        print(len(depths))
        print(depths)

# part 1
count = 0
previous_depth = None
for d in depths:
    if previous_depth:
        if d > previous_depth:
            count+=1
    previous_depth = d
print("Part one:Depth increased {} times".format(count))
print(f"Part one:Depth increased {count} times")          

# part 2
averaged_depths = []
i = 0
while i < len(depths)-2:
    averaged_depths.append(depths[i] + depths[i+1] + depths[i+2])
    i+=1

count = 0
previous_depth = None
for d in averaged_depths:
    if previous_depth:
        if d > previous_depth:
            count+=1
    previous_depth = d
print("Depth increased {} times".format(count))  


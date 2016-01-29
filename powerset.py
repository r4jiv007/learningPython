complete_set = [1,2,3,4,5]
#binary_counts = ['000', '001', '010', '011', '100', '101', '110', '111']

binary_counts =list()
length = 2 ** 5
    
for dummy_bin in range(length):
    binary_counts.append(bin(dummy_bin)[2:])

power_set = set([()])
for count in binary_counts:
    power_set.add(tuple([complete_set[i] for i in range(len(count))
                         if count[i] == '1']))

print power_set


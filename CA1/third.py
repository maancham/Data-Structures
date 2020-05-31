size_of_input = input()
gene = input()
Agene = gene.count('A')
Cgene = gene.count('C')
Tgene = gene.count('T')
Ggene = gene.count('G')
default = len(gene)/4
extra_list = []
extra_list.append(['A',Agene - default])
extra_list.append(['C',Cgene - default])
extra_list.append(['T',Tgene - default])
extra_list.append(['G',Ggene - default])


def check_array(temp_arr):
    positives = 0
    equals = True
    for i in extra_list:
        if (i[1] > 0):
            positives += 1
            new_count = temp_arr.count(i[0])
            if(new_count < i[1]):
                equals = False
    if (equals):
        return True
    else:
        return False

f = 0
l = 0
min_len = 10000

while (f < int(size_of_input)):

    while (l < int(size_of_input)):
        temp_arr = gene[f:l]
        if (check_array(temp_arr)):
            break
        l += 1

    if(l >= int(size_of_input)):
        break

    while (check_array(temp_arr)) :
        temp_arr = gene[f:l]
        if(min_len > len(temp_arr)):
            min_len = len(temp_arr)
        f += 1

print(min_len+1)



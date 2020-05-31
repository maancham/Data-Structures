def check_equality(shortest_word,word_inventory, index):
    if index >= len(shortest_word):
        return False
    goal_char = shortest_word[index]
    for i in word_inventory:
        temp_str = i[index]
        if(temp_str.lower() != goal_char.lower()):
            return False
    return True

def find_recursive(shortest_word,word_list,k):
    global result
    if(check_equality(shortest_word,word_list,k)):
        result += word_list[0][k]
        find_recursive(shortest_word,word_list,k+1)
    return result

result = ''
n = int(input())
word_list = list(input().split())
shortest_word = min((word for word in word_list if word), key=len)
final = find_recursive(shortest_word,word_list,0)
if (final == ''):
    print("NULL")
else:
    print(final)





def civil_minor(n , starting, ending, temp): 
    if n == 1:
        print(starting,ending) 
        return
    civil_minor(n-1, starting, temp, ending)
    print(starting,ending) 
    civil_minor(n-1, temp , ending, starting) 
          
n = input()
Carriers = []
Carriers.append('A')
Carriers.append('C')
Carriers.append('B')
civil_minor(int(n),Carriers[0],Carriers[1],Carriers[2])


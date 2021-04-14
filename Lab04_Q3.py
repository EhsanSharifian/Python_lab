#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 3.1
a = []
a.append(95102051)
a.append("Pouria")
b = []
b.append(95109156)
b.append("Rouzbeh")
c = list()
c.append(95101774)
c.append("Faraz")


print(a)
print(b)
print(c)
T = []
T.append(a)
T.append(b)
T.append(c)
print(T)
print(T[0][0])
print(T[0][1])
print(T[1][1])
print(T[2][0])


# In[8]:


# 3.2

a = ()
a = a + (95102051 ,"Pouria")

b = ()
b = b + (95109156,"Rouzbeh")

c = ()
c = c + (95101774, "Faraz")


print(a)
print(b)
print(c)
T = ()
T = (a,) + (b,) + (c,)

print(T)
print(T[0][0])
print(T[0][1])
print(T[1][1])
print(T[2][0])


# In[14]:


# 3.3
def getDistance(Table,x,y):
    distance = 0
    num_rows = len(Table)        
    num_cols = len(Table[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if Table[i][j] == 1:
                distance = abs(i-x) + abs(j-y) + distance
    return distance

def getMassCenter(Table):
    num_rows = len(Table)        
    num_cols = len(Table[0])
    distance_matrix = [[0]*num_cols for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            distance_matrix[i][j] = getDistance(Table,i,j)


    min_dist = min(min(distance_matrix))

    flag = False
    for i in range(num_rows):
        for j in range(num_cols):
            if distance_matrix[i][j] == min_dist:
                print("The center is [" + str(i) + "," + str(j) + "]")
                flag = True
                break
        if (flag):
            break
            
                
Table = [[1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0]]

getMassCenter(Table)


# In[22]:


# 3.4

nation = ['Roman','Egypt','Greek','Chinese','Islamic','Mayan','Persian','Mongol']
golden_age = ['27BC-1453AD','3150BC-30BC','800BC-600AD','221BC-1912AD',
              '750AD-1257AD','2000BC-1540AD','550BC-651AD','1206AD-1368AD']

zip_list = list(zip(nation, golden_age))
print(zip_list)
print("\n")


zip_dictionary = dict(zip(nation, golden_age))
print(zip_dictionary)
print("\n")

print(zip_dictionary['Persian'])


# In[23]:


# 3.5

a = [2**i for i in range(17)]
print(a)

b = [x*x for x in range(1,5)]
print(b)

c = [a[x] for x in b if x % 2 == 0]
print(c)


# In[24]:


# 3.6

a = [[(x+i)*(x+i) for i in range(0,3)] for x in range(0,9,3)]
print(a)


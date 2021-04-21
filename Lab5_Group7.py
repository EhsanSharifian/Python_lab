#!/usr/bin/env python
# coding: utf-8

# # Lab5
# ## Group 7
# 
# ## 1
# ### 1.1

# In[1]:


def fibonacci(n = 10):
    nums = [0 , 1]
    i = 2
    while len(nums) < n:
        nums.append(nums[i - 1] + nums[i - 2])
        i += 1
    return nums

n = input("Please enter n: ")
print("without input:",fibonacci())
print("with input:", fibonacci(int(n)))


# ### 1.2

# In[2]:


def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))
l = [4]
print("Before reassign: arr={}".format(l))
reassign(l)
print("After reassign: arr={}".format(l))


# In[3]:


def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))
l = [4]
print("Before append_one: arr={}".format(l))
append_one(l)
print("After append_one: arr={}".format(l))


# ### 1.3

# In[4]:


lst = [1,2,3]
def func():
    lst.append(4)
func()
print(lst)


# In[5]:


lst = [1,2,3]
def func():
    lst = lst + [4]
func()
print(lst)


# ### 1.4

# In[6]:


def search(goal, i, j, visited):
    visited.append((i,j))
    if goal == '':
        return True
    else:
        a = False
        b = False
        c = False
        d = False
        if i > 0:
            if goal[0] == Table[i - 1][j] and (i - 1, j) not in visited:
                a = search(goal[1:], i - 1, j, visited[:])
        if i < xsize - 1:
            if goal[0] == Table[i + 1][j] and (i + 1, j) not in visited:
                b = search(goal[1:], i + 1, j, visited[:])
        if j > 0:
            if goal[0] == Table[i][j - 1] and (i, j - 1) not in visited:
                c = search(goal[1:], i, j - 1, visited[:])
        if j < ysize - 1:
            if goal[0] == Table[i][j + 1] and (i, j + 1) not in visited:
                d = search(goal[1:], i, j + 1, visited[:])
        return a or b or c or d


Table = ["ABCE",
         "SFCS",
         "ADEE"]
xsize = len(Table)
ysize = len(Table[0])
word = input("please enter the word: ") 

flag = False
for i in range(xsize):
    for j in range(ysize):
        if Table[i][j] == word[0]:
            if search(word[1:],i,j,[]):
                flag = flag or True
                
print(flag)


# ### 1.5

# In[7]:


def cost(fuel, position):
    if position == N + 1:
        return 0
    
    future_fuel = fuel - F * (D[position + 1] - D[position])
    A = (C - fuel) * P[position] + cost(C - F * (D[position + 1] - D[position]), position + 1)
    
    if future_fuel < 0:
        return A
    
    B = cost(future_fuel, position + 1)
    return min(A,B)



C = 50
F = 0.1
N = 5
D = [0,300,450,700,900,1100,1200]
P = [0,1100,1500,900,2100,1300]

print(cost(50,0))


# ## 2
# ### 2.1

# In[8]:


round5 = lambda x :  5 * round(x / 5)
print(round5(3))
print(round5(193.3))
print(round5(22.5))


# ### 2.2

# In[9]:


names = [['Pouria', 'fatemi'], ['Ehsan', 'Sharifian'], ['Faraz', 'Farahvash'],['Rouzbeh', 'ghaderi'] ]

[(lambda name : name[0] + ' ' + name[1]) (item) for item in names]


# ## 3

# ### 3.1

# In[10]:


import Pouria
n = input("Please enter a number: ")
Pouria.square(int(n))


# In[11]:


from Pouria import square
n = input("Please enter a number: ")
square(int(n))


# ### 3.2
# 
# #### explaned in PyCharm

# ## 4
# ### 4.1

# In[12]:


file = open("python_lab.txt","w")
file.write("Pouria Fatemi")
file.close()
file = open("python_lab.txt","a")
file.write("\n95102051")
file.close()

file = open("python_lab.txt","r")
print(file.read())


# In[13]:


file = open("python_lab.txt","r")
print(file.readlines())


# ### 4.2

# In[14]:


import os
if not os.path.isdir('./input_files'):
    os.mkdir('./input_files')
file = open("./input_files/python_lab.txt","w")   
file.write("Pouria Fatemi")
file.close()
file = open("./input_files/python_lab.txt","r")
print(file.read())
file.close()


# ### 4.3

# In[15]:


with open('class_names.txt', 'r') as file: 
    if os.path.isfile('./newclass_names.txt'):
        os.remove('./newclass_names.txt')
    for line in file.readlines(): 
        print(line, end = '')
        temp = line.split(" ")
        new_data = " ".join([temp[1].rstrip("\n"), temp[0], "\n"])
        with open('newclass_names.txt', 'a') as f:
            f.write(new_data)


# In[16]:


file = open("newclass_names.txt","r")
print(file.read())
file.close()


# ### 4.4

# In[17]:


import csv
with open('files/data.csv', 'r') as file:
    if os.path.isfile('./newdata.csv'):
        os.remove('./newdata.csv')
    for line in csv.reader(file):
        with open('newdata.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=' ')
            writer.writerow(line[1:])


# In[18]:


with open('newdata.csv', 'r') as file:
    print(file.read())


# ### 4.5
# #### 1.1

# In[ ]:


import re

path = '/usr/src/linux-headers-4.15.0-122'
regex = '(.*c$)|(.*py$)'

for root, dirs, files in os.walk(path):
    for file in files:
        res = re.match(regex, file)
        if res:
            if res.group(1):
                print(file)
            if res.group(2):
                print(file)


# #### 1.2

# In[19]:


import re
pattern = re.compile("^GNU")
with open("./files/GPL-3", 'r') as file:
    for line in file.readlines():
        for match in re.finditer(pattern, line):
            print(line)


# In[20]:


pattern = re.compile("cept")
with open("./files/GPL-3", 'r') as file:
    for line in file.readlines():
        for match in re.finditer(pattern, line):
            print(line)


# In[21]:


pattern = re.compile('\([^)]*\)')
with open("./files/GPL-3", 'r') as file:
    for line in file.readlines():
        for match in re.finditer(pattern, line):
            print(match.group(0))


# #### 1.3

# In[22]:


regex = '^#.*\n?'

with open("./files/sqspell.php", 'r') as file:
    for line in file.readlines():
        print(re.sub(regex, '', line))


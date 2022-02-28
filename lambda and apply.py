# 单个参数的：
# one parameter
g = lambda x : x ** 2
print(g(3))
# output
# 9
"""This represent a function
def g(x):
    return x**2
print(g(3))
"""

# 多个参数的：
# multi-parameters
g = lambda x, y, z : (x + y) ** z
print(g(1,2,2))
# output
# 9
"""This represent a function
def g(x):
    return x**2
print(g(3))
"""
def g(x, y, z):
    return (x + y) ** z
print(g(1, 2, 2))

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
"""
output:
[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

print(list(map(lambda x: x not in [3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])))
"""
output:
[True, True, False, False, False, False, False, False, False]
"""

#
# apply
#
import pandas as pd

df = pd.DataFrame([['A',23,'M'],['B',24,'F'],['C',35,'M']],columns=['Name','age','gender'],index=['1','2','3'])
print(df)
f1 = lambda x:x.max()
print(df.apply(f1))
print(df.max())
f2 = lambda x: x == 'A'
print(df.apply(f2, axis=0))
# DataFrame.drop(labels=None,axis=0, index=None, columns=None, inplace=False)
# axis 默认为0，指删除行，因此删除columns时要指定axis=1；
# axis = 0: row axis = 1:col
"""
output
  Name  age gender
1    A   23      M
2    B   24      F
3    C   35      M
Name       C
age       35
gender     M
dtype: object
Name       C
age       35
gender     M
dtype: object
    Name    age  gender
1   True  False   False
2  False  False   False
3  False  False   False
"""
df = pd.DataFrame([['A',23,'M'],['B',24,'F'],['C',35,'M'],
                   ['D',33,'M'],['E',23,'F'],['F',21,'F'],
                   ['G',25,'M'],['H',26,'F'],['I',24,'M']],
                  columns=['Name','age','gender'],
                  index=['1','2','3','4','5','6','7','8','9'])
print(df['gender'])
print(df['gender'].apply(lambda x: 'F' in x))
print(sum(df['gender'].apply(lambda x: 'F' in x)))
"""
for i in range(len(df)):
    if df['Name'][i] == 'A':
        df['Name'][i] = 'Z'
"""
# ↓ has the same results as ↑ for loop
df['Name'] = df['Name'].apply(lambda x: x if x != 'A' else 'Z')
print(df)
"""
output
1    M
2    F
3    M
4    M
5    F
6    F
7    M
8    F
9    M
Name: gender, dtype: object
1    False
2     True
3    False
4    False
5     True
6     True
7    False
8     True
9    False
Name: gender, dtype: bool
4
  Name  age gender
1    Z   23      M
2    B   24      F
3    C   35      M
4    D   33      M
5    E   23      F
6    F   21      F
7    G   25      M
8    H   26      F
9    I   24      M
"""

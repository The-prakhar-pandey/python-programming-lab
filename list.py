lst=[101,102,999,1,10000]
a=lst[0]
for i in lst:
    if a>i:
        a=i
print(lst)
print(a)

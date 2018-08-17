# DATA TYPES
#1
n=int(input("enter no.of elements you want to insert in list "))
l1=[ ]#create empty list
for i in range (n):
            b=input()
            l1.append(b)
print('list1 =' ,l1)

#2
#Add the given list to above created list: ['google','apple','facebook','microsoft','tesla'] 
l2= ['google','apple','facebook','microsoft','tesla']
l1.extend(l2)
print('new list1  =' ,l1)

#3
l3=['red','orange','green','blue','red','white','red','pink','green']
print('list3 =', l3)
c=l3.count('red')
print("count of 'red' is ",c)

#4
l4=[4,56,24,11,89,123,54,76,32]
print('list4 =',l4)
l4.sort()
print('Sorted list4 =',l4)

#5
l5=[4,12,56,90]
l6=[5,18,80]
l7=[ ]
l7=l5+l6
l7.sort()#merge l5 and l6 to new list l7
print('Sorted list7 after merging list5 and list6 =',l7)

#6
#Stack follows a particular order that could be last in first out 
stack =[ ] #stack using list
stack.append(10)
stack.append(82)
stack.append(68)
stack.append(44)
stack.append(66)
print('stack after appending elements =',stack)
stack.pop()
stack.pop()
print('stack after removing last two elements =',stack)

#in  Queue  insertion and deletion happens at different ends”
queue =[ ] #Queue using list
queue.append(10)
queue.append(82)
queue.append(68)
queue.append(44)
queue.append(66)
print('queue after appending elements =',queue)
queue.pop(0)
queue.pop(0)
print('queue after removing first two elements =',queue)
queue.remove(44)
print('queue after removing specific element =',queue)

#7
#cout even and odd numbers in list
l8=[34,45,12,17,99,567,80,77,89,80,43]
o=0#counts odd numbers
e=0#counts even numbers
for i in range (len(l8)):
    if(l8[i]%2==0):
        e+=1
    elif(l8[i]%2!=0):
            o+=1
print('no.of even numbers in list  = ', e)
print('no.of odd numbers in list  = ', o)
            






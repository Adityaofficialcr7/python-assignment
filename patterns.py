#!/usr/bin/env python
# coding: utf-8

# In[1]:


s= "aditya"
print(s[1])


# In[2]:


s[2]


# In[ ]:





# In[3]:


s[2:4]


# In[4]:


s[4:0:-1]


# In[6]:


s[5::-1]


# In[7]:


s


# In[8]:


for i = s :
    print(i)
    


# In[57]:


n=5
for i in range(n,0,-2):
    print (i )
    


# In[30]:


s= "my name is aditya"
b= len(s)
range(b)


# In[74]:


n=5
for i in range(0, n):
    for j in range (n, i, -1):
        print("+", end="  ")
    print("\r")   


# In[123]:


n= 7
for i in range(0,n):
    for j in range(0,i):
        print(end=" ")
    for j in range(n,i,-1):
        print ("*", end=" ")
        
    print("\r")
    


# In[146]:


n= 5


# In[112]:


n= int(input("enter the no. of rows"))

i=1
while(i<=n):
    j=n
    while(j>i):
        print(" ",end=" ")
        j=j-1
    while(j<=i):
        print("*",end=" ")
 


# In[145]:


n= int(input("enter the no of rows"))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    
    for j in range(0,2*i-1):
        print("*",end=" ")
    print("\r") 


# In[140]:


n= int(input("enter the no of rows"))

for i in range(0,n):
 
    for j in range(n,i+1,-1):
        print(end=" ")
    
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r") 


# In[132]:


for j in range(5,4,-1):
    print("n")


# In[136]:


range(5)


# In[137]:


range(,5)


# In[ ]:





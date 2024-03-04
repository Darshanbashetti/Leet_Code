# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

num1=[1,2,3,0,0,0]
num2=[2,5,6]
num=[]
ans=[]
for i in num1:
    if i!=0:
        num.append(i)
for i in num2:
    if i!=0:
        num.append(i)
for i in range(1,len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print(num)

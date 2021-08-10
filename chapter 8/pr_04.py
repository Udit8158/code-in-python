# Date:10/08/2021
# sum(n)=sum(n-1)+n
def sum_recursive(n):
    if n==0 or n<0:
        return 0
    return n+ sum_recursive(n-1)
print(sum_recursive(-4))
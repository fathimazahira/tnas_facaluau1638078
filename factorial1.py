def fact_rec(n):
 if(n==0 or n==1):   
  return 1 
 else:
   return n*fact_rec(n-1)
number=int(input(&quot;enter a value&quot;))
res=fact_rec(number)
print(&quot;The factorial of {} is {}.&quot;.format(number,res))

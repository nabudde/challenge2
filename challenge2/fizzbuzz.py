def fizzbuzz(x,y):
    z=x+y
    t=len(z)
    if not isinstance(x,list) and isinstance(y,list):
        return "invalid input"
    if t % 3 == 0 : 
        return "fizz"
    if t % 5 == 0 :
        return "buzz"
    if ( t % 3 ==0  and t % 5 == 0 ):
        return"fizzbuzz"
        return len(z)  
fizzbuzz(x=[1,2,3,4],y=[5,6,7,8,9])
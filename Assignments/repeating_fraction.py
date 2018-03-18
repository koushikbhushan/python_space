from math import gcd
def rep_fraction(num,den):
    factor=gcd(num,den)
    num=num/factor
    den=den/factor
    
    x=int(num//den)
    rem = num%den
    dec=str(x)
    fraction = ''
    decimal_dict = {}
    sigma = ''
    tau = ''
    if rem == 0:
        #No fraction
        return dec,sigma,tau
    
    counter = 0
    repeats = False
    while True:
        if (rem in decimal_dict):
            break
        repeats=True
        decimal_dict[rem]=counter
        num = rem*10
        x=int(num//den)
        rem=num%den
        fraction=fraction+str(x)
        counter = counter+1
        if rem == 0:
            repeats=False
            break
    if repeats:
        #There is repeating fraction 
        tau_index = decimal_dict[rem]
        sigma = fraction[:tau_index]
        tau = fraction[tau_index:]       
    else:
        #No repeating fraction
        sigma=fraction
        
    return dec,sigma,tau    

if __name__=='__main__':
    dec,sigma,tau=rep_fraction(97,99)
    ans = dec+'.'+sigma+tau
    print('Answer is: ',ans)
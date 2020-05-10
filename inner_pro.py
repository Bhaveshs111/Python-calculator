responses = ["welcome to a smart calculator", "my name is Bhavesh but you can call me as SB.", "Thanks",
             "sorry, this is beyond my ability"]


def FindNumFromText(text):
    lst = []
    index = 0
    
    for i in text.split(' '):
        try:
            lst.append(float(i))
            index += 1
        
        except ValueError:
            pass
    
    return (lst)


def lcm(lst):
    big = max(lst)
    
    while big <= mul(lst):
        s = 0
        for i in lst:
            if big % i == 0:
                s += 1
                if s == len(lst):
                    return (big)
        big += 1


def hcf(lst):  # GCD
    small = min(lst)
    
    while small >= 1:
        s = 0
        for i in lst:
            if i % small == 0:
                s += 1
                if s == len(lst):
                    return (small)
        small -= 1
        
def facto(lst):
  n=lst[0]
  ans=fact(n)
  return ans

  def fact(n)
    if n==1:
      return 1
    else:
    return fact(n-1)*n
  
  




def sum(lt):
    s = 0
    for i in lt:
        s += i
    return (s)


def largest(lst):
    big = max(lst)
    return (big)


def sub(lt):
    s = (lt[0] - lt[1])
    return (s)


def mul(lst):
    m = 1
    for i in lst:
        m *= i
    return (m)


def div(lst):
    return (lst[0] / lst[1])


def TOH(lst):
    def toh(n,t1,t2,t3):
         if n > 0:
            toh(n-1,t1,t3,t2)
            print(f"move: t{t1} to t{t3}")
            toh(n-1,t2,t1,t3)
    toh(lst[0],1,2,3)


def name():
    print(responses[1])


def end():
    print(responses[2])
    input('please enter a key to exit:')
    exit()


def sorry():
    print(responses[3])


operation = {'LARGEST': largest,"TOH":TOH,'BIGGEST': largest, 'LCM': lcm, 'HCF': hcf,'FACTORIAL':facto,
             'SUM': sum, 'SUMMATION': sum, 'ADD': sum, 'SUBTRACTION': sub, 'SUBTRACT': sub, 'MINUS': sub,
             'MULTIPLICATION': mul, 'MULTIPLY': mul, 'DIVISION': div, 'DIVIDE': div}
command = {'NAME': name, 'EXIT': end, 'CLOSE': end, 'END': end}


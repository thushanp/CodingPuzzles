
cons   = lambda el, lst: (el, lst)
mklist = lambda *args: reduce(lambda lst, el: cons(el, lst), reversed(args), None)
car = lambda lst: lst[0] if lst else lst
cdr = lambda lst: lst[1] if lst else lst
nth = lambda n, lst: nth(n-1, cdr(lst)) if n > 0 else car(lst)
length  = lambda lst, count=0: length(cdr(lst), count+1) if lst else count
begin   = lambda *args: args[-1]
display = lambda lst: begin(w("%s " % car(lst)), display(cdr(lst))) if lst else w("nil\n")

class Node: 
  def __init__(self, cargo=None, next=None): 
    self.car = cargo 
    self.cdr = next    
  def __str__(self):
    return str(self.car)  

def display(lst):
  if lst:
    w("%s " % lst)
    display(lst.cdr)
  else:
    w("nil\n")

alpha = Node()
alpha.car = "test"

alpha.cdr = beta


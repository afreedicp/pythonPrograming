
def freq(s):
     "takes a string and return the number of each character in it"
     dict={}
     for i in s:
          if i in dict:
               dict[i]+=1
          else:
               dict[i]=1
     return dict 

 
def panagram(q):

     for i in "qwertyuiopasdfghjklzxcvbnm":
          if i not in q:
               return False
     return True                   

def avrg(g):
     sum=0
     if len(g)==0:
          return None 
     for i in g:
          sum=sum+i
     return sum/len(g)
          
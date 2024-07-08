# class student:
#  collageName = "ABC"
#  def setData (self,roll,name):
#     self.roll=roll;
#     self.name=name;
#     def showData(self):
#          print(student.collageName)
#         print (self.roll)
#         print(self.name)\

#         print(student.CollageName)
# s1=student()
# print(s1.collageName)
# s1.setData(1,"amit")

# s2=student()
# s2.setData(2,"vishal")
# s1.showData()
# s2.showData()
 


#  #static method
# class student:
#     a=3
#     @staticmethod
#     def msg():
#         print(student.a)

# student.msg()
# s1=student()
# s1.msg()
                        

# #single lvl inheritance
# class A : 
#    def display(self):
#       print(self.a)

#       obj=b()
#       obj.display()    

# #multilvl inheritance
#       class A:
#          a=10
#          class b(A):
#             b=20
#             classc(b):
#             def display(self):
#                print(self.a)
#                print(self.b)

#                obj=C()
#                obj.display)()



#hierarchical inheritance
class P:
   x=10

class c1(P):
    def display(self):
        print(P.x)

class C2(p):
    def display(self):
        print(P.x)
    
obj1= C1()
obj2=c2()
obj1.display()
obj2.display()



   #multiple inheritance
#    class P1

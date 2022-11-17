class Point:

    printed_per="*" #it's a variable
    def __init__(self,intix,intiy):
        self.x=intix
        self.y=intiy
    
    def graph(self):

        row=[]

        size=max(int(self.x),int(self.y))+2

        for j in range(size):

            if (j+1) ==int(self.y):
                special_row= str((j+1)%10)+" "+ self.printed_per
                row.append(special_row)
            else:
                row.append(str((j+1)%10))
            
        row.reverse()

        extra_row= ""
        for i in range(size):
            extra_row += str(i%10)
        row.append(extra_row)

        return "\n".join(row)


p1=Point(10,12)
p2=Point(2,5)

print(p1.graph())
print("\nNow P2 \n")
print(p2.graph())



        

            



        




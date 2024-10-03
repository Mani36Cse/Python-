class SubfieldsInAI():
    AI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
    @classmethod
    def Subfields(cls):
        print("Sub-fields in AI are:")
        for a in cls.AI:
            print(a)
            
    def OddEven():
        c=int(input("Enter the number :"))
        if (c%2)==0:
            b=f"{c} is even number"
        else:
            b=f"{c} is odd number"
        return b
        
    def Elegible():
        h=int(input("Enter 1 for Male, Enter 2 for Female :"))
        g=int(input("Enter your age :"))
        if (h == 1 and g >= 21) or (h == 2 and g >= 18):
            print("Your ELIGIBLE")
        else:
            print("Not ELIGIBLE")
            
    def percentage(sub_1,sub_2,sub_3,sub_4,sub_5):
        s=sub_1+sub_2+sub_3+sub_4+sub_5
        per=(s/500)*100
        print("Toatl :",s)
        print("percentage :",per)
        
    def triangle(Height1,Height2,Breadth):
        total=Height1+Height2+Breadth
        k="Perimeter of Triangle: "
        return k+str(total)
    
    def tr(Height,Breadth):
        h=(Height*Breadth)/2
        g="Area of Triangle: "
        return g+str(h)
class Picture:
    def __init__(self,d,w,h,c):
        self.__description = d #string
        self.__width = w #integer
        self.__height = h #integer
        self.__framecolor = c #string
    def getdescription(self):
        return self.__description
    def getwidth(self):
        return self.__width
    def getheight(self):
        return self.__height
    def getframecolor(self):
        return self.__framecolor
    def setdescription(self,d):
        self.__description= d

ar=[]
for i in range(100):
    ar.append(Picture("",0,0,""))
def readdata(ar):
    count=0
    try:
            with open("Pictures.txt","r") as f1:
                d=f1.readline()
                while d!= "":
                    w = f1.readline()
                    h = f1.readline()
                    c = f1.readline()
                    ar[count]=Picture(d,w,h,c)
                    count+=1
                    d = f1.readline()
                f1.close()


    except:
        print("File not found")
    return (count)
PictureCount=readdata(ar)
print("What are your requirements for a picture? Enter the color frame, max width, max height in this order")
c=(input("Enter color of frame"))
w=int(input("What is the max width:"))
h=int(input("What is the max height:"))



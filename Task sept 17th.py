c=1
choice = ["Reading Books", "Play Computer Games", "Sports", "Programming", "Watching TV"]
t = [0, 0, 0, 0, 0]
while c != 0:
    print("1.Reading Books")
    print("2.Play Computer Games")
    print("3.Sports")
    print("4.Programming")
    print("5.Watching TV")
    c = int(input("Enter a choice, 0 TO END."))
    if (c > 5 or c < 1) and c!=0:
        print("invlaid choice, pick a choice between 1-5")
        c = int(input("Enter a choice, 0 TO END."))

    if c == 1:
        t[0] = t[0] + 1
    if c == 2:
        t[1] = t[1] + 1
    if c == 3:
        t[2] = t[2] + 1
    if c == 4:
        t[3] = t[3] + 1
    if c == 5:
        t[4] = t[4] + 1

f1 = open("sample.TXT", "w")
for i in range(len(t)):
    l = (f"{i}. {choice[i]} {t[i]} ")
    f1.write(l)
f1.close()
f2=open("sample.TXT","r")
for line in f2:
    l=line.strip()
    l2=l.split()
    print(f"The choice {l2[1]} {l2[2]} was chosen {l2[3]} time")



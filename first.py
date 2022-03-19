import random
name = input("enter name ")
id = input("enter ID")
mcq= {
"A" :"""1)2+2 
a) 4 b) 5 c)6""",  

"C" :"""2)3*2 
a) 4 b) 5 c)6""",

"B" :"""3)2+3 
a) 4 b) 5 c)6""",  

"A" :"""4)9+1 
a) 10 b) 15 c)26""", 

"C" :"""5)20+20
a)47 b)50 c)40""",

"A" :"""6)30+2 
a) 32 b) 50 c)6""",  

"C" :"""7)4*2 
a) 4 b) 5 c)8""",

"B" :"""8)20+3 
a) 4 b) 23 c)6""",  

"A" :"""9)92+1 
a) 93 b) 15 c)26""", 

"C" :"""10)52+20
a)47 b)50 c)72""",

"A" :"""11)2+25 
a) 27 b) 53 c)6""",  

"C" :"""12)2*8 
a) 4 b) 15 c)16""",

"B" :"""13)211+3 
a) 400 b) 214 c)621""",  

"A" :"""14)95+1 
a) 96 b) 15 c)26""", 

"C" :"""15)70+20
a)47 b)50 c)90""",

"A" :"""16)90+2 
a) 92 b) 50 c)6""",  

"C" :"""17)5*2 
a) 14 b) 52 c)25""",

"B" :"""18)16+4 
a) 4 b) 20 c)6""",  

"A" :"""19)82+1 
a) 83 b) 15 c)26""", 

"C" :"""20)30+20
a)47 b)20 c)50""",
}
Answer = []

shuf = list (mcq)

y=random.shuffle(shuf)
for y in mcq :
    print(mcq[y])
    x=input("Enter Your Anwser : ").upper()
    if x == y :
        Answer.append("true")

reslet=f"{len(Answer)}/3"
print(reslet)
file = open("student.txt","a")
file.write("name : " + name)
file.write('\n')
file.write("id : " +id)
file.write('\n')
file.write("reslet : " + reslet)
file.write('\n')
file.write('*******************')
file.close()
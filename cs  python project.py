def functions():
    #decimal to binary
    def dtb(num):
        if num>1:
            dtb(num//2)
        print('the required binary number is:',num%2,end="")
    #binary to decimal
    def bta(kum):
        I=0
        final=0
        while(kum!=0):
            temp=kum%10
            temp=temp*(2**I)
            I=I+1
            final=final+temp
            kum=kum//10
        print('the required decimal number is:',final)
    #decimal to hexadecimal
    def fun(s):
        def cal(s):
            if a<10:
                b=str(a)
            elif a==10:
                b="A"
            elif a==11:
                b="B"
            elif a==12:
                b="C"
            elif a==13:
                b="D"
            elif a==14:
                b="E"
            else:
                b="F"
            return b
        b=a
        L1=""
        while True:
            b=int(b)
            c=b%16
            if b<16:
                L1=L1+cal(c)
                break
            else:
                L1=L1+cal(c)
                b=b/16
        c=""
        for i in reversed(L1):
            c=c+i
            print('required hexadecimal value:',c)
    #hexadecimal to decimal
    def htd():
        print("Enter the Hexadecimal Number:")
        hexdecnum=input()
        chk=0
        decnum=0
        hexdecnumlen=len(hexdecnum)
        hexdecnumlen=hexdecnumlen-1
        i=0
        while hexdecnumlen>=0:
            rem=hexdecnum[hexdecnumlen]
            if rem>='0' and rem<='9':
                rem=int(rem)
            elif rem>='A' and rem<='F':
                rem=ord(num)
                rem=rem-87
            else:
                chk=1
                break
            decnum=decnum+(rem*(16**i))
            hexdecnumlen=hexdecnumlen-1
            i=i+1
        if chk==0:
            print("\nEquivalent Decimal Value:",decnum)
        else:
            print("\nInvalid Input!")
    #decimal to octal
    def dto():
        decimal=int(input("Enter a decimal number \n"))
        octal=0
        ctr=0
        temp=decimal
        while(temp>0):
            octal+=((temp%8)*(10**ctr))
            temp=int(temp/8)
            ctr+=1
            print("octal of {x} is:{y}".format(x=decimal,y=octal))
    #octal to decimal
    def otd(num):
        decimal_value=0
        base=1
        while(num):
            last_digit=num%10
            num=int(num/10)
            decimal_value+=last_digit*base
            base=base*8
        print("The decimal value is:",decimal_value)
    #binary to hexadecimal
    def bth():
        print("Enter the binary number:")
        bnum=int(input)
        hex=0
        mul=1
        chk=1
        i=0
        hnum=[]
        while bnum!=0:
            rem=bnum%10
            hex=hex+(rem*mul)
            if chk%4==0:
                if hex<10:
                    hex=hex+48
                    val=chr(hex)
                    hnum.insert(i,val)
                else:
                    hex=hex+55
                    val=chr(hex)
                    hnum.insert(i,val)
                mul=1
                hex=0
                chk=1
                i=i+1
            else:
                mul=mul*2
                chk=chk+1
            bnum=int(bnum/10)
        if chk!=1:
            hex=hex+48
            val=chr(hex)
            hnum.insert(i,val)
        elif chk==1:
            i=i-1
        print("\nEquivalent hexadecimal value=",end=" ")
        while i>0:
            print(end=hnum[i])
            i=i-1
        print()
    #binary to octal
    def bto():
        print("Enter the binary number:")
        binarynum=int(input())
        octaldigit=0
        octalnum=[]
        i=0
        mul=1
        chk=1
        while binarynum!=0:
              rem=binarynum%10
              octaldigit=octaldigit+(rem*mul)
              if chk%3==0:
                  octalnum.insert(i,octaldigit)
                  mul=1
                  octaldigit=0
                  chk=1
                  i=i+1
              else:
                  mul=mul*2
                  chk=chk+1
              binarynum=int(binarynum/10)
              if chk!=1:
                octalnum.insert(i,octaldigit)
              print("\nEquivalent octal value=",end=' ')
              while i>=0:
                print(str(octalnum[i]),end=" ")
              i=i-1
              print()
    #octal to hexadecimal
    def oth():
        octnum=int(input())
        chk=0
        i=0
        decnum=0
        while octnum!=0:
            rem=octnum%10
            if rem>7:
                chk=1
                break
            decnum=decnum+(rem*(8**i))
            i=i+1
            octnum=int(octnum/10)
        if chk==0:
            i=0
            hexdecnum=[]
            while decnum!=0:
                rem=decnum%16
                if rem<10:
                    rem=rem+48
                else:
                    rem=rem+55
                rem=chr(rem)
                hexdecnum.insert(i,rem)
                i=i+1
                decnum=int(decnum/16)
            print("\nEquivalent hexadecimal value is:")
            i=i-1
            while i>=0:
                print(end=hexadecimal[i])
                i=i-1
            print()
        else:
            print("\nInvalid Input")
    #octal to binary
    def otb(h):
        print(h)
        def OctToBin(octnum):
            binary=" "
            while octnum!=0:
                d=int(octnum%10)
                if d==0:
                    binary="".join(["000",binary])
                elif d==1:
                    binary="".join(["001",binary])
                elif d==2:
                    binary="".join(["010",binary])
                elif d==3:
                    binary="".join(["011",binary])
                elif d==4:
                    binary="".join(["100",binary])
                elif d==5:
                    binary="".join(["101",binary])
                elif d==6:
                    binary="".join(["110",binary])
                elif d==7:
                    binary="".join(["111",binary])
                else:
                    binary="Invalid Octal Digit"
                    break
                octnum=int(octnum/10)
            return binary
        octnum=int(input("enter octal value"))
        final_bin=""+OctToBin(octnum)
        print("Equivalent Binary Value=",final_bin)
    #hexadecimal to binary
    def htb():
        import math
        ini_string=input("enter hexadecimal value")
        print("Initial string",ini_string)
        n=int(ini_string,16)
        bStr=''
        while n>0:
            bStr=str(n%2)+bStr
            n=n>>1
        res=bStr
        print("resultant string",str(res))
    #hexadecimal to octal
    def hto():
        print("enter the hexadecimal number:")
        hexdecnum=input()
        chk=0
        decnum=0
        hexdecnumlen=len(hexdecnum)
        hexdecnumlen=hexdecnumlen-1
        i=0
        while hexdecnumlen>=0:
            rem=hexdecnum[hexdecnumlen]
            if rem>='0' and rem<='9':
                rem=int(rem)
            elif rem>='A' and rem<='F':
                rem=ord(rem)
                rem=rem-55
            elif rem>='a' and rem<='f':
                rem=ord(rem)
                rem=rem-87
            else:
                chk=1
                break
            decnum=decnum+(rem*(16**i))
            hexdecnumlen=hexdecnumlen-1
            i=i+1
        if chk==0:
            i=0
            octnum=[]
            while decnum!=0:
                rem=decnum%8
                octnum.insert(i,rem)
                i=i+1
                decnum=int(decnum/8)
            print("\nEquivalent octal value is:")
            i=i-1
            while i>=0:
                print(octnum[i],end="")
                i=i-1
            print()
        else:
            print("\nInvalid Input!")
            print("Hello,['_'],I am max and i will assist you in your number convertions")
            f=input("would you like to convert any number,['_'],(y,n)")
        while f=="y":
         print("so lets get started ,[^_^]")
         d=input("now enter the value you wish to convert,(decimal,hexadecimal,octal,binary),['_']")
         x=input("good!,[^_^],now enter to what type should this number be converted to,(decimal,hexadecimal,octal,binary)")
         if d=='decimal' and x=='binary':
             numb=int(input("enter decimal value"))
             dtb(numb)
         elif d=='decimal' and x=='hexadecimal':
             a=int(input("enter decimal value:"))
             fun(a)
         elif d=='decimal' and x=='octal':
             dto()
         elif d=='binary' and x=='decimal':
             kumb=int(input("enter binary value"))
             bta(kumb)
         elif d=='binary' and x=='hexadecimal':
             bth()
         elif d=='binary' and x=='octal':
             bto()
         elif d=='hexadecimal' and x=='decimal':
             htd()
         elif d=='hexadecimal' and x=='binary':
             h()
         elif d=='hexadecimal' and x=='octal':
             hto()
         elif d=='octal' and x=='binary':
             hto()
         elif d=='octal' and x=='binary':
             h="['_']"
             otb(h)
         elif d=='octal' and x=='hexadecimal':
             oth()
         elif d=='octal' and x=='decimal':
             octnum=int(input("enter an octal number"))
             otd(num)
         elif d==x:
             print("you have entered two same types ,[-_-],please re-enter your number")
         else:
             print("error,[*_*],check if the type you have entered is available in the options and re-enter the types")
             end
         f=input("do you want to continue?,[@_@],(y,n)")
         print("oh,ok,[._.],see you next time then,[^_^]")
functions()
         
                
        
        
            
    

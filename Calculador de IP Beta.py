print("1 a 126 - classe A")
print("128 a 196 - classe B")
print("198 a 255 - classe C")
ip = input("insira o seu IP com pontos e mascara")
ip_p = ip.split(".")
wd=255
m=0
octi=[128,192,224,240,248,252,254,255]
#classe do IP#
msc = ip_p[0]
if int(msc) >=1 and int(msc)<=126 :
    print("classe do Ip é A")
elif int(msc) >=128 and int(msc)<=191:
    print("classe do Ip é B")
elif int(msc) >=192 and int(msc)<=223:
     print("classe do Ip é C")
else:
    print("classe do Ip é D")
#classe da rede#
cr = ip_p[4]
if int(cr) ==8:
    m=int(m)+1
    print("classe da mascara é A")
elif int(cr) >=9 and int(cr)<=15 :
    m=int(m)+2
    print(" mascará sub classe A")
elif int(cr) ==16:
    m=int(m)+3
    print("classe da mascara é B")
elif int(cr) >=17 and int(cr)<=23 :
    m=int(m)+4
    print(" mascará sub classe B")
elif int(cr) ==24:
    m=int(m)+5
    print("classe da mascara é C")
elif int(cr) >=25 and int(cr)<=31 :
    m=int(m)+6
    print("mascará sub classe C")
else:
    print("classe D")
#Id da rede / primeiro Ip da rede #
if m==1:
    print("ID_da rede",ip_p[0],"0","0","0")
    print("primeiro Ip da rede",ip_p[0],"0","0","1")
elif m==2:
    print("ID_da rede",ip_p[0],(ip_p[1]),"0","0")
    print("Primeiro Ip da Rede",ip_p[0],(ip_p[1]),"0","1")
elif m==3:
    print("ID_da rede",ip_p[0],(ip_p[1]),"0","0")
    print("Primeiro Ip da Rede",ip_p[0],(ip_p[1]),"0","1")
elif m==4:
    print("ID_da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"0")
    print("primeiro Ip da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"1")
elif m==5:
    print("ID_da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"0")
    print("primeiro Ip da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"1")
elif m==6:
    print("ID_da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"0")
    print("primeiro Ip da rede",ip_p[0],(ip_p[1]),(ip_p[2]),"1")
else:
    print("Id da rede só vai até 31 bro -_-")
#mascara da rede#
if m==1:
    mr=int(cr)-1
    print("a mascara da rede é",octi[mr],"0","0","0",)
elif m==2:
    mr=int(cr)-9
    print("a mascara da rede é","255",octi[mr],"0","0",)
elif m==3:
    mr=int(cr)-9
    print("a mascara da rede é","255",octi[mr],"0","0",)
elif m==4:
    mr=int(cr)-17
    print("a mascara da rede é","255","255",octi[mr],"0",)
elif m==5:
    mr=int(cr)-17
    print("a mascara da rede é","255","255",octi[mr],"0",)
elif m==6:
    mr=int(cr)-25
    print("a mascara da rede é","255","255","255",octi[mr],)
else:
    print("classe D")
#broadcast#
if m==1:
    q1=wd-0
    q2=wd-0
    q3=wd-0 
    print("Broadcast_é",ip_p[0],q1,q2,q3)
    print("Ultimo Ip valido é",ip_p[0],q1,q2,q3-1)
elif m==2:
    q2=wd-0
    q3=wd-0 
    print("Broadcast_é",ip_p[0],ip_p[1],q2,q3)
    print("Ultimo Ip valido é",ip_p[0],ip_p[1],q2,q3-1)
elif m==3:
    q2=wd-0
    q3=wd-0 
    print("Broadcast_é",ip_p[0],ip_p[1],q2,q3)
    print("Ultimo Ip valido é",ip_p[0],ip_p[1],q2,q3-1)
elif m==4:
    q3=wd-0 
    print("Broadcast_é",ip_p[0],ip_p[1],ip_p[2],q3)
    print("Ultimo Ip valido é",ip_p[0],ip_p[1],ip_p[2],q3-1)
elif m==5:
    q3=wd-0 
    print("Broadcast_é",ip_p[0],ip_p[1],ip_p[2],q3)
    print("Ultimo Ip valido é",ip_p[0],ip_p[1],ip_p[2],q3-1)
elif m==6:
    q3=wd-0 
    print("Broadcast_é/ultimo_Ip_da_rede",ip_p[0],ip_p[1],ip_p[2],q3)
    print("Ultimo Ip valido é",ip_p[0],ip_p[1],ip_p[2],q3-1)
else:
    print("deu erro")
#quantidade de Ips#
ips=32-int(cr)
ips=2**ips
print("quantidade de Ips",ips)
#quantidade de hosts#
host=ips-2
print("quantidade de Hosts",host)

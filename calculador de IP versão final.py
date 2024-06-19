while True:
    ip=input("Insira o seu IP:\n")
    ip_p=ip.split(".")
    ip_p2=ip.split("/")
    wd=255
    m=0
    np=0
    l=0
    cr=0
    octi=[128,192,224,240,248,252,254,255]
    sr=[1,2,4,8,16,32,64,128]
    ky=0
    mr=0
    # classe do IP
    msc=ip_p[0]
    if int(msc)>=1 and int(msc)<=126:
        np=0+1
        ç=8
        l="A"
        gab1=["Classe do Ip é:"]
    elif int(msc)>=128 and int(msc)<=191:
        np=0+3
        ç=16
        l="B"
        gab1=["Classe do Ip é:"]
    elif int(msc)>=192 and int(msc)<=223:
        np=0+5
        ç=24
        l="C"
        gab1=["Classe do Ip é:"]
    else:
        print("IP inválido")
    # classe da redePT1
    if len(ip_p2)==1:
        gab2=["Classe da rede é:"]
        m=np
    else:
        cr = ip_p2[1]
    # classe da redePT2
    if int(cr)==1:
        cr=cr + 0
    elif int(cr)==8:
        m=int(m) + 1
        gab2=["Classe da mascara é: A"]
    elif int(cr) >= 9 and int(cr) <= 15:
        m=int(m) + 2
        gab2=["Mascará sub classe: A"]
    elif int(cr)==16:
        m=int(m) + 3
        gab2=["Classe da mascara é: B"]
    elif int(cr)>=17 and int(cr)<=23:
        m=int(m) + 4
        gab2=["Mascará sub classe: B"]
    elif int(cr)==24:
        m=int(m) + 5
        gab2=["Classe da mascara é: C"]
    elif int(cr)>=25 and int(cr)<=31:
        m=int(m) + 6
        gab2=["Mascará sub classe: C"]
    else:
        print("IP inválido")
    # Id da rede / primeiro Ip válido
    if m==1 and np==1:
        gab3=["ID da rede:", ip_p[0],"0", "0","0"]
        gab4=["primeiro Ip da rede:",ip_p[0],"0","0","1"]
    elif m==1:
        gab3=["ID da rede:", ip_p[0],"0", "0","0"]
        gab4=["primeiro Ip da rede:",ip_p[0],"0","0","1"]
    elif m==2:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),"0","0"]
        gab4=["Primeiro Ip da Rede:",ip_p[0],(ip_p[1]),"0","1"]
    elif m==3 and np == 3:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),"0","0"]
        gab4=["Primeiro Ip da Rede:",ip_p[0],(ip_p[1]),"0","1"]
    elif m==3:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),"0","0"]
        gab4=["Primeiro Ip da Rede:",ip_p[0],(ip_p[1]),"0","1"]
    elif m==4:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),(ip_p[2]),"0"]
        gab4=["primeiro Ip da rede:",ip_p[0],(ip_p[1]),(ip_p[2]),"1"]
    elif m==5 and np == 5:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),(ip_p[2]),"0"]
        gab4=["primeiro Ip da rede:",ip_p[0],(ip_p[1]),(ip_p[   2]),"1"]
    elif m==5:
        gab3=["ID da rede:", ip_p[0],(ip_p[1]),(ip_p[2]),"0"]
        gab4=["primeiro Ip da rede:",ip_p[0],(ip_p[1]),(ip_p[2]),"1"]
    elif m==6:
        gab3=["ID da rede:",ip_p[0],(ip_p[1]),(ip_p[2]), "0"]
        gab4=["primeiro Ip da rede:",ip_p[0],(ip_p[1]),(ip_p[2]),"1"]
    else:
        print("IP inválido")
    # mascara da rede/Quantidade de sub redes
    if m==1 and np==1:
        mr=int(cr)
        gab5=["A mascara da rede é:",255,0,0,0]
    elif m==1:
        mr=int(cr)-9
        gab5=["A mascara da rede é:",255,0,0,0]
    elif m==2:
        mr=int(cr)-9
        gab5=["A mascara da rede é:",255,0,0]
        gab5.insert(2,octi[mr])  
    elif m==3 and np==3:
        mr=int(cr)
        gab5=["A mascara da rede é:",255,255,0,0]
    elif m==3:
        mr=int(cr)-17
        gab5=["A mascara da rede é:",255,255,0,0]
    elif m==4:
        mr=int(cr)-17
        gab5=["A mascara da rede é:",255,255,0]
        gab5.insert(3,octi[mr])
    elif m==5 and np==5:
        mr=int(cr)
        gab5=["A mascara da rede é:",255,255,255,0]
    elif m==5:
        mr=int(cr)-25
        gab5=["A mascara da rede é:",255,255,255,0]
    elif m==6:
        mr=int(cr)-25
        gab5=["A mascara da rede é:",255,255,255,]
        gab5.insert(4,octi[mr])
    else:
        print("IP inválido")
    # broadcast/ultimo IP válido
    if m==1 and np==1:
        gab6=["Broadcast é:",ip_p[0],wd,wd,wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],wd,wd,254]
    elif m==1:
        gab6=["Broadcast é:",ip_p[0],wd,wd,wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],wd,wd,254]
    elif m==2:
        gab6=["Broadcast é:", ip_p[0],ip_p[1], wd, wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],wd,254]
    elif m==3 and np==3:
        gab6=["Broadcast é:", ip_p[0],ip_p[1], wd, wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],wd,254]
    elif m==3:
        gab6=["Broadcast é:", ip_p[0],ip_p[1], wd, wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],wd,254]
    elif m==4:
        gab6=["Broadcast é:", ip_p[0],ip_p[1],ip_p[2],wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],ip_p[2],254]
    elif m==1 and np==5:
        gab6=["Broadcast é:", ip_p[0],ip_p[1],ip_p[2],wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],ip_p[2],254]
    elif m==5:
        gab6=["Broadcast é:", ip_p[0],ip_p[1],ip_p[2],wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],ip_p[2],254]
    elif m==6:
        gab6=["Broadcast é:", ip_p[0],ip_p[1],ip_p[2],wd]
        gab7=["Ultimo Ip válido é:",ip_p[0],ip_p[1],ip_p[2],254]
    else:
        print("IP inválido")
    # quantidade de Ips
    if m==1 and np==1:
        ips=32-int(ç)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==1:
        ips=32-int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==2:
        ips=32 - int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==3 and np==3:
        ips=32-int(ç)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==3:
        ips=32-int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==4:
        ips=32-int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==5 and np==5:
        ips=32-int(ç)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==5:
        ips=32-int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    elif m==6:
        ips=32-int(cr)
        ips=2**ips
        gab8=["Quantidade de Ips:",ips]
    else:
        print("IP inválido")
    #limpeza do printPT1#   
    gab1 = [str(item) for item in gab1]
    gab2 = [str(item) for item in gab2]
    gab3 = [str(item) for item in gab3]
    gab4 = [str(item) for item in gab4]
    gab5 = [str(item) for item in gab5]
    gab6 = [str(item) for item in gab6]
    gab7 = [str(item) for item in gab7]
    gab8 = [str(item) for item in gab8]
    #limpeza do printPT2#
    print(" ".join(gab5))
    print(" ".join(gab3))
    print(" ".join(gab6))
    print(" ".join(gab1),l)
    print(" ".join(gab2))
    print(" ".join(gab4))
    print(" ".join(gab7))
    print(" ".join(gab8))
    print("Quantidade de Hosts:", ips - 2)
    print("Quantidade de sub redes",sr[mr+1])
    #repeticão#
    rs = input("Deseja executar o script novamente? (s/n):\n")
    if rs.lower() != "s": 
        break

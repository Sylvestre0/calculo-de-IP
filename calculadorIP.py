class redeIP:
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.partes_ip = [barra for partes in self.ipv4.split(".") for barra in partes.split("/")]
        self.valido = self.validar_ip()

    def validar_ip(self):
        if not (len(self.partes_ip) == 5 or len(self.partes_ip) == 4):
            return False
        if len(self.partes_ip) == 5:
            if not (8 <= int(self.partes_ip[4]) <= 32):
                return False
        for parte in self.partes_ip[:4]:
            if not (parte.isdigit() and 0 <= int(parte) <= 255):
                return False
        return True

    def classe_ip(self):
        primeiro_octeto = int(self.partes_ip[0])
        if 1 <= primeiro_octeto <= 126:
            if len(self.partes_ip) == 4:
                self.partes_ip.append(8)
            return 'A'
        if 128 <= primeiro_octeto <= 191:
            if len(self.partes_ip) == 4:
                self.partes_ip.append(16)
            return 'B'
        if 192 <= primeiro_octeto <= 223:
            if len(self.partes_ip) == 4:
                self.partes_ip.append(24)
            return 'C'
        
    def classe_mascara(self):
        mascara = int(self.partes_ip[-1])
        if 8 <= mascara <= 15:
            return 'A'
        if 16 <= mascara <= 23:
            return 'B'
        if 24 <= mascara <= 31:
            return 'C'

    def sub_mascara(self):
        submascara = [0, 0, 0, 0]
        mascara = int(self.partes_ip[-1])
        octetos_completo = mascara // 8
        octetos_incompleto = mascara % 8
 
        for rede in range(octetos_completo):
            submascara[rede] = 255

        if octetos_completo < 4:
            submascara[octetos_completo] = (256 - 2**(8 - octetos_incompleto))

        return submascara, 2 **octetos_incompleto

    def endereco_de_rede(self):
        submascara = self.sub_mascara()[0]
        endereco = [int(self.partes_ip[i]) & submascara[i] for i in range(4)]
        return endereco

    def endereco_de_broadcast(self):
        submascara = self.sub_mascara()[0]
        mascara_invertida = [255 - mask for mask in submascara]
        broadcast = [int(self.partes_ip[i]) | mascara_invertida[i] for i in range(4)]
        return broadcast

    def intervalo_hosts(self):
        endereco = self.endereco_de_rede()
        broadcast = self.endereco_de_broadcast()
        primeiro_host = list(endereco)
        primeiro_host[-1] += 1
        ultimo_host = list(broadcast)
        ultimo_host[-1] -= 1
        return primeiro_host, ultimo_host

    def total_ips(self):
        mascara = int(self.partes_ip[-1])
        return 2**(32 - mascara)

    def ips_usaveis(self):
        total_ips = self.total_ips()
        return total_ips - 2 if total_ips > 2 else 0

    def __str__(self):
        return (
        f"\nIP: {self.ipv4}\n"
        f"Classe do Ip: {self.classe_ip()}\n"
        f"Classe da mascará:{self.classe_mascara()}\n"
        f"ID da rede: {'.'.join(map(str, self.endereco_de_rede()))}\n"
        f"Primeiro IPs: {'.'.join(map(str, self.intervalo_hosts()[0]))}\n"
        f"Mascará: {'.'.join(map(str, self.sub_mascara()[0]))}\n"
        f"endereço de Broadcast: {'.'.join(map(str, self.endereco_de_broadcast()))}\n"
        f"Ultimo IPs: {'.'.join(map(str, self.intervalo_hosts()[1]))}\n"
        f"Quantidade de IPs: {self.total_ips()}\n"
        f"IPs Utilizaveis: {self.ips_usaveis()}\n"
        f"Numero de Redes: {self.sub_mascara()[1]}\n"
        )

def main():
    while True:
        ipv4 = input("Insira o seu IP no formato xxx.xxx.xxx.xxx/xx Com ou sem mascará: ")
        rede_ip = redeIP(ipv4)
        
        if not rede_ip.valido:
            print("IP inválido. Tente novamente.")
            continue
        
        print(rede_ip)

        resposta = input("Deseja executar novamente? (s/n): ").lower()
        if resposta != "s":
            break

main()
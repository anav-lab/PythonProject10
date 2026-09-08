class DispositivoRede:

    def __init__(self, ip, hostname, ativo):
        self.ip = ip
        self.hostname = hostname
        self.ativo = ativo

    def verificar_status(self):
        if self.ativo:
            status = "online"
        else:
            status = "offline"

        return f"Dispositivo {self.hostname} - IP: {self.ip} - Status: {status}"


class Servidor(DispositivoRede):

    def __init__(self, ip, hostname, ativo, sistema_operacional):
        super().__init__(ip, hostname, ativo)
        self.sistema_operacional = sistema_operacional

    def verificar_status(self):
        if self.ativo:
            status = "online"
        else:
            status = "offline"

        return f"Servidor {self.hostname} - IP: {self.ip} - Status: {status} - Sistema: {self.sistema_operacional}"


class Roteador(DispositivoRede):

    def __init__(self, ip, hostname, ativo, numero_portas):
        super().__init__(ip, hostname, ativo)
        self.numero_portas = numero_portas

    def verificar_status(self):
        if self.ativo:
            status = "online"
        else:
            status = "offline"

        return f"Roteador {self.hostname} - IP: {self.ip} - Status: {status} - Portas: {self.numero_portas}"


class Switch(DispositivoRede):

    def __init__(self, ip, hostname, ativo, velocidade_portas):
        super().__init__(ip, hostname, ativo)
        self.velocidade_portas = velocidade_portas

    def verificar_status(self):
        if self.ativo:
            status = "online"
        else:
            status = "offline"

        return f"Switch {self.hostname} - IP: {self.ip} - Status: {status} - Velocidade: {self.velocidade_portas}"


dispositivos = [
    Servidor("192.168.1.10", "Servidor01", True, "Linux"),
    Servidor("192.168.1.11", "Servidor02", False, "Windows"),

    Roteador("192.168.1.1", "Roteador01", True, 8),
    Roteador("192.168.1.2", "Roteador02", False, 16),

    Switch("192.168.1.20", "Switch01", True, "1 Gbps"),
    Switch("192.168.1.21", "Switch02", True, "10 Gbps")
]


for dispositivo in dispositivos:
    print(dispositivo.verificar_status())
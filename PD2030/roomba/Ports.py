import serial.tools.list_ports


class Ports:
    def __init__(self):
        self.dict = {}

    def update(self):
        ports = serial.tools.list_ports.comports()
        for p in ports: self.dict[p.description] = p.device

    def print(self):
        self.update()
        keys = self.dict.keys()
        for k in keys:
            print(k, self.dict[k])

    def get_port(self, device):
        self.update()
        keys = self.dict.keys()
        for k in keys:
            if device in k: return self.dict[k]
        return None


def get_port(device):
    ports = Ports()
    port = ports.get_port(device)
    return port


if __name__ == "__main__":
    p = Ports()
    p.print()

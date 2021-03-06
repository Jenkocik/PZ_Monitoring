class SystemInfo:
    """
    Klasa ta jest kontenerem przechowujacym informacje o obciazeniu systemu.
    """
    
    def __init__(self):
        self.cpu = {}
        self.ram = {}
        self.disk = {}

    def get_cpu(self):
        return self.cpu

    def get_ram(self):
        return self.ram

    def get_disk(self):
        return self.disk

    def set_cpu(self, x):
        self.cpu = x

    def set_ram(self, x):
        self.ram = x

    def set_disk(self, x):
        self.disk = x

    def get_str_info(self):
        return str({"INFO" : [self.get_cpu(), self.get_ram(), self.get_disk()]}).replace('\'', '"')

if __name__ == "__main__":
    pass

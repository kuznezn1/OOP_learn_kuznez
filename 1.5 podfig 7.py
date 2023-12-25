class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(args)

    def get_config(self):
        return [
        f"Материнская плата: {self.name}",
        f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
        f"Слотов памяти: {self.total_mem_slots}",
        f"Память: {'; '.join([f'{el.name} - {el.volume}' for el in self.mem_slots])}"
        ]



mb = MotherBoard("asus", CPU("intel", 9600), Memory("kingston1", 1024), Memory("kingston2", 2048))
print(mb.get_config())
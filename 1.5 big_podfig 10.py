from random import choices

class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines  # число мин вокруг клетки
        self.mine = mine  # наличие/отсутствие мины в текущей клетке (True/False);
        self.fl_open = False  # открыта/закрыта клетка - булево значение (True/False)


class GamePole:
    def __init__(self, N, M):
        """Здесь N - размер поля; M - общее число мин на поле"""
        self.count_mines = M
        self.pole = [[Cell(around_mines = 0, mine = self.get_mine()) for _ in range(N)] for _ in range(N)]


    def get_mine(self):
        """ Выдает случайным образом мину или не мину определенное колчисетсво раз"""

        mina = choices([True, False], weights=[0.2, 0.8])[0]


        if self.count_mines <= 0:
            return False
        if mina:
            self.count_mines -= 1
        return mina

    def show(self):
        for ryad in self.pole:
            for element in ryad:
                if element.fl_open == False:
                    print("#",end = " ")
                elif element.mine:
                    print("*",end = " ")
                else:
                    print(element.around_mines,end=" ")
            print('\n')




N = 10
M = 12
p = GamePole(N,M)

# открываем все клетки
for i in range(N):
    for j in range(N):
        p.pole[i][j].fl_open = True


p.show()
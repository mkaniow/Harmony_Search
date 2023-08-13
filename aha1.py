import random
from operator import itemgetter
import aha
import qwe

class Policz():

    def __init__(self, iterations, hms, hmrc, par, r, function, ilosc, x1min = 0.0, x1max = 0.0, x2min = 0.0, x2max = 0.0, x3min = 0.0, x3max = 0.0, x4min = 0.0, x4max = 0.0, x5min = 0.0, x5max = 0.0):
        self.memory = list()
        self.min_max = [[x1min, x1max],[x2min, x2max],[x3min, x3max],[x4min, x4max],[x5min, x5max]]
        self.iterations = iterations
        self.hms = hms
        self.hmrc = hmrc
        self.par = par
        self.r = r
        self.ilosc = ilosc
        self.function = function
        self.i = 1
        self.start_hs()
        self.memory_piece = []

    def start_hs(self):
        while self.i <= self.iterations:
            #if memory is not full
            if self.i <= self.hms:
                cords = []
                for z in range(self.ilosc):
                    cord = random.uniform(itemgetter(0)(self.min_max[z]), itemgetter(1)(self.min_max[z]))
                    cords.append(cord)
                memory_piece = [cords]
                if len(cords) == 2:
                    result = aha.Licz.solve(self.function, cords[0], cords[1])
                elif len(cords) == 3:
                    result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2])
                elif len(cords) == 4:
                    result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2], cords[3])
                elif len(cords) == 5:
                    result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2], cords[3], cords[4])
                memory_piece.append(result)
                self.memory.append(memory_piece)
                del cords
                del memory_piece

                self.i += 1
            #if memory is full
            else:
                self.memory = sorted(self.memory, key = itemgetter(1))
                random_number = random.random()
                if random_number > self.hmrc:
                    cords = []
                    for z in range(self.ilosc):
                        cord = random.uniform(itemgetter(0)(self.min_max[z]), itemgetter(1)(self.min_max[z]))
                        cords.append(cord)
                    memory_piece = [cords]
                    if len(cords) == 2:
                        result = aha.Licz.solve(self.function, cords[0], cords[1])
                    elif len(cords) == 3:
                        result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2])
                    elif len(cords) == 4:
                        result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2], cords[3])
                    elif len(cords) == 5:
                        result = aha.Licz.solve(self.function, cords[0], cords[1], cords[2], cords[3], cords[4])
                    memory_piece.append(result)
                    if itemgetter(1)(self.memory[-1]) > itemgetter(1)(memory_piece):
                        self.memory[-1] = memory_piece
                        self.i += 1
                    else:
                        self.i += 1
                    del cords
                    del memory_piece
                else:
                    q = random.random()
                    cords_container = []
                    for k in range(self.ilosc):
                        for j in range(self.hms):
                            if q >= (j * (1/self.hms)) and q < ((j + 1) * (1/self.hms)):
                                cord = itemgetter(0)(self.memory[j])[k]
                                random_par = random.random()
                                if random_par <= self.par:
                                    alfa = random.uniform(-self.r, self.r)
                                    cord = cord + alfa
                                    cords_container.append(cord)
                                else:
                                    cords_container.append(cord)
                            else:
                                pass
                    for s in range(self.ilosc):
                        if cords_container[s] < itemgetter(0)(self.min_max[s]) or cords_container[s] > itemgetter(1)(self.min_max[s]):
                            break
                        else:
                            if len(cords_container) == 2:
                                result = aha.Licz.solve(self.function, cords_container[0], cords_container[1])
                            elif len(cords_container) == 3:
                                result = aha.Licz.solve(self.function, cords_container[0], cords_container[1], cords_container[2])
                            elif len(cords_container) == 4:
                                result = aha.Licz.solve(self.function, cords_container[0], cords_container[1], cords_container[2], cords_container[3])
                            elif len(cords_container) == 5:
                                result = aha.Licz.solve(self.function, cords_container[0], cords_container[1], cords_container[2], cords_container[3], cords_container[4])
                            memory_piece = [cords_container]
                            memory_piece.append(result)
                            if itemgetter(1)(self.memory[-1]) > itemgetter(1)(memory_piece[0]):
                                self.memory[-1] = memory_piece
                                self.i += 1
                            else:
                                self.i += 1
                    del cords_container
                    del memory_piece
            qwe.Plot.plot(self.memory, self.min_max[0][0], self.min_max[0][1], self.min_max[1][0], self.min_max[1][1])
        return self.memory

#a = Policz(3000, 10, 0.85, 0.5, 0.2, '(x1+2*x2-7)^2+(2*x1+x2-5)^2', 2, -5, 5, -5, 5)

#a = Policz.start_hs(4000, 10, 0.85, 0.5, 0.3, '(x1)^2+(x2)^2+(x3)^2', 3, -5, 5, -5, 5, -5, 5)

#print(a.memory)
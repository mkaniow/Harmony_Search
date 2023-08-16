import random
from operator import itemgetter
import ploter
import parser_modul
import solver_module

class Calculate():
    '''
    Main loop for Harmony Search algorithm

    Parameters
    ----------
    iterations : int
    hms : int
    hmrc : float
        value between 0 and 1
    par : float
        value between 0 and 1
    r : int / float
    function : str
    ilosc : int
    x1min, x1max, x2min, x2max, x3min, x3max, x4min, x4max, x5min, x5max : floats
                
    Returns
    -------
    Memory with cords and values
    '''
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

    def start_hs(self):
        self.list_of_func_parts = parser_modul.ReadFunction.string_to_list(self.function)
        while self.i <= self.iterations:
            #if memory is not full
            if self.i <= self.hms:
                cords = []
                for z in range(self.ilosc):
                    cord = random.uniform(itemgetter(0)(self.min_max[z]), itemgetter(1)(self.min_max[z]))
                    cords.append(cord)
                memory_piece = [cords]
                print(memory_piece)
                result = solver_module.Solve.solve(self.list_of_func_parts, cords)
                memory_piece.append(result)
                self.memory.append(memory_piece)

                self.i += 1
            
            #if memory is full
            else:
                self.memory = sorted(self.memory, key = itemgetter(1))
                random_number = random.random()
                #full random cords case
                if random_number > self.hmrc:
                    cords = []
                    for z in range(self.ilosc):
                        cord = random.uniform(itemgetter(0)(self.min_max[z]), itemgetter(1)(self.min_max[z]))
                        cords.append(cord)
                    memory_piece = [cords]
                    result = solver_module.Solve.solve(self.list_of_func_parts, cords)
                    memory_piece.append(result)
                    if itemgetter(1)(self.memory[-1]) > itemgetter(1)(memory_piece):
                        self.memory[-1] = memory_piece
                        self.i += 1
                    else:
                        self.i += 1
                #cords from memory case
                else:
                    q = random.random()
                    cords = []  
                    for k in range(self.ilosc):
                        for j in range(self.hms):
                            if q >= (j * (1/self.hms)) and q < ((j + 1) * (1/self.hms)):
                                cord = itemgetter(0)(self.memory[j])[k]
                                random_par = random.random()
                                if random_par <= self.par:
                                    alfa = random.uniform(-self.r, self.r)
                                    cord = cord + alfa
                                    cords.append(cord)
                                else:
                                    cords.append(cord)

                    for s in range(self.ilosc):
                        if cords[s] < itemgetter(0)(self.min_max[s]) or cords[s] > itemgetter(1)(self.min_max[s]):
                            break
                        else:
                            result = solver_module.Solve.solve(self.list_of_func_parts, cords)
                            memory_piece = [cords]
                            memory_piece.append(result)
                            if itemgetter(1)(self.memory[-1]) > itemgetter(1)(memory_piece[0]):
                                self.memory[-1] = memory_piece
                                self.i += 1
                            else:
                                self.i += 1 
            
            ploter.Plot.plot(self.memory, self.min_max[0][0], self.min_max[0][1], self.min_max[1][0], self.min_max[1][1])

        return self.memory
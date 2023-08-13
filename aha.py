
class Licz():
    def solve(function, cord1 = 0.0, cord2 = 0.0, cord3 = 0.0, cord4 = 0.0, cord5 = 0.0):
        y=''
        x1 = cord1
        x2 = cord2
        x3 = cord3
        x4 = cord4
        x5 = cord5
        holder = list(function)
        for i in range(len(holder)):
            if i == 0:
                if(holder[i] == 'x' and holder[i+1] =='1'):
                    y = y + str(x1)
                elif(holder[i] == 'x' and holder[i+1] == '2'):
                    y = y + str(x2)
                elif(holder[i] == 'x' and holder[i+1] =='3'):
                    y = y + str(x3)
                elif(holder[i] == 'x' and holder[i+1] == '4'):
                    y = y + str(x4)
                elif(holder[i] == 'x' and holder[i+1] == '5'):
                    y = y + str(x5)
                elif(holder[i] == 'c' and holder[i+1] == 'o' and holder[i+2] == 's'):
                    y = y + str('math.cos')
                elif(holder[i] == 's' and holder[i+1] == 'i' and holder[i+2] == 'n'):
                    y = y + str('math.sin')
                elif(holder[i] == 'e' and holder[i+1] == 'x' and holder[i+2] == 'p'):
                    y = y + str('math.exp')
                elif(holder[i] == 'e'):
                    y = y + str('math.e')
                else:
                    y = y + holder[i]
            else:
                if(holder[i] == 'x' and holder[i+1] =='1'):
                    y = y + str(x1)
                elif(holder[i] == 'x' and holder[i+1] == '2'):
                    y = y + str(x2)
                elif(holder[i] == 'x' and holder[i+1] =='3'):
                    y = y + str(x3)
                elif(holder[i] == 'x' and holder[i+1] == '4'):
                    y = y + str(x4)
                elif(holder[i] == 'x' and holder[i+1] == '5'):
                    y = y + str(x5)
                elif(holder[i] == '^'):
                    y = y + str('**')
                elif(holder[i] == 's' and holder[i+1] == 'i' and holder[i+2] == 'n'):
                    y = y + str('math.sin')
                elif(holder[i] == 'c' and holder[i+1] == 'o' and holder[i+2] == 's'):
                    y = y + str('math.cos')
                elif(holder[i] == 'e' and holder[i+1] == 'x' and holder[i+2] == 'p'):
                    y = y + str('math.exp')
                elif(holder[i] == 'e'):
                    y = y + str('math.e')
                elif(holder[i] == 'o'):
                    pass
                elif(holder[i] == 'p'):
                    pass
                elif(holder[i] == 'i'):
                    pass
                elif(holder[i] == 'n'):
                    pass
                elif(holder[i] == 's'):
                    pass
                elif(holder[i] == '1' and holder[i-1] =='x'):
                    pass
                elif(holder[i] == '2' and holder[i-1] =='x'):
                    pass
                elif(holder[i] == '3' and holder[i-1] =='x'):
                    pass
                elif(holder[i] == '4' and holder[i-1] =='x'):
                    pass
                elif(holder[i] == '5' and holder[i-1] =='x'):
                    pass
                elif(holder[i] == 'x' and holder[i-1] =='e'):
                    pass
                else:
                    y = y + holder[i]
        return eval(y)
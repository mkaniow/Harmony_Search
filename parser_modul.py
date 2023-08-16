class ReadFunction():
    def string_to_list(function):
        '''
        Returns the list of parts of parsed function

        Parameters
        ----------
        function : str
                    
        Returns
        -------
        list of parts (parts are: strings of non variables and variables represented as ints 1 - 5)
        '''
        memory_for_x = {'1', '2', '3', '4', '5'}
        memory_other = {
            'c': ['o', 's', 'math.cos'],
            's': ['i', 'n', 'math.sin'],
            'e': ['x', 'p', 'math.exp']
        }
        memory_skip = {'o', 'p', 'i', 'n', 's'}
        holder = list(function)
        funcion_list = []
        y = ''

        for i in range(len(holder)):
            if i == 0:    
                if(holder[i] == 'x' and holder[i+1] in memory_for_x):
                    funcion_list.append(int(holder[i+1]))
                elif (holder[i] in memory_other and holder[i+1] == memory_other[holder[i]][0] and holder[i+2] == memory_other[holder[i]][1]):
                    y = y + memory_other[holder[i]][2]
                elif (holder[i] == 'e'):
                    y = y + str('math.e')
                else:
                    y = y + holder[i]
            else:
                if(holder[i] == 'x' and holder[i+1] in memory_for_x):
                    funcion_list.append(y)
                    y = ''
                    funcion_list.append(int(holder[i+1]))
                elif (holder[i] in memory_other and holder[i+1] == memory_other[holder[i]][0] and holder[i+2] == memory_other[holder[i]][1]):
                    y = y + memory_other[holder[i]][2]
                elif (holder[i] == 'e'):
                    y = y + str('math.e')
                elif(holder[i] == '^'):
                    y = y + str('**')
                elif(holder[i] in memory_skip):
                    pass
                elif(holder[i] in memory_for_x and holder[i-1] == 'x'):
                    pass
                else:
                    y = y + holder[i] 
        funcion_list.append(y)
        
        return funcion_list
                

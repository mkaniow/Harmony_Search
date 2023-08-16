class Solve():
    def solve(function, args):
        '''
        Returns the value of function for given variables

        Parameters
        ----------
        function : list
            Returned from parser_module.py
        args : list
            Variables to the function
                    
        Returns
        -------
        Value of function : float
        '''

        y = {}
        i = 1

        for item in args:
            y[i] = item
            i += 1
        
        final_function = ''

        for i in range(len(function)):
            if function[i] in y:
                final_function = final_function + str(y[function[i]])
            else:
                final_function = final_function + function[i]

        return eval(final_function)
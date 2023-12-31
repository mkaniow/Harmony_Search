import matplotlib.pyplot as plt

# Create Scatter Plot

class Plot():
    def plot(data, xmin, xmax, ymin, ymax):
        '''
        Plots the cords from memory (X1, X2)

        Parameters
        ----------
        data : list
            Release in format [[[...], ...], ..., [[...], ...]]
        xmin : int / float
        xmax : int / float
        ymin : int / float
        ymax : int / float
                    
        Returns
        -------
        scatter plot
        '''
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        X = []
        Y = []
        for item in data:
            x = item[0][0]
            y = item[0][1]
            X.append(x)
            Y.append(y)
        plt.scatter(X, Y)
        plt.title("Scatter Plot")
        plt.xlabel("X1-Axis")
        plt.ylabel("X2-Axis")
        plt.pause(0.001)
        plt.clf()
    plt.show()
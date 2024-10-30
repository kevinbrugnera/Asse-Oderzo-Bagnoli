import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


#------------------------------------------------------------------------------
#Sezione dove si crea la classe

class AgedPlot:
    def __init__(self, filepath, ascissa, ordinata):
        self.path = filepath
        self.x = ascissa
        self.y = ordinata
        
#------------------------------------------------------------------------------
#SottoSezione dove si implementa il metodo per leggere Nemo_6670

    def load_data(self):
        self.DataFrame = pd.read_csv(self.path, delim_whitespace=True)
        
        self.datax = self.DataFrame[self.x]
        self.datay = self.DataFrame[self.y]
        self.age = self.DataFrame['age_parent']
        
        print(self.datax, self.datay)

#------------------------------------------------------------------------------
#SottoSezione dove si implementa i bin

    def bins(self):
        nbin = 25

        bins = pd.cut(self.DataFrame['age_parent'],bins=nbin)
        self.DataFrame['bin_age'] = bins

        self.grouped = self.DataFrame.groupby('bin_age')

#------------------------------------------------------------------------------
#SottoSezione dove si implementa il plot
       
    def plot(self):
        plt.figure(figsize=(12, 8))     

        for name, group in self.grouped:
             plt.scatter(group[self.x], -group[self.y], label=f'{name} Gyr', marker='.', c=group['age_parent'], cmap='terrain')

        plt.legend(title='Age Bins', loc='upper right')
        plt.xlabel(self.x)  # Usa self.x per l'etichetta dell'asse x
        plt.ylabel(self.y)  # Usa self.y per l'etichetta dell'asse y
        plt.title('Scatter Plot of Stars Grouped by Age')

        plt.tight_layout()
        plt.show()

        
#------------------------------------------------------------------------------
        
Nemo = AgedPlot('C:\\Users\\kevin\\Desktop\\Python\\Nemo_6670.txt', 'b_y', 'MsuH')
Nemo.load_data()  # Questo è dove verrà stampato il contenuto delle colonne
Nemo.bins()
Nemo.plot()


















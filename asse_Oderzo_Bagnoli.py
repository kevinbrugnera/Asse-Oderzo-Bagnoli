import matplotlib.pyplot as plt
import pandas as pd

# Imposta lo stile del grafico su sfondo scuro
plt.style.use('dark_background')

# Classe AgedPlot per creare grafici con raggruppamenti in base a valori di età
class AgedPlot:
    def __init__(self, filepath, ascissa, ordinata, binnaggio):
        """
        Inizializza l'oggetto AgedPlot con il percorso del file, le colonne 
        per l'asse x e y, e la colonna da utilizzare per il raggruppamento in bin.
        
        Parametri:
        - filepath: Percorso al file di dati.
        - ascissa: Nome della colonna per l'asse x.
        - ordinata: Nome della colonna per l'asse y.
        - binnaggio: Nome della colonna su cui fare il binning.
        """
        self.path = filepath
        self.x = ascissa
        self.y = ordinata
        self.bin = binnaggio
        
    def load_data(self):
        """
        Carica i dati da un file e crea Serie per le colonne specificate 
        da x, y e bin
        """
        self.DataFrame = pd.read_csv(self.path, delim_whitespace=True)
        
        # Serie dei dati di interesse
        self.datax = self.DataFrame[self.x]
        self.datay = self.DataFrame[self.y]
        self.age = self.DataFrame[self.bin]
        
    def bins(self):
        """
        Raggruppa i dati in 25 bin basati sui valori nella colonna `bin`.
        Aggiunge una colonna `bin_int` al DataFrame per indicare l'intervallo 
        di ogni bin e crea un oggetto `grouped` per il raggruppamento.
        """
        nbin = 25
        bins = pd.cut(self.DataFrame[self.bin], bins=nbin)
        self.DataFrame['bin_int'] = bins
        self.grouped = self.DataFrame.groupby('bin_int')
        
    def plot(self):
        """
        Crea uno scatter plot con i dati raggruppati per la colonna di binning.
        Colora i punti in base all'età raggruppata e mostra una legenda.
        """
        plt.figure(figsize=(14, 10))
        
        # Plot per ogni gruppo di dati
        for name, group in self.grouped:
            plt.scatter(group[self.x], -group[self.y], 
                        label=f'{name}', marker='.', c=group[self.bin], 
                        cmap='cool', alpha=0.7)

        # Etichette e titolo del grafico
        plt.legend(title=f'{self.bin} bins', loc='upper right')
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title('Scatter Plot of Stars Grouped by {}'.format(self.bin))
        plt.tight_layout()
        plt.show()

# Inizializzazione di un elemento della classe (apposita per l'es.)
Nemo = AgedPlot('C:\\Users\\kevin\\Desktop\\Python\\Nemo_6670.txt', 'b_y', 'M_ass', 'age_parent')
#Uso della classe per un grafico specifico (quello dell'es.)
Nemo.load_data()
Nemo.bins()
Nemo.plot()


















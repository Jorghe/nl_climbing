import pandas as pd
import time
import sys

from settings import Settings

DEPORTIVA = Settings.DEPORTIVA
VERMIN = Settings.VERMIN
DROP_COL = Settings.DROP_COLUMNS


class nlCrag(object):
    url: str
    crag: pd.DataFrame
    boulders: pd.DataFrame
    by_zone: pd.DataFrame
    projects: pd.DataFrame
    _filename = Settings.Default

    def __init__(self, url = _filename):
        self.url = url
        self.nombre = 'huaste'
    
    def describe(self):
        print(self.crag.size)
        return self.url
    
    def initialize(self):
        """
            First function to create self.crag dataframe, runs normalize(), organizes routes by zone and saves the file
        """
        if self.url == '': return False
        print(f"Reading routes from {self.url} ")
        qStart = time.time()

        self.crag = self.read_html()
        # self.crag = self.read_file('json')
        self.normalize()
        self.crag_by_zone()
        self.save_file(format="json")
        
        qEnd = time.time()
        qTime = (qEnd-qStart)*(10**3)
        print(f"Tiempo de ejecución: {qTime} segundos")

        return True if self.crag.size > 0 else False
    
    def normalize(self):
        """ 
            Second function to remove nan and complete table with last value
        """
        try:
            # Complete table with previous row index
            for ind, ruta in self.crag['Grade'].items():
                if ind == 0: continue
                if pd.isna(ruta):
                    self.crag['Grade'][ind] = self.crag['Grade'][ind-1]
            # Create Boulder and Project section
            _grado = self.crag['Grade']
            self.projects = self.crag[_grado == '?'] # .reset_index(inplace=True, drop = True)
            self.boulders = self.crag[_grado.isin(VERMIN)]

            self.crag = self.crag[~_grado.isin(self.projects['Grade'])] 

        except IndexError:
            print('Index error')
            return False
    
    def read_html(self):
        # Check if file path exists
        web_page = pd.read_html(self.url)[-1] # Last table contains all routes in grade order
        return web_page.drop(columns = DROP_COL )
    
    def read_file(self, format="json"):
        print(format)
        try:
            
            if format == "json":
                file = pd.read_json(f"{self.nombre}.json" )
            elif format == "csv":
                file= pd.read_csv(f"{self.nombre}.csv")
            return file
        except :
          print( 'Something went wrong')
        finally:
          print('The try except is finished')

        
    
    def save_file(self, format="json"):
        if self.crag.size < 1: return False
        # TODO: Check if file is available
        filename = self.nombre
        if format == "csv":
            self.crag.to_csv(+filename +".csv")
        else: 
            self.crag.to_json(filename +'.json')

    def crag_by_zone(self):

        self.by_zone = self.crag.groupby(['Area'])


if __name__ == '__main__':
    print('Initialization started crag')
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) > 1:
        # Instantiate all crags
        print("Support for all crags unavailable")
    nlCrag = nlCrag()
    nlCrag.initialize()
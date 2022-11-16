class Settings(object):
    def __init__(self):
        pass

    class Zonas:
        all = ("epc", "salto", 'huaste')
        EPC = {"name": "El Potrero Chico", 
                "alias": "epc",
                "web": "https://www.thecrag.com/es/escalar/mexico/el-potrero-chico/guide"}
        Huasteca = {"name": "La Huasteca",
                    "alias": "huaste",
                    "web" : "https://www.thecrag.com/es/escalar/mexico/la-huasteca/guide"}
        Salto = {"name": "El Salto",
                "alias": "salto",
                "web": "https://www.thecrag.com/es/escalar/mexico/el-salto/guide"}

    
    DEPORTIVA = ['5.6', '5.7', '5.8', '5.9',
                '5.10', '5.10a', '5.10b', '5.10c', '5.10d',
                '5.11', '5.11a', '5.11b', '5.11c', '5.11d',
                '5.12', '5.12a', '5.12b', '5.12c', '5.12d',
                '5.13', '5.13a', '5.13b', '5.13c', '5.13d',
                '5.14', '5.14a', '5.14b', '5.14c', '5.14d',
                '5.15', '5.15a', '5.15b', '5.15c', '5.15d']
    
    VERMIN = ['V0', 'V1', 'V2', 'V3', 'V4','V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16']
    DROP_COLUMNS = ['Unnamed: 1', 'Stars', 'Pop']
    Default = Zonas().Huasteca["web"]


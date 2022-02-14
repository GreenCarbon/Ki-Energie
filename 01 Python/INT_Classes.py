from SQL_Tools import *

from configparser import ConfigParser
import logging 

config = ""

# Externe Parameter, welche beim Aufruf übergeben werden
class ext_params() :
    pass; 
    
 

# Hier werden alle Parameter bereitgestellt, welche über Config-File(s) beim Programmstart eingelesen werden
class config_params() :
    pass
    


# Interne Parameter, welche global für die Session angelegt werden
class int_params() :
    pass
    


class env_params() :
    pass


class tools() :
    def getCurYear() :
        return 20
    
 
# Aufruf der Systeminitialisierung. Hat alles funktioniert, wird True zurückgeliefert, bei Fehlern FALS
def SystemInit() :
    connect_database()
    parseConfig('Config.ini')
    return True

def getVal(var1):
    return var1


def parseConfig(cfgFile):
    global config
    config = ConfigParser()
    print (config.read(cfgFile))
  
    print ("Sections : ", config.sections())
    sections = config.sections()
    for sec in sections: 
        print("Sections : ", sec)
        for key in config[sec]:  
            try:
                print(sec, " ", key, " " , config[sec][key])
            except:
                pass
            
def getConfigParam(p_Section, p_Key):
    global config
    return    config[p_Section][p_Key]         
    
def initLogger(name):
# Logger Config Beispiele:
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    #logging.warning('This is a Warning')
    #logging.basicConfig(filename='Optimizer.log', filemode='a', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    #logging.basicConfig()
    #logging.debug('Logging startet')
    #formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    #logFileName = 'Log.txt'
    #fh = logging.FileHandler(logFileName)
    #fh = RotatingFileHandler(filename=logFileName, mode="a", maxBytes=1310720, backupCount=50)
    
    #handler = logging.StreamHandler()
    #handler.setFormatter(formatter)
    
    #logger = logging.getLogger(name)
    #logger.basicConfig(filename='Optimizer.log', filemode='a', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    #logger.setLevel(logging.DEBUG)
    #logger.addHandler(handler)
    #return logger
    logfile = getConfigParam('LOG', 'logfile')    
    logging.basicConfig(filename=logfile,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    logger = logging.getLogger(name)
    logging.info("Running Decarbonara ")

    return logger
    
    
    
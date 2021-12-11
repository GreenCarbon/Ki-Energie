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
    

# Aufruf der Systeminitialisierung
def SystemInit() :
    return True
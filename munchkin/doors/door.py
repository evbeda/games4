class Door:
    def __init__(self, name):
        #Atributo comun de todos los doors
        self.name = name

    def __str__(self):
        return 'Name: ' + str(self.name)

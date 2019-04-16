class cubo(object):
    def __init__(self, nombre, on, clear, onTable):
        self.nombre = nombre
        self.on = on
        self.clear = clear
        self.onTable = onTable

    def toTableValid(self):
        if self.clear and not self.onTable: #Si el cubo esta clear y no esta sobre la mesa se puede mover a la mesa
            return True
        return False

    def tableToTowerValid(self, cubo):
        if self.nombre == cubo.nombre:  #Si es el mismo cubo no se puede
            return False
        if not self.clear:  #Si el cubo original no esta clear no se puede mover
            return False
        if not self.onTable:    #Si el cubo original no esta en la mesa no se puede mover
            return False
        if not cubo.clear:  #Si el cubo destino no esta clear no se puede mover
            return False
        return True

    def towerToTowerValid(self, cubo):
        if self.nombre == cubo.nombre:  #Si es el cubo destino es el mismo que el cubo original no se puede mover
            return False
        if not self.clear:  #Si el cubo original no esta clear no se puede mover
            return False
        if self.onTable:    #Si el cubo original esta sobre la mesa no se puede mover
            return False
        if not cubo.clear:  #Si el cubo destino no esta clear no se puede mover
            return False
        return True

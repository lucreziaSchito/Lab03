class Strumento :
    def __init__(self, id_strumento, tipo_strumento, marca, anno_acquisto, valore):
        self.__id_strumento = id_strumento
        self.__tipo_strumento = tipo_strumento
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore

    @property
    def id_strumento(self):
        return self.__id_strumento

    @property
    def marca(self):
        return self.__marca

# sto estraendo in sola lettuta (senza possibilità di modifica da parte dell'utente) le due variabili che mi
    #interessano per il salvataggio all'interno del dizionario e per l'ordinamento alfabetico

    def __str__(self) :
        pass
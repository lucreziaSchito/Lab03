class Prestito:
    def __init__(self, cod_prestito, data, cod_strumento, cognome_allievo):
        self.__id_prestito = cod_prestito
        self.__data = data
        self.__id_strumento = cod_strumento
        self.__cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.__id_prestito}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"



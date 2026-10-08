from csv import reader
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.__responsabile = responsabile
        self.DictDeposito = {}

    @property   # GETTER: legge il valore privato
    def responsabile(self):
        return self.__responsabile
    @responsabile.setter  # SETTER: modifica il valore
    def responsabile(self, nuovo_resp):
        self.__responsabile = nuovo_resp
    #eventualmente posso inserire controlli e verifiche


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try :
            fileIn = open(file_path, "r")
            CsvReader = reader(fileIn)
            for line in CsvReader:
                self.DictDeposito[line[0]] = [line[1], line[2], line[3], line[4]]
        except FileNotFoundError:
            raise FileNotFoundError("Il percorso del file non è stato trovato. Controlla e riprova.")
        fileIn.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        progressivo = len(self.DictDeposito)
        self.DictDeposito[f"S{progressivo + 1}"] = [tipo, marca, anno_acquisto, valore]

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        lista_strumento_marche = []
        for key in self.DictDeposito:
            marca = self.DictDeposito[key][1]
            lista_strumento_marche.append((key, marca))
        lista_strumento_marche.sort(key = attrgetter('marca'))
        return lista_strumento_marche

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        progressivo = 1
        id_prenotazione = f"P{progressivo}"
        try :
            ###
            pass
        except Exception:
            raise Exception("Non è possibile richiedere il prestito")

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO

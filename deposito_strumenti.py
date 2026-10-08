from csv import reader
from operator import attrgetter
from strumento import Strumento
from prestito import Prestito

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
                s = Strumento(line[0],line[1], line[2], line[3], line[4])
                self.DictDeposito[s.id_strumento] = s
            fileIn.close()
        except FileNotFoundError:
            raise FileNotFoundError("Il percorso del file non è stato trovato. Controlla e riprova.")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        progressivo = len(self.DictDeposito)
        codice_strumento = f"S{progressivo + 1}"
        s = Strumento(codice_strumento, tipo, marca, anno_acquisto, valore)
        self.DictDeposito[s.id_strumento] = s
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        # ho estratto gli oggetti Strumento dal dizionario (i valori)
        # sorted() li ordina usando l'attributo 'marca' di ogni singolo oggetto.
        return sorted(self.DictDeposito.values(), key=attrgetter('marca'))


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        try :
            # memorizzo tutti i prestiti in una lista
            lista_prestiti = []
            progressivo = len(lista_prestiti) + 1
            id_prenotazione = f"P{progressivo}"
            p = Prestito(id_prenotazione, data, id_strumento, cognome_allievo)
            if id_strumento not in self.DictDeposito :
                raise Exception("L'ID strumento da lei inserito non è presente all'interno del deposito")
            elif p in lista_prestiti:
                raise Exception("Strumento attualmente non disponibile, risulta essere già impeganto in un prestito")
            else :
                lista_prestiti.append(p)

        except Exception:
            print("Non è stato possibile accettare la richiesta di prestito")

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        try :
            #if id_prestito in lista_
            pass
        except Exception :
            print("") ###

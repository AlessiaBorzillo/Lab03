from prestito import Prestito
from strumento import Strumento
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path, "r") as file:
            for riga in file:
                riga = riga.strip()
                if riga:
                    parti = riga.split(",")
                    id_strumento = parti[0]
                    tipo = parti[1]
                    marca = parti [2]
                    anno_acquisto = int(parti [3])
                    valore = float(parti [4])
                    s = Strumento(id_strumento, tipo, marca, anno_acquisto, valore)
                    self.strumenti[id_strumento] = s


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        #trovo numero piu alto in modo tale da assegnare allo strumento aggiunto il valore subito successivo
        max_id = 0
        for id_str in self.strumenti:
            num = int(id_str[1:]) #estraggo parte numerica dopo la S
            if num > max_id:
                max_id = num
        nuovo_id = f"S{max_id + 1}"
        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti[nuovo_id] = nuovo_strumento   #salvo nel dizionario e restutuisco l'oggetto
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti.values(), key =lambda s: s.marca)
    #ordino gli studenti x marca in ordine alfabetico

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        #1o controllo lo strumento deve esistere nel sistema
        if id_strumento not in self.strumenti:
            raise Exception("Lo strumento non esiste nel sistema")
        #2o controllo
        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception("Lo strumento è gia in prestito")
        #genero nuovo ID con prefisso P
        max_id = 0
        for id_p in self.prestiti:
            num = int(id_p[1:]) #estraggo parte numerica dopo la S
            if num > max_id:
                max_id = num
        nuovo_id = f"P{max_id + 1}"
        p = Prestito(nuovo_id, data, id_strumento, cognome_allievo)
        self.prestiti[nuovo_id] = p
        return p

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        #concludere il prestito, rimuovendo ogni riferimento dal sistema. Se il codice
        # non corrisponde ad alcun prestito esistente, il metodo deve scatenare un'eccezione
        if id_prestito in self.prestiti:
            del self.prestiti[id_prestito]
        else:
            raise Exception("Prestito non trovato")
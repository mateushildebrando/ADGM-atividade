from config import *

class Nacao(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    populacao = Required(int)
    pib = Required(float)
    pib_per_capita = Required(float)
    continente = Required(str)
    idiomas = Required(str)
    moeda = Required(str)
    area = Required(float)
    capital = Required(str)
    governo = Required(str)
    
    def __str__(self):
        return f'{self.nome}, {self.populacao}, {self.pib}, {self.pib_per_capita}, {self.continente}, {self.idiomas}, {self.moeda}, {self.area}, {self.capital}, {self.governo}'

db.bind(provider='sqlite', filename='nacao.db', create_db=True)
db.generate_mapping(create_tables=True)

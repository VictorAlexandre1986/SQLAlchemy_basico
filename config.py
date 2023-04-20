from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,String,DateTime,Integer
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'site.db')

#Atributo echo mostra os comandos SQL quando executado via sqlalchemy
engine = create_engine(connection_string, echo=True)

Base = declarative_base()

Session = sessionmaker()




class User(Base):
    __tablename__="Usuario"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    endereco = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    sexo = Column(String(1), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    data_criada = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, name, endereco, bairro, sexo, cpf):
        self.name = name
        self.endereco = endereco
        self.bairro = bairro
        self.sexo = sexo
        self.cpf = cpf
        
    def __repr__(self):
        return f"<Usuario  name={self.name} cpf={self.cpf} endereco={self.endereco} bairro={self.bairro} sexo={self.sexo}>"
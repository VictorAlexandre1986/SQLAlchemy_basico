from config import User
from config import Session
from config import engine
from sqlalchemy import desc


local_session = Session(bind=engine)

class Crud:
    
    @staticmethod
    def create_user(nome, endereco, bairro,cpf,sexo):
        new_user = User(name=nome, endereco=endereco, bairro=bairro, cpf=cpf, sexo=sexo )
        local_session.add(new_user)
        local_session.commit()
        
    @staticmethod
    def get_user_with_limit(name):
        #Retorna todos os objetos da tabela
        users = local_session.query(User).all()[:2]
        for user in users:
            print(user.name)
            
    @staticmethod
    def get_user():
        users = local_session.query(User).all()
        for user in users:
            print(user.name)
            
    @staticmethod
    def get_user_by_id(id):
        user = local_session.query(User).filter_by(id=id).one_or_none()
        print(user)
        
    @staticmethod
    def get_user_order_by_asc():
        users = local_session.query(User).order_by(User.name).all()
        for user in users:
            print(user.name)
            
    @staticmethod
    def get_user_order_by_desc():
        users = local_session.query(User).order_by(desc(User.name)).all()
        for user in users:
            print(user.name)
        
    @staticmethod
    def update_user(id,name,endereco,bairro,cpf,sexo):
        user_to_update = local_session.query(User).filter_by(id=id).first()
        user_to_update.name = name
        user_to_update.endereco = endereco
        user_to_update.bairro = bairro
        user_to_update.cpf = cpf
        user_to_update.sexo = sexo
        local_session.commit()
        
    @staticmethod
    def delete_user(id):
        user = local_session.query(User).filter_by(id=id).first()
        local_session.delete(user)
        local_session.commit()
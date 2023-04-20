from models.model import Crud
    
if __name__ == "__main__":
    #Adicionando apenas um
    #Crud.create_user("Alexandre","Dom Pedro I","Centro","55466578521","M")
    
    
    #Adicionando uma lista
    # lista_usuario = [
    #     {"name":"Victor","endereco":"Dom Pedro I","bairro":"Centro","cpf":"11122233345","sexo":"M"},
    #     {"name":"Cleide","endereco":"Dom Pedro I","bairro":"Centro","cpf":"11122233346","sexo":"F"},
    # ]
    
    # for usuario in lista_usuario:
    #     Crud.create_user(usuario['name'],usuario['endereco'],usuario['bairro'],usuario['cpf'],usuario['sexo'])

    #Crud.get_user_by_id(2)
    
    #Crud.get_user_with_limit("Alexandre")
    
    #Crud.get_user_order_by_asc()
    
    Crud.get_user_order_by_desc()
    
   #Crud.get_user()
   
   #Crud.update_user(1,"Ribeiro","Adhemar de Barros","Centro","55566677754","M")

    #Crud.delete_user(1)
def main():
    nome=""
    idade=0
    email=""
    cidade=""
    profissao=""
    while True:
        print("\n===MENU===")
        print("1. cadastrar usuaro")
        print("2. ver dados cadastrados")
        print("3.sair do sistema")
        print("==============================")
        opcao=int(input("Escolha uma opçao"))
        if opcao==1:
            nome= input("Digite seu nome:")
            idade=int(input("Digite sua idade:"))
            email=input("Digite seu email:")
            cidade=input("Digite sua cidade:")
            profissao=input("Digite sua profissao:")
            print("Usuario cadastrado com sucesso!")
        elif opcao==2:
            print("\n===DADOS CADASTRADOS===")
            print(f"nome:{nome}")
            print(f"idade:{idade}")
            print(f"email:{email}")
            print(f"cidade:{cidade}")
            print(f"profissao:{profissao}")
            print("==============================")
        if opcao==3:
            print("\nSaindo do sistema.")
            break
if __name__ == "__main__":
    main()




    
        
        




print("Digite o nome do arquivo html que deseja converter os dados css inline para extern !!! /n")

nomeDoArquivo = input()

print("Digite o nome da classe que sera referenciada no arquivo , a classe tende ao nome do arquivo !!! /n")

nomeDaClasse = input()

try:
   
    with open(nomeDoArquivo, 'r') as arquivo:
       
        arq = arquivo.read()
        
except FileNotFoundError:
    print(f"O arquivo '{nomeDoArquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo: {e}")

print("Digite o nome do arquivo css externo que voce deseja criar /n/n")

nomeDoCss = input()
nomeDoCss+=".css"
cont=0;local=0;acerto=0;nomeClasseBase="."+nomeDaClasse;conteudoArquivo="";inicioClasse="{";fimClasse="}";saida="";contadorClass=0
while cont < len(arq):
    if arq[cont] == "s":
        local = cont
        local += 1
        if arq[local] == "t":
             acerto+=1
             local += 1
        if arq[local] == "y":
             acerto+=1
             local += 1
        if arq[local] == "l":
             acerto+=1
             local += 1
        if arq[local] == "e":
             acerto+=1
             local += 1
        if arq[local] == "=":
             acerto+=1
             local += 2
       
        if acerto == 5 :
            while arq[local] != '"' :
                conteudoArquivo+=arq[local]
                local += 1
            contadorClass+=1
            saida+=nomeClasseBase+str(contadorClass)+inicioClasse+"\r"+conteudoArquivo+"\r"+fimClasse+"\r\r\r"
            conteudoArquivo=""

        acerto=0
    cont += 1

with open(nomeDoCss, 'w') as file_destino:
    file_destino.write(saida)

            


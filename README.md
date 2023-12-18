Automação de Impressão de Etiquetas
Este código tem como objetivo automatizar o processo de impressão de arquivos, especialmente aqueles gerados como etiquetas de peças durante o processo de bipagem na produção. 
Quando um arquivo PDF com a nomenclatura "Etiqueta" é detectado na pasta de downloads, o programa inicia automaticamente o leitor de PDF Adobe Acrobat para imprimir o arquivo na impressora padrão designada. 
Após a conclusão da impressão, o arquivo é excluído.

Instruções de Uso
Configuração da Pasta de Downloads: Antes de executar o programa, certifique-se de ajustar o caminho da pasta de downloads conforme necessário. 
Isso pode ser feito modificando a variável de caminho no código para refletir o usuário do computador.
caminho_da_pasta_download = "Caminho/Para/Sua/Pasta/Downloads"

Configuração do Leitor de PDF:
Se estiver utilizando um leitor de PDF diferente do Adobe Acrobat, ajuste o caminho do executável correspondente.
caminho_do_executavel_pdf = "Caminho/Para/Seu/Executavel/PDF/Leitor.exe"

Como Funciona
Este código foi desenvolvido para resolver a necessidade de automatizar a impressão de etiquetas, particularmente quando essas etiquetas são geradas por meio de bipagem de peças na produção. 
Em cenários nos quais o navegador web não permite a impressão direta sem a confirmação do usuário, o arquivo é baixado para a pasta de downloads, desencadeando a execução deste programa.

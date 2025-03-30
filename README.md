PT/BR: 
Explicação do Funcionamento
O código é dividido em funções principais: preprocess_pdf, search_word e a função principal main.

Função preprocess_pdf(pdf_path)
Esta função recebe o caminho de um arquivo PDF, extrai seu texto usando pdfminer e cria um índice de palavras. O índice é armazenado em um dicionário (indexed_words), onde as palavras são as chaves e o valor é uma lista das páginas onde a palavra aparece. O texto extraído é dividido por páginas, e cada palavra do texto é registrada no índice.

Entrada: Caminho do PDF

Saída: Dicionário onde as chaves são palavras e os valores são listas com números das páginas.

Função search_word(indexed_pdfs, word)
Essa função é responsável pela pesquisa de uma palavra no índice criado pelos PDFs. Ela recebe o índice de todos os PDFs (indexed_pdfs) e a palavra que o usuário deseja buscar. O índice é percorrido, e a função retorna os PDFs e as páginas onde a palavra aparece. As páginas são ordenadas e duplicadas são removidas.

Entrada: Dicionário com o índice de PDFs e a palavra a ser pesquisada.

Saída: Lista de resultados com o nome do arquivo e as páginas encontradas.

Função main()
A função principal do script é responsável pela interação com o usuário. Ela solicita o caminho da pasta onde os PDFs estão localizados, chama a função de indexação para todos os PDFs na pasta e, em seguida, permite que o usuário digite uma palavra para buscar nos documentos. O loop continuará até o usuário digitar sair.

Entrada: Caminho da pasta dos PDFs.

Saída: Exibe os resultados da pesquisa ou uma mensagem de "não encontrado" se a palavra não estiver nos documentos.

EN:

The code is divided into three main functions: preprocess_pdf, search_word, and the main function main.

Function preprocess_pdf(pdf_path)
This function receives the path to a PDF file, extracts its text using pdfminer, and creates a word index. The index is stored in a dictionary (indexed_words), where the words are the keys and the values are lists of page numbers where the word appears. The extracted text is split by pages, and each word is recorded in the index.

Input: Path to the PDF file.

Output: Dictionary where keys are words and values are lists of page numbers.

Function search_word(indexed_pdfs, word)
This function is responsible for searching a word in the index created by the PDFs. It receives the index of all PDFs (indexed_pdfs) and the word the user wants to search. It loops through the index and returns the PDFs and pages where the word appears. Pages are sorted, and duplicates are removed.

Input: Dictionary of indexed PDFs and the word to search.

Output: List of results with file names and pages where the word is found.

Function main()
The main function handles user interaction. It prompts the user for the folder path containing the PDFs, calls the indexing function for all PDFs in the folder, and then allows the user to type a word to search within the documents. The loop will continue until the user types sair.

Input: Path to the PDF folder.

Output: Displays search results or a "not found" message if the word is not in the documents.

import os
import re
from collections import defaultdict
from pdfminer.high_level import extract_text
import logging

logging.getLogger("pdfminer").setLevel(logging.ERROR)  # Silencia avisos do pdfminer

def preprocess_pdf(pdf_path):
    raw_text = extract_text(pdf_path)
    indexed_words = defaultdict(list)
    
    for page_num, page_text in enumerate(raw_text.split('\f'), start=1):  # Divide por páginas
        for word in page_text.split():
            indexed_words[word.lower()].append(page_num)
    
    return indexed_words

def search_word(indexed_pdfs, word):
    results = []
    word = word.lower()
    
    for pdf_name, indexed_words in indexed_pdfs.items():
        pages = indexed_words.get(word, [])
        if pages:
            results.append((pdf_name, sorted(set(pages))))
    
    return results

def main():
    folder_path = "./pdfs"  # Caminho da pasta contendo os PDFs
    indexed_pdfs = {}
    
    print("Processando os PDFs...")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            indexed_pdfs[filename] = preprocess_pdf(pdf_path)
    
    print("Todos os PDFs foram indexados com sucesso!")
    
    while True:
        word = input("Digite a palavra para pesquisar (ou 'sair' para encerrar): ").strip()
        if word.lower() == 'sair':
            break
        
        results = search_word(indexed_pdfs, word)
        if results:
            for pdf_name, pages in results:
                print(f"A palavra '{word}' foi encontrada no arquivo '{pdf_name}' nas páginas: {pages}")
        else:
            print(f"A palavra '{word}' não foi encontrada em nenhum documento.")

if __name__ == "__main__":
    main()

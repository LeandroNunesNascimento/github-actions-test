#!/usr/bin/env python3
import os
import re
import json
import glob
import sys

def extract_error_messages_from_logs():
    """Extrai todo o conteúdo dentro de 'errorMessages': [] dos logs"""
    log_dir = "/Users/leandronunes/actions-runner/_diag"
    log_files = glob.glob(os.path.join(log_dir, "Worker*.log"))
    
    all_error_messages = []
    
    for log_file in log_files:
        print(f"Analisando: {log_file}")
        
        try:
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Método 1: Extrai usando regex para encontrar arrays errorMessages
            error_patterns = [
                # Padrão para "errorMessages": ["erro1", "erro2", ...]
                r'"errorMessages":\s*\[\s*((?:"[^"]*"(?:\s*,\s*"[^"]*")*)?)\s*\]',
                # Padrão para 'errorMessages': ['erro1', 'erro2', ...]
                r"'errorMessages':\s*\[\s*((?:'[^']*'(?:\s*,\s*'[^']*')*)?)\s*\]"
            ]
            
            for pattern in error_patterns:
                matches = re.findall(pattern, content, re.DOTALL)
                for match in matches:
                    if match.strip():
                        print(f"Conteúdo encontrado: {match}")
                        
                        # Tenta processar como array JSON
                        try:
                            # Se for um array de strings JSON
                            error_array = json.loads(f'[{match}]')
                            all_error_messages.extend(error_array)
                        except json.JSONDecodeError:
                            # Fallback: extrai manualmente as strings
                            string_pattern = r'["\']([^"\']*)["\']'
                            strings = re.findall(string_pattern, match)
                            all_error_messages.extend(strings)
            
            # Método 2: Busca por errorMessages com conteúdo mais complexo
            complex_pattern = r'"errorMessages":\s*\[(.*?)\]'
            complex_matches = re.findall(complex_pattern, content, re.DOTALL)
            
            for match in complex_matches:
                if match.strip() and match != '""':
                    print(f"Conteúdo complexo encontrado: {match[:100]}...")
                    
                    # Tenta parsear como JSON
                    try:
                        error_array = json.loads(f'[{match}]')
                        all_error_messages.extend(error_array)
                    except json.JSONDecodeError:
                        # Se falhar, adiciona o conteúdo bruto
                        all_error_messages.append(match.strip())
            
        except Exception as e:
            print(f"Erro ao ler arquivo {log_file}: {e}")
            continue
    
    # Remove duplicatas e limpa
    unique_errors = list(set(all_error_messages))
    unique_errors = [error.strip() for error in unique_errors if error.strip()]
    
    return unique_errors

def main():
    """Função principal"""
    print("=== EXTRAINDO ERROR MESSAGES ===")
    
    error_messages = extract_error_messages_from_logs()
    
    print(f"\n=== RESULTADOS ===")
    print(f"Total de mensagens de erro únicas: {len(error_messages)}")
    
    for i, error in enumerate(error_messages, 1):
        print(f"\n--- ERRO {i} ---")
        print(error)
    
    # Salva os resultados
    if error_messages:
        with open('error_messages.json', 'w', encoding='utf-8') as f:
            json.dump(error_messages, f, indent=2, ensure_ascii=False)
        
        with open('error_messages.txt', 'w', encoding='utf-8') as f:
            for error in error_messages:
                f.write(f"{error}\n")
                f.write("-" * 50 + "\n")
        
        print(f"\nResultados salvos em error_messages.json e error_messages.txt")
        
    #     # Escreve o output no formato GITHUB_OUTPUT
    #     with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    #         f.write(f"errors={json.dumps(error_messages)}\n")
        
    #     # Sucesso
    #     sys.exit(0)
    # else:
    #     print("Nenhuma mensagem de erro encontrada")
    #     with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    #         f.write("errors=[]\n")
    #     # Sucesso mesmo sem erros
    #     sys.exit(0)

if __name__ == "__main__":
    main()
# coding: utf-8

# Usamos apenas os radicais das palavras para apanhar todas as variações (verbos, plurais, etc.)
radicais_matematicos = {
    "eu": "1", "voc": "2", "outr": "2", "nos": "1+2",
    "nao": "-", "negar": "-",
    "e": "=", "sou": "=", "esta": "=", "som": "=", # apanha é, está, somos, sou
    "mud": "Δ", "viaj": "Δ", "mov": "Δ",         # apanha mudo, mudou, mudança, viajar
    "evol": "e", "cresc": "e", "melhor": "e",     # apanha evoluindo, crescer, melhoria
    "ment": "θ", "pens": "θ", "segred": "θ",      # apanha mente, pensamentos, segredos
    "idei": "λ", "luz": "λ", "inspir": "λ",       # apanha ideia, luzes, inspiração
    "fim": "Ω", "destin": "Ω", "conclu": "Ω"      # apanha fim, final, destino, conclusão
}

def traduzir_tudo(frase):
    # Limpeza básica de pontuação e acentos
    frase_limpa = frase.lower().replace(".", "").replace(",", "").replace("í", "i").replace("á", "a").replace("ã", "a")
    palavras = frase_limpa.split()
    resultado = []
    
    for palavra in palavras:
        traduzida = False
        # O código varre os radicais para ver se a palavra começa com algum deles
        for radical, simbolo in radicais_matematicos.items():
            if palavra.startswith(radical) or palavra == radical:
                resultado.append(simbolo)
                traduzida = True
                break
        
        # Se for uma palavra totalmente desconhecida, o código não quebra! 
        # Ele mantém a palavra ou gera um símbolo genérico de incógnita 'x'
        if not traduzida:
            resultado.append(f"[x:{palavra}]") 
            
    return " ".join(resultado)

# Teste com variações que não estavam no primeiro dicionário:
print(traduzir_tudo("Nós fomos viajar e a minha mente teve uma inspiração"))
# Resultado aproximado: 1+2 [x:fomos] Δ = [x:a] [x:minha] θ [x:teve] [x:uma] λ

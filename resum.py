import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def gerar_resumo(texto, numero_sentencas=5):
    # Tokenização de sentenças e palavras
    sentencas = sent_tokenize(texto)
    palavras = word_tokenize(texto)

    # Remover stopwords (palavras comuns que geralmente não contêm informações importantes)
    palavras_sem_stopwords = [palavra.lower() for palavra in palavras if palavra.isalnum() and palavra.lower() not in stopwords.words('portuguese')]

    # Calcular a frequência das palavras
    frequencia = FreqDist(palavras_sem_stopwords)

    # Atribuir pontuação a cada sentença com base na frequência das palavras
    pontuacao_sentencas = {sentenca: sum([frequencia[palavra] for palavra in word_tokenize(sentenca.lower()) if palavra.isalnum()]) for sentenca in sentencas}

    # Selecionar as top N sentenças para formar o resumo
    resumo = ' '.join([sentenca for sentenca, pontuacao in sorted(pontuacao_sentencas.items(), key=lambda x: x[1], reverse=True)[:numero_sentencas]])

    return resumo

# Exemplo de uso
texto_completo = '''
Seu texto longo aqui. Pode conter várias frases e parágrafos.
'''

resumo_gerado = gerar_resumo(texto_completo)
print(resumo_gerado)

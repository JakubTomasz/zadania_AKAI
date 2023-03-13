# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

#https://www.youtube.com/watch?v=oHC1230OpOg
# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

def allowed(char):
    return char.isalnum() or char == ' '
def word_ranking(list_of_sentences,number_of_ranks=3):
    dict_of_words={}
    for sentence in list_of_sentences:
        words_in_sentance=''.join(filter(allowed,sentence.lower())).split(' ')
        for word in words_in_sentance:
            if word not in dict_of_words:
                dict_of_words[word]=1
            else:
                dict_of_words[word]+=1
    ranked_words=sorted(dict_of_words.items(), key=lambda item: item[1], reverse=True)
    output=""
    for i in range(number_of_ranks):
        if len(ranked_words)>i:
            output+=f"{i+1}. \"{ranked_words[i][0]}\" - {ranked_words[i][1]}\n"
    return output

if __name__ == "__main__":
    print(word_ranking(sentences))
    #print(word_ranking(["Andrzej"]))
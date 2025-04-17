# odczytywanie pliku  
with open('szarlotka.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    

words = content.split()
word_count = len(words)

print("Liczba słów w pliku: ", word_count)

#zapisanie pierwszych trzech znaków wyrazów do nowego pliku
first_three_chars = [word[:3] for word in words]

with open('nowy_plik.txt', 'w', encoding = 'utf-8') as new_file:
    new_file.write(" ".join(first_three_chars))
    
# tworzenie słownika dla zliczania wystąpień słów w tekście
word_frequency = {}

for word in words:
    word = word.lower().strip(',.():')
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print('\n Występowanie słów: ')
for word, count in word_frequency.items():
    print(f"{word}: {count}")

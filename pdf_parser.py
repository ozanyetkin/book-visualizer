from unicodedata import name
import fitz
import matplotlib.pyplot as plt

book_texts = []

for i in range(1, 25):
    with fitz.open(f"books/{i}.pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    book_texts.append(text.lower())

names = []
with open('names.txt') as f:
    names = f.readlines()
names = [n.replace("\n", "").lower() for n in names]

book_numbers = []
word_counts = []
occurrences = []
for i, text in enumerate(book_texts):
    book_numbers.append(i + 1)
    words = text.split()
    for j, w in enumerate(words):
        for n in names:
            if n in w:
                occurrences.append((i + 1, j))
    word_counts.append(len(words))

print(book_numbers)
print(word_counts)
print(occurrences)

x = book_numbers
y = [-w for w in word_counts]

fig, ax = plt.subplots()

ax.bar(x, y, width=0.2, color="#828282")
ax.set(xlim=(0, 25))

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

for occurrence in occurrences:
    x, y = occurrence
    ax.scatter(x, -y, c="#912a16")

plt.show()
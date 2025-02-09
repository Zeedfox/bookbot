#mi_edad = 29
#mi_nombre = "Antonio"
#print(f"hello {mi_nombre}!!! now you have {mi_edad} years old")
##Print de arriba solo test..
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    count_words(file_contents)

def count_words(book):
    words = book.split()
    print(len(words))



main()
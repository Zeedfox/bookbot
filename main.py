#mi_edad = 29
#mi_nombre = "Antonio"
#print(f"hello {mi_nombre}!!! now you have {mi_edad} years old")
##Print de arriba solo test..
def main():
    file_path = "books/frankenstein.txt"
    book_text = read_file(file_path)
    #print(book_text) #Ejercicio inicial lectura y print consola
    #print(count_words(book_text))#Ejercicio devolver conteo palabras
    print(count_char(book_text))

def read_file(url):
    with open(url) as f: #With es la mejor practica para cerrar conexiones o archivos
        file_contents = f.read() #Cierra de forma automatica With
    return file_contents

def count_words(book):
    words = book.split()
    count = len(words)
    return count

def text_lower(text):
    return text.lower()#convierte todos los caracteres en minusculas

def count_char(text):
    dict_char = {}
    content_lower = text_lower(text)
    list_char = list(content_lower)#se dividen en todos los caracteres
    #print(f"El numero total de caracteres es: {len(list_char)}")
    for c in list_char:
        if c in dict_char: #valida existencia de caracter en diccionario
            dict_char[c] += 1
        else:
            dict_char[c] = 1
    #for done
    return dict_char

main()
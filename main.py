#Global Variables
file_path = "books/frankenstein.txt"

def main():
    book_text = read_file(file_path)
    #print(book_text) #Ejercicio inicial lectura y print consola
    #print(count_words(book_text))#Ejercicio devolver conteo palabras
    #print(count_char(book_text)) #Ejercicio conteno individual por caracters
    #char_report(count_char(book_text)) #Ejercicio de Lista de Diccionarios
    print_report(char_report(count_char(book_text)),count_words(book_text))


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

def sort_on(dict): #Aun no se para que sirve, supongo para una llave "key"
    return dict["num"]

def char_report(dict_of_char):
    list_of_dict = []
    for char in dict_of_char:
        if char.isalpha():#Verificando si pertenece al alfabeto
            list_of_dict.append({"char":char, "num":dict_of_char[char]}) #creando lista de diccionarios
    #ordenando los items de la lista en orden descendente.
    list_of_dict.sort(reverse=True, key=sort_on)
    #print(list_of_dict)
    return list_of_dict

def print_report(list_dict, words):
    print(f"---- Begin report of {file_path} ----")
    print(f"{words} words found in the document\n")
    for x in list_dict:
        print(f"The '{x["char"]}' character was found {x["num"]} times")
    print("\n--- End report ---")
    #



#Excecuting the main function..
main()
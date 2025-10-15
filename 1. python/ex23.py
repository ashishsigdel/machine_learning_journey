import sys
script, input_encoding, error = sys.argv

def main(language_file, encodings, errors):
    line = language_file.readline()

    if line :
        print_line(line, encodings, errors)
        return main(language_file, encodings, errors)

def print_line(line, encodings, errors):
    next_lang = line.strip()

    raw_bytes = next_lang.encode(encodings, errors=errors)
    cooked_string = raw_bytes.decode(encodings, errors=errors)    

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

        
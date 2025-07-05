def tokenizer(code: str):
    current_words = ''
    current_type = ''
    code_lexer = {}

    for letter in code:
        if letter == " ":
            code_lexer[current_words] = current_type
            current_words = ''
        if letter.isspace():
            continue

        if letter.isalpha():
            if current_type != "string":
                if current_words:
                    code_lexer[current_words] = current_type
                current_words = ''
                current_type = "string"
            current_words += letter

        elif letter.isnumeric():
            if current_type != "integer":
                if current_words:
                    code_lexer[current_words] = current_type
                current_words = ''
                current_type = "integer"
            current_words += letter

        elif not letter.isdigit():
            if current_type != "symbol":
                if current_words and (not current_words.isspace()):
                    code_lexer[current_words] = current_type
                current_words = ''
                current_type = "symbol"
            current_words += letter
    if current_words:
        code_lexer[current_words] = current_type
    return code_lexer

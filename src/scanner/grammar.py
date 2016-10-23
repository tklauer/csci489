class Grammar:

# global token/minilang grammar file

    keyword_tokens = {
        'read': ('KWRD', 3),
        'write': ('KWWR', 4),
        'if': ('KWIF', 5),
        'then': ('KWTH', 6),
        'else': ('KWEL', 7),
        'fi': ('KWFI', 8),
        'to': ('KWTO', 9),
        'do': ('KWDO', 10),
        'loop': ('KWSTRL', 29),
        'endloop': ('KWENDL', 11),
        'declare': ('KWDEC', 27),
        'integer': ('KWINT', 28)
    }

    tokens = {
        ';': ('SEMI', 12),
        ',': ('COMMA', 13),
        ':': {
            ':=': ('ASGN', 14)
        },
        '+': ('PLUS', 15),
        '-': ('MINUS', 16),
        '*': ('STAR', 17),
        '/': ('DVD', 18),
        '=': ('EQR', 19),
        '>': {
            '>': ('GTR', 20),
            '>=': ('GER', 23),
        },
        '<': {
            '<': ('LTR', 21),
            '<=': ('LER', 22)
        },
        '#': {
            '#': ('NOTEQUAL', 30)
            '##': ('NER', 24)
        },
        '(': ('LPAR', 25),
        ')': ('RPAR', 26)
    }

    special_tokens = {
        'identifier': ('IDR', 1),
        'constant': ('CONST', 2),
    }

    # deprecated function
    def tokenIterativeDict():

        temp_tokens_dict = Grammar.tokens

        for keyword, tuple_val in Grammar.keyword_tokens.items():

            temp_keyword = ''
            current_location = temp_tokens_dict

            for char in keyword:
                temp_keyword += char
                if temp_keyword in current_location:
                    current_location = current_location[temp_keyword]
                else:
                    current_location[temp_keyword] = {}
                    current_location = current_location[temp_keyword]

            current_location[temp_keyword] = tuple_val

        return temp_tokens_dict

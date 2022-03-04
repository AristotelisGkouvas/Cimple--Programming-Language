import sys
import string

#############################################################################
#	LEXICAL ANALYZER														#
#############################################################################
line = 1

family = ''
lexical = ''
tokenType = ''

def lexicalAnalyzer():

    # counting variables
    global line             #Current line
    global family
    global lexical
    global tokenType

    family = ''
    tokenType = ''
    lexical = ''
    character = 0  #counting number of letter

    token_char = file.read(1)

    # TAB or SPACE or newline
    while token_char == '\t' or token_char == ' ' or token_char == '\r':
        token_char = file.read(1)

    if token_char == '\n':
        line += 1
        return lexicalAnalyzer()

    # Letter
    elif token_char.isalpha():
        lexical = token_char
        token_char = file.read(1)
        character += 1
        while token_char.isalpha() or token_char.isdigit():
            if character > 30:
                print(('Error in line %d: Word lenght surpassed limit of 30.', line))
            lexical = lexical + token_char
            character += 1
            token_char = file.read(1)
            #print('\t( %s )' % (token_char))
        file.seek(file.tell() - 1)
        family = 'Keyword'

        if lexical == 'program':
            tokenType = 'program_token'

        elif lexical == 'declare':
            tokenType = 'declare_token'

        elif lexical == 'if':
            tokenType = 'if_token'

        elif lexical == 'else':
            tokenType = 'else_token'

        elif lexical == 'while':
            tokenType = 'while_token'

        elif lexical == 'switchcase':
            tokenType = 'switchcase_token'

        elif lexical == 'forcase':
            tokenType = 'forcase_token'

        elif lexical == 'incase':
            tokenType = 'incase_token'

        elif lexical == 'case':
            tokenType = 'case_token'

        elif lexical == 'default':
            tokenType = 'default_token'

        elif lexical == 'not':
            tokenType = 'not_token'

        elif lexical == 'and':
            tokenType = 'and_token'

        elif lexical == 'or':
            tokenType = 'or_token'

        elif lexical == 'function':
            tokenType = 'function_token'

        elif lexical == 'procedure':
            tokenType = 'procedure_token'

        elif lexical == 'call':
            tokenType = 'call_token'

        elif lexical == 'return':
            tokenType = 'return_token'

        elif lexical == 'in':
            tokenType = 'in_token'

        elif lexical == 'inout':
            tokenType = 'inout_token'

        elif lexical == 'input':
            tokenType = 'input_token'

        elif lexical == 'print':
            tokenType = 'print_token'
        else:
            tokenType = 'id_token'
            family = 'Identifier'

    # Digit
    elif token_char.isdigit():
        lexical = token_char
        token_char = file.read(1)

        while token_char.isdigit():
            lexical = lexical + token_char
            token_char = file.read(1)
            num = int(lexical)
            if (num < -4294967297 or num > 4294967295):
                print('Error in line %d: Invalid range of number %s ( -2^32+1 > number > 2^32-1).' % (line, lexical))
                sys.exit(0)
        file.seek(file.tell() - 1)
        tokenType = 'INTEGER_token'

        family = 'Number'

    # '+' or '-'
    elif token_char == '+' or token_char == '-':
        lexical = token_char
        if lexical == '+':
            tokenType = 'plus_token'
        elif lexical == '-':
            tokenType = 'minus_token'

        family = 'Add_Operator'

    # '*' or '/'
    elif token_char == '*' or token_char == '/':
        lexical = token_char
        if lexical == '*':
            tokenType = 'multiply_token'
        elif lexical == '/':
            tokenType = 'division_token'

        family = 'Mul_Operator'

    # ':='
    elif token_char == ':':
        lexical = lexical + token_char
        token_char = file.read(1)
        if token_char == '=':
            tokenType = 'assign_token'
            lexical = lexical + token_char
            token_char = file.read(1)
        file.seek(file.tell() - 1)

        family = 'Assignment'

    # ',' or ';'
    elif token_char == ',' or token_char == ';':
        lexical = token_char
        if lexical == ',':
            tokenType = 'comma_token'
        elif lexical == ';':
            tokenType = 'semicolon_token'

        family = 'Delimiter'

    # '=' or '<>' or '<=' or '<' or '>=' or '>'
    elif token_char == '='  or token_char == '<' or token_char == '>':
        lexical = token_char
        if lexical == '=':
            token_char = file.read(1)
            tokenType = 'equals_token'
            lexical = lexical + token_char
        elif lexical == '<':
            token_char = file.read(1)
            if token_char == '>':
                tokenType = 'notequal_token'
                lexical = lexical + token_char

            elif token_char == '=':
                tokenType = 'lessorequals_token'
                lexical = lexical + token_char
            else:
                tokenType = 'less_token'
                file.seek(file.tell() - 1)
        elif lexical == '>':
            token_char = file.read(1)
            if token_char == '=':
                tokenType = 'greaterorequals_token'
                lexical = lexical + token_char
            else:
                tokenType = 'greater_token'
                file.seek(file.tell() - 1)

        family = 'Rel_Operator'
    # '(' or ')' or '{' or '}' or '[' or ']'
    elif token_char == '(' or token_char == ')' or token_char == '{' or token_char == '}' or token_char == '[' or token_char == ']':
        lexical = token_char
        if lexical == '(':
            tokenType = 'leftbracket_token'

        elif lexical == ')':
            tokenType = 'rightbracket_token'

        elif lexical == '{':
            tokenType = 'begin_token'

        elif lexical == '}':
            tokenType = 'end_token'

        elif lexical == ']':
            tokenType = 'rightsquarebracket_token'

        elif lexical == '[':
            tokenType = 'leftsquarebracket_token'

        family = 'Group_Symbol'

    # End program
    elif token_char == '.':
        lexical = token_char
        tokenType = 'endprogram_token'

        family = 'Delimiter'

    # Comments
    elif token_char == '#':
        lexical = token_char
        token_char = file.read(1)
        flag = False
        while token_char != '':
            token_char = file.read(1)
            if token_char == '#':
                flag= True
                break
        if flag == True:
            lexicalAnalyzer()
        else:
            print('Error in line %d: "#" is missing. The comment was supposed to be closed.' % (line))
            sys.exit(0)

    elif token_char == '':
        lexical = ''
        tokenType = 'eof_token'

    else:
        print('Error in line %d : character is not recognised as a language character/symbol ' % (line))
        sys.exit(0)

    ### If it finds a comment, it prints the next lexical twice ###
    print('Line: %d \t%s\t\t\tfamily: %s ' % (line,lexical,family))

    return tokenType


#############################################################################
#	SYNTAX ANALYZER 						                                #
#############################################################################

def syntaxAnalyzer():

    global tokenType
    global lexical

    def program():
        # program ID block .

        # "program" is the starting symbol
        # followed by its name and a block
        # every program ends with a fullstop
        global tokenType
        global lexical

        tokenType = lexicalAnalyzer()

        if tokenType == 'program_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                programName = lexical
                tokenType = lexicalAnalyzer()
                block()
                if tokenType == 'endprogram_token':
                    tokenType = lexicalAnalyzer()
                    if tokenType == 'eof_token':
                        print("\nCompilation successfully completed without errors.\n")
                        return
                    else:
                        print('Error in line %d: No characters are allowed after the fullstop indicating the end of the program.' % (line))
                        sys.exit(0)
                else:
                    print('Error in line %d: A fullstop expected, the program should end with a fullstop.' % (line))
                    sys.exit(0)
            else:
                print('Error in line %d: The program name expected after the keyword "program" but found "%s" .' % (line, lexical))
                sys.exit(0)
        else:
            print('Error in line %d: The program must start with the keyword "program" but instead it starts with the word "%s".' % (line, lexical))
            sys.exit(0)


    def block():
        # { declarations subprograms statements }

        # a block consists of declarations, subprograms and statements
        global tokenType

        if tokenType == 'begin_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'declare_token':
                declarations()
            subprograms()
            blockStatements()
            if tokenType == 'end_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The "}" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "{" was expected .' % line)
            sys.exit(0)
        return


    def declarations():
        # ( declare varlist ; ) *

        # declaration of variables
        # kleene star implies zero or more "declare" statements
        global tokenType

        while tokenType == 'declare_token':
            tokenType = lexicalAnalyzer()
            varlist()
            if tokenType == 'semicolon_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The keyword ";" was expected\n' % line)
                sys.exit(0)
        return


    def varlist():
        # ID ( , ID ) *
        # | e

        # a list of variables following the declaration keyword
        global tokenType

        if tokenType == "id_token":
            tokenType = lexicalAnalyzer()
            while tokenType == 'comma_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'id_token':
                    tokenType = lexicalAnalyzer()
                else:
                    print('Error in line %d: A variable is expected after comma (,). ' % line)
                    sys.exit(0)
        return


    def subprograms():
        # ( subprogram ) *

        # zero or more subprograms
        global tokenType

        while tokenType == 'procedure_token' or tokenType == 'function_token':
            subprogram()
        return


    def subprogram():
        # a subprogram is a function or a procedure
        # followed by parameters and block
        global tokenType
        global lexical

        # function ID ( formalparlist ) block
        if tokenType == 'function_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                if tokenType == "leftbracket_token":
                    tokenType = lexicalAnalyzer()
                    formalparlist()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        block()
                    else:
                        print('Error in line %d: The ")" was expected .' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: A variable is expected after the keyword "function".' % line)
                sys.exit(0)

        # procedure ID ( formalparlist ) block
        elif tokenType == 'procedure_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                name = lexical
                tokenType = lexicalAnalyzer()
                if tokenType == "leftbracket_token":
                    tokenType = lexicalAnalyzer()
                    formalparlist()
                    if tokenType == 'rightbracket_token':
                        block()
                    else:
                        print('Error in line %d: The ")" was expected .' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: A variable is expected after the keyword "procedure".' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The keyword "function" or "procedure" was expected.' % line)
            sys.exit(0)
        return


    def formalparlist():
        # formalparitem ( , formalparitem ) *

        # list of formal parameters
        # one or more parameters are allowed
        global tokenType

        formalparitem()
        while tokenType == 'comma_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'in_token' or tokenType == 'inout_token':
                formalparitem()
            else:
                print('Error in line %d: Expected "in" or "inout" after the comma.' %  line)
                sys.exit()
        return


    def formalparitem():
        # a formal parameters
        # "in": by value, "inout": by reference
        global tokenType

        # in ID
        if tokenType == 'in_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: A variable is expected after the keyword "in".' % line)
                sys.exit(0)

        # inout ID
        elif tokenType == 'inout_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: A variable is expected after the keyword "inout".' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The keyword "in" or "inout" was expected.' % line)
            sys.exit(0)
        return


    def statements():
        # statement  ;
        # | { statement ( ; statement ) * }

        # one or more statements
        # more than one statements should be grouped with brackets
        global tokenType

        if tokenType == 'begin_token':
            tokenType = lexicalAnalyzer()
            blockStatements()
            if tokenType == 'end_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: The "}" was expected .' % line)
                sys.exit(0)
        else:
            statement()
            if tokenType == 'semicolon_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: The keyword ";" was expected\n' % line)
                sys.exit(0)
        return


    def blockStatements():
        # statement ( ; statement ) *

        # statements cosidered as block (used in program and subprogram)

        global tokenType

        statement()
        while tokenType == 'semicolon_token':
            tokenType = lexicalAnalyzer()
            statement()
        return


    def statement():
        # one statement

        global tokenType

        # assignStat
        if tokenType == 'id_token':
            assignStat()
        # ifStat
        elif tokenType == 'if_token':
            ifStat()
        # whileStat
        elif tokenType == 'while_token':
            whileStat()
        # switchcaseStat
        elif tokenType == 'switchcase_token':
            switchcaseStat()
        # forcaseStat
        elif tokenType == 'forcase_token':
            forcaseStat()
        # incaseStat
        elif tokenType == 'incase_token':
            incaseStat()
        # callStat
        elif tokenType == 'call_token':
            callStat()
        # returnStat
        elif tokenType == 'return_token':
            returnStat()
        # inputStat
        elif tokenType == 'input_token':
            inputStat()
        # printStat
        elif tokenType == 'print_token':
            printStat()
        return


    def assignStat():
        # ID := expression

        # assignment statement
        global tokenType
        global lexical

        if tokenType == 'id_token':
            id = lexical
            tokenType = lexicalAnalyzer()
            if tokenType == 'assign_token':
                tokenType = lexicalAnalyzer()
                expression()
            else:
                print('Error in line %d: The assignment symbol ":=" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "id" was expected.' % line)
            sys.exit(0)
        return


    def ifStat():
        # if ( condition ) statements
        # elsepart

        # if statement
        global tokenType

        if tokenType == 'if_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                condition()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    statements()
                    elsePart()
                else:
                    print('Error in line %d: The ")" was expected .' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected .' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "if" was expected.' % line)
            sys.exit(0)
        return


    def elsePart():
        # else statements
        # | e

        # else part is optional
        global tokenType

        if tokenType == 'else_token':
            tokenType = lexicalAnalyzer()
            statements()
        return


    def whileStat():
        # while ( condition ) statements

        # while statement
        global tokenType

        if tokenType == 'while_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                condition()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                    statements()

                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "while" was expected.' % line)
            sys.exit(0)
        return


    def switchcaseStat():
        # switchcase
        #   ( case ( condition ) statements ) *
        #   default statements

        # switch statement
        global tokenType

        if tokenType == 'switchcase_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        statements()
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "switchcase" was expected.' % line)
            sys.exit(0)
        return


    def forcaseStat():
        # forcase
        #   ( case ( condition ) statements ) *
        #   default statements

        # forcase statement
        global tokenType

        if tokenType == 'forcase_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        statements()
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "forcase" was expected.' % line)
            sys.exit(0)
        return


    def incaseStat():
        # incase
        #   ( case ( condition ) statements )*

        # incase statement
        global tokenType

        if tokenType == 'incase_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'case_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    condition()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        statements()
                        while tokenType == 'default_token':
                            tokenType = lexicalAnalyzer()
                            statements()
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "case" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "incase" was expected.' % line)
            sys.exit(0)
        return


    def returnStat():
        # return ( expression )

        # return statement
        global tokenType

        if tokenType == 'return_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                expression()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "return" was expected.' % line)
            sys.exit(0)
        return


    def callStat():
        # call ID ( actualparlist )

        # call statement
        global tokenType
        global lexical

        if tokenType == 'call_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'leftbracket_token':
                    tokenType = lexicalAnalyzer()
                    actualparlist()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        return
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "(" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "id" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "call" was expected.' % line)
            sys.exit(0)


    def printStat():
        # print ( expression )

        # print statement
        global tokenType

        if tokenType == 'print_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                expression()
                if tokenType == 'rightbracket_token':
                    tokenType = lexicalAnalyzer()
                else:
                    print('Error in line %d: The ")" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "print" was expected.' % line)
            sys.exit(0)
        return


    def inputStat():
        # input ( ID )

        # input statement
        global tokenType
        global lexical

        if tokenType == 'input_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftbracket_token':
                tokenType = lexicalAnalyzer()
                if tokenType == 'id_token':
                    tokenType = lexicalAnalyzer()
                    if tokenType == 'rightbracket_token':
                        tokenType = lexicalAnalyzer()
                        return
                    else:
                        print('Error in line %d: The ")" was expected.' % line)
                        sys.exit(0)
                else:
                    print('Error in line %d: The "id" was expected.' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The "(" was expected.' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The "input" was expected.' % line)
            sys.exit(0)


    def actualparlist():
        # actualparitem ( , actualparitem ) *
        # | e

        # list of actual parameters
        global tokenType

        actualparitem()
        while tokenType == 'comma_token':
            tokenType = lexicalAnalyzer()
            actualparitem()
        return


    def actualparitem():
        #   in expression
        # | inout ID

        # an actual parameter
        # "in": value, "inout": reference
        global tokenType

        if tokenType == 'in_token':
            tokenType = lexicalAnalyzer()
            expression()
        elif tokenType == 'inout_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'id_token':
                tokenType = lexicalAnalyzer()
            else:
                print('Error in line %d: A parameter was expected after the keyword "inout".\n' % line)
                sys.exit(0)
        else:
            print('Error in line %d: The keyword "in" or "inout" was expected \n' % line)
            sys.exit(0)
        return


    def condition():
        # boolterm ( or boolterm ) *

        # boolean expression
        global tokenType

        boolTerm()
        while tokenType == 'or_token':
            tokenType = lexicalAnalyzer()
            boolTerm()
        return


    def boolTerm():
        # boolfactor ( and boolfactor )*

        # term in boolean expression
        global tokenType

        boolfactor()
        while tokenType == 'and_token':
            tokenType = lexicalAnalyzer()
            boolfactor()
        return


    def boolfactor():
        # factor in boolean expression

        global tokenType
        # not [ condition ]
        if tokenType == 'not_token':
            tokenType = lexicalAnalyzer()
            if tokenType == 'leftsquarebracket_token':
                tokenType = lexicalAnalyzer()
                condition()
                if tokenType == 'rightsquarebracket_token':
                    tokenType = lexicalAnalyzer()
                    return
                else:
                    print('Error in line %d: The right square bracket symbol "]" was expected here.\n' % line)
                    sys.exit(0)
            else:
                print('Error in line %d: The left square bracket symbol "[" was expected here.\n' % line)
                sys.exit(0)

        # [ condition ]
        elif tokenType == 'leftsquarebracket_token':
            tokenType = lexicalAnalyzer()
            condition()
            if tokenType == 'rightsquarebracket_token':
                tokenType = lexicalAnalyzer()
                return
            else:
                print('Error in line %d: The right square bracket symbol "]" was expected here.\n' % line)
                sys.exit(0)

        # expression REL_OP expression
        else:
            expression()
            REL_OP()
            expression()
            return


    def expression():
        # optionalSign term ( ADD_OP term ) *

        # arithmetic expression
        global tokenType

        optionalSign()
        term()
        while tokenType == 'plus_token' or tokenType == 'minus_token':
            ADD_OP()
            term()
        return


    def term():
        # factor ( MUL_OP factor ) *

        # term in arithmetic expression
        global tokenType

        factor()
        while tokenType == 'multiply_token' or tokenType == 'division_token':
            MUL_OP()
            factor()
        return


    def factor():
        # factor in arithmetic expression
        global tokenType

        #   INTEGER
        if tokenType == 'INTEGER_token':
            fact = lexical
            tokenType = lexicalAnalyzer()
            return fact

        # | ( expression )
        elif tokenType == 'leftbracket_token':
            tokenType = lexicalAnalyzer()
            e = expression()
            if tokenType == 'rightbracket_token':
                fact = e
                tokenType = lexicalAnalyzer()
                return fact
            else:
                print('Error in line %d: The right bracket symbol ")" was expected here\n' % line)
                sys.exit(0)
        # | ID idTail
        elif tokenType == 'id_token':
            fact = lexical
            tokenType = lexicalAnalyzer()
            idTail()
            return fact
        else:
            print('Error in line %d: A integer, an expression , a procedure call or a function call was expected here.\n' % line)
            sys.exit(0)


    def idTail():
        # ( actualparlist )
        # | e

        # follows a function or procedure
        # describes parethneses and parameters
        global tokenType

        if tokenType == 'leftbracket_token':
            tokenType = lexicalAnalyzer()
            actualparlist()
            if tokenType == 'rightbracket_token':
                tokenType = lexicalAnalyzer()
                return
        return

    def optionalSign():
        # ADD_OP
        # | e

        # symbols "+" and "-" (are optional)
        global tokenType
        if tokenType == 'plus_token' or tokenType == 'minus_token':
            opSign = ADD_OP()
            tokenType = lexicalAnalyzer()
            return opSign
        return

    ########################################
    # lexer rules: relational, arithentic operations, integer values and ids
    ########################################

    def REL_OP():
        # = | <= | >= | > | < | <>
        global tokenType
        global lexical

        if (tokenType == 'equals_token' or tokenType == 'lessorequals_token' or tokenType == 'greaterorequals_token'
                or tokenType == 'less_token' or tokenType == 'greater_token' or tokenType == 'notequals_token'):
            relOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A comparison sign was expected here.' % line)
            sys.exit(0)
        return relOp


    def ADD_OP():
        # + | -
        global tokenType
        global lexical

        if tokenType == 'plus_token' or tokenType == 'minus_token':
            addOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A plus sign(+) or a minus sign(-) was expected here.' % (line))
            sys.exit(0)
        return addOp


    def MUL_OP():
        # * | /
        global tokenType
        global lexical

        if tokenType == 'multiply_token' or tokenType == 'division_token':
            mulOp = lexical
            tokenType = lexicalAnalyzer()
        else:
            print('Error in line %d: A multiplication sign(*) or a division sign(/) was expected here.' % (line))
            sys.exit(0)
        return mulOp
    program()


# Opening file, as arguement in command line:
file = open(sys.argv[1], 'r')
print("\n")
syntaxAnalyzer()

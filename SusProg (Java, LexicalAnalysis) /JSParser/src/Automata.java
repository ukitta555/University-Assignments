import java.util.Scanner;

public class Automata {
    public AutomataState currentState;
    private int nextCharToProcessIndex;

    public Automata() {
        this.currentState = AutomataState.IDENTIFIER_NAME_EXTRACTION;
        this.nextCharToProcessIndex = 0;
        System.out.println("Automata initialized");
    }

    public String getNextLexeme(String line) {
        // don't reset in case we hit a multi - line comment


        while (this.nextCharToProcessIndex < line.length()) {
            char currentChar = this.readChar(line, this.nextCharToProcessIndex);
            if (this.currentState != AutomataState.COMMENT_EXTRACTION) {
                this.currentState = AutomataState.IDENTIFIER_NAME_EXTRACTION;
            }

             if (currentChar == '/' || this.currentState == AutomataState.COMMENT_EXTRACTION) {
                if (this.nextCharToProcessIndex + 1 < line.length()) {
                    char nextChar = this.readChar(line, this.nextCharToProcessIndex + 1);
                    if (nextChar == '*' || this.currentState == AutomataState.COMMENT_EXTRACTION) {
                        if (!(this.currentState == AutomataState.COMMENT_EXTRACTION)) {
                            this.nextCharToProcessIndex += 2;
                        }
                        this.currentState = AutomataState.COMMENT_EXTRACTION;
                        String comment = this.getComment(line, this.nextCharToProcessIndex);
                        this.nextCharToProcessIndex += 2;
                        return comment;
                    }
                } else {
                    return Character.toString(currentChar);
                }
            } else if (this.isIdentifierSymbol(currentChar)) {
                String identifier = this.getIdentifierName(line, this.nextCharToProcessIndex);
                if (this.isIdentifierReserved(identifier)) {
                    this.currentState = AutomataState.IDENTIFIER_IS_RESERVED;
                }
                return identifier;
            }
            else if (this.isNumeric(currentChar)) {
                this.currentState = AutomataState.NUMBER_EXTRACTION;
                try {
                    String number = this.getNumber(line, this.nextCharToProcessIndex);
                    return number;
                } catch (Exception e) {
                    this.log(e.getMessage());
                }
            } else if (this.isSingleQuote(currentChar)) {
                this.currentState = AutomataState.STRING_EXTRACTION;
                String str = this.getStringLiteral(line, this.nextCharToProcessIndex, QuoteModeEnum.SINGLE_QUOTE_MODE);
                if (str.equals("Bad string literal!")) {
                    this.currentState = AutomataState.ERROR_STATE;
                }
                return str;
            } else if (this.isDoubleQuote(currentChar)) {
                this.currentState = AutomataState.STRING_EXTRACTION;
                String str = this.getStringLiteral(line, this.nextCharToProcessIndex, QuoteModeEnum.DOUBLE_QUOTE_MODE);
                 if (str.equals("Bad string literal!")) {
                     this.currentState = AutomataState.ERROR_STATE;
                 }
                return str;
            } else if (this.isPunctuationSymbol(currentChar)) {
                this.currentState = AutomataState.PUNCTUATION_EXTRACTION;
                this.nextCharToProcessIndex++;
                return Character.toString(currentChar);
            }  else if (this.isOperatorSymbol(currentChar)) {
                this.currentState = AutomataState.OPERATOR_EXTRACTION;
                String operator = this.getOperator(line, this.nextCharToProcessIndex);
                return operator;
            } else if (currentChar == ' ') {
                this.nextCharToProcessIndex++;
             } else {
                this.currentState = AutomataState.ERROR_STATE;
                this.nextCharToProcessIndex++;
                return Character.toString(currentChar);
             }
        }

        this.nextCharToProcessIndex = 0;
        return null;
    }

    private String getComment(String line, int startingIndex) {
        int currentIndex = startingIndex;
        char currentChar;
        char nextChar;
        if (startingIndex < line.length()) {
            currentChar = this.readChar(line, startingIndex);
        } else {
            this.nextCharToProcessIndex = line.length();
            return line;
        }

        if (startingIndex + 1 < line.length()) {
            nextChar = this.readChar(line, startingIndex + 1);
        } else {
            this.nextCharToProcessIndex = line.length();
            return line;
        }

        while (currentIndex + 2 < line.length() && currentChar != '*' && nextChar != '/') {
            currentIndex++;
            currentChar = this.readChar(line, currentIndex);
            nextChar = this.readChar(line, currentIndex + 1);
        }

        if (currentIndex + 2 >= line.length()) {
            this.nextCharToProcessIndex = line.length();
            return line.substring(startingIndex);
        }
        this.nextCharToProcessIndex = currentIndex;
        return line.substring(startingIndex, currentIndex + 2);
    }

    // + - * / % = ! { } ( )
    // ++ -- && || ==  <= >= !=
    // !==   ===
    private String getOperator(String line, int startingIndex) {
        int currentIndex = startingIndex;
        char currentChar = this.readChar(line, currentIndex);
        if (currentIndex + 1 < line.length()) {
            char nextChar = this.readChar(line, currentIndex + 1);
            if (currentIndex + 2 < line.length()) {
                char nextNextChar = this.readChar(line, currentIndex + 2);
                if (nextChar == '=' && nextNextChar == '=') {
                    if (currentChar == '=')  {
                        this.nextCharToProcessIndex += 3;
                        return "===";
                    }
                    else if (currentChar == '!') {
                        this.nextCharToProcessIndex += 3;
                        return "!==";
                    }
                }
            }
            if (currentChar == '+') {
                if (nextChar == '+') {
                    this.nextCharToProcessIndex += 2;
                    return "++";
                }  else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "+";
                }
            }
            if (currentChar == '-') {
                if (nextChar == '-') {
                    this.nextCharToProcessIndex += 2;
                    return "--";
                }
                else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "-";
                }
            }
            if (currentChar == '&') {
                if (nextChar == '&') {
                    this.nextCharToProcessIndex += 2;
                    return "&&";
                }
                else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "&";
                }
            }
            if (currentChar == '|') {
                if (nextChar == '|') {
                    this.nextCharToProcessIndex += 2;
                    return "||";
                }
                else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "|";
                }
            }
            if (currentChar == '<') {
                if (nextChar == '=') {
                    this.nextCharToProcessIndex += 2;
                    return "<=";
                }
                else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "<";
                }
            }
            if (currentChar == '>') {
                if (nextChar == '=') {
                    this.nextCharToProcessIndex += 2;
                    return ">=";
                } else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return ">";
                }
            }
            if (currentChar == '=') {
                if (nextChar == '=') {
                    this.nextCharToProcessIndex += 2;
                    return "==";
                }
                else if (nextChar == ' ') {
                    this.nextCharToProcessIndex += 2;
                    return "=";
                }
            }
            if (currentChar == '!') {
                if (nextChar == '=') {
                    this.nextCharToProcessIndex += 2;
                    return "!=";
                } else if (this.isIdentifierSymbol(nextChar)) {
                    this.nextCharToProcessIndex += 1;
                    return "!";
                }
            }
        }

        if (this.isSingleSymbolOperator(currentChar)) {
            this.nextCharToProcessIndex += 1;
            return Character.toString(currentChar);
        }

        return null;
    }

    private boolean isPunctuationSymbol(char c) {
        return c == ',' || c == ';' || c == '.';
    }

    private char quoteToCompare(QuoteModeEnum mode) {
        return mode == QuoteModeEnum.DOUBLE_QUOTE_MODE
                ? '\"'
                : '\'';
    }

    private String getStringLiteral(String line, int startingIndex, QuoteModeEnum mode) {
        int currentIndex = startingIndex + 1;
        char currentChar = this.readChar(line, currentIndex);
        while (currentIndex + 1 < line.length()
                && currentChar != this.quoteToCompare(mode)) {
            currentIndex++;
            currentChar = this.readChar(line,currentIndex);
        }

        this.nextCharToProcessIndex = currentIndex + 1;

        if (currentIndex + 1 >= line.length()) {
            return "Bad string literal!";
        }

        // quote wasn't included, so we add it here
        return line.substring(startingIndex, currentIndex + 1);
    }

    private boolean isDoubleQuote(char c) {
        return c == '\"';
    }

    private boolean isSingleQuote(char c) {
        return c == '\'';
    }

    private boolean isIdentifierReserved(String identifier) {
        return identifier.equals("const")
                || identifier.equals("let")
                || identifier.equals("var")
                || identifier.equals("function")
                || identifier.equals("for")
                || identifier.equals("while")
                || identifier.equals("do");
     }


     private String getNumber(String line, int startingIndex) throws Exception {
         int currentIndex = startingIndex;
         char currentChar = this.readChar(line, startingIndex);

         this.currentState = AutomataState.NUMBER_IS_DECIMAL;

         if (startingIndex + 2 < line.length()) {
             char nextChar = this.readChar(line, startingIndex + 1);
             // Hex
             if (currentChar == '0' && (nextChar == 'X' || nextChar == 'x')) {
                 this.currentState = AutomataState.NUMBER_IS_HEX;
                 currentIndex = startingIndex + 2;
                 currentChar = this.readChar(line, currentIndex);

                 while (currentIndex + 1 < line.length() && this.isHexSymbol(currentChar)) {
                     currentIndex++;
                     currentChar = this.readChar(line, currentIndex);
                 }
             }
         }

         if (!(this.currentState == AutomataState.NUMBER_IS_HEX)) {
             while (currentIndex + 1 < line.length() && (currentChar == '.' || this.isNumeric(currentChar))) {
                 if (currentChar == '.' && this.currentState != AutomataState.NUMBER_IS_FLOAT) {
                     this.currentState = AutomataState.NUMBER_IS_FLOAT;
                 }
                 currentIndex++;
                 currentChar = this.readChar(line, currentIndex);
             }
         }

         this.nextCharToProcessIndex = currentIndex;

         return line.substring(startingIndex, currentIndex);
     }

    private String getIdentifierName(String line, int startingIndex) {
        int currentIndex = startingIndex;
        char currentChar = this.readChar(line, startingIndex);
        while (currentIndex + 1 < line.length() && this.isIdentifierSymbol(currentChar)) {
            currentIndex++;
            currentChar = this.readChar(line, currentIndex);
        }
        this.nextCharToProcessIndex = currentIndex;

        return line.substring(startingIndex, currentIndex);
    }

    private boolean isIdentifierSymbol(char c) {
        return c == '$' || c == '_' || this.isEnglishLetter(c);
    }

    private boolean isHexSymbol(char c) {
        return this.isNumeric(c) || (c >= 'A' && c <= 'F');
    }

    private boolean isEnglishLetter(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }

    private boolean isNumeric(char c) {
        return c >= '0' && c <= '9';
    }

    private boolean isOperatorSymbol(char c) {
        return c == '+'
                || c == '-'
                || c == '*'
                || c == '/'
                || c == '%'
                || c == '!'
                || c == '&'
                || c == '|'
                || c == '<'
                || c == '>'
                || c == '='
                || c == '('
                || c == ')'
                || c == '{'
                || c == '}';
    }

    private boolean isSingleSymbolOperator(char c) {
        return c == '+'
                || c == '-'
                || c == '*'
                || c == '/'
                || c == '%'
                || c == '!'
                || c == '='
                || c == '('
                || c == ')'
                || c == '{'
                || c == '}';
    }

    private char readChar(String line, int position) {
        return line.charAt(position);
    }

    private void log(String s) {
        System.out.println(s);
    }
}

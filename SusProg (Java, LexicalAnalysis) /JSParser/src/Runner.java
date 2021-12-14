import java.io.File;
import java.util.Scanner;

public class Runner {
    private final File file;
    private Scanner sc;
    private final Automata automata;


    public Runner() {
        this.file = new File("examplefile.js");

        try {
            this.sc = new Scanner(file);
        }  catch (Exception e) {
            System.out.println(e.getMessage());
        }

        this.automata = new Automata();
    }


    public void run(){
        String currentLine;
        while ((currentLine = this.readLineFromFile()) != null) {
            String currentLexeme;
            while ((currentLexeme = this.automata.getNextLexeme(currentLine)) != null) {
                if (this.automata.currentState != AutomataState.COMMENT_EXTRACTION) {
                    this.log("___________");
                    this.log(currentLexeme);
                }



                switch (this.automata.currentState) {
                    case IDENTIFIER_NAME_EXTRACTION:
                        this.log("Is identifier!");
                        break;

                    case IDENTIFIER_IS_RESERVED:
                        this.log("Is reserved!");
                        break;

                    case NUMBER_EXTRACTION:
                        case NUMBER_IS_DECIMAL:
                            this.log("Is decimal!");
                            break;
                        case NUMBER_IS_HEX:
                            this.log("Is hex!");
                            break;
                        case NUMBER_IS_FLOAT:
                            this.log("Is float!");
                            break;
                    case PUNCTUATION_EXTRACTION:
                        this.log("Is a punctuation symbol!");
                        break;
                    case STRING_EXTRACTION:
                        this.log("Is a string!");
                        break;
                    case OPERATOR_EXTRACTION:
                        this.log("Is an operator!");
                        break;
                    case COMMENT_EXTRACTION:

                        /*this.log("Is a comment!");*/
                        if (currentLexeme.charAt(currentLexeme.length() - 1) == '/' && currentLexeme.charAt(currentLexeme.length() - 2) == '*') {
                            this.automata.currentState = AutomataState.IDENTIFIER_NAME_EXTRACTION;
                        }
                        break;
                    case ERROR_STATE:
                        this.log("Bad lexeme");
                    default:
                        this.log("404 Not found");
                        break;
                }
            }
        }
    }

    public String readLineFromFile() {
        if (sc.hasNextLine()) {
            return sc.nextLine();
        }
        return null;
    }

    private void log(String s) {
        System.out.println(s);
    }
}

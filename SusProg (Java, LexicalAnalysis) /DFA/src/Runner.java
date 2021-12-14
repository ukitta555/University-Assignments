import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Runner {
    private int[][] dfa;
    private boolean[] isStateFinal;
    private int stateCount;
    private HashSet<String> acceptedWords;

    public Runner() {
        this.acceptedWords = new HashSet<String>();
        this.constructDFA();
        this.debug();
        this.getAllAcceptedWords(new StringBuilder(""), 0);
        for (String word : acceptedWords) {
            System.out.println(word);
        }
    }

    private boolean wordHasCycles(StringBuilder wordToTest) {
        for (int i = 2; i <= wordToTest.length() / 2; i++) {
            String lastSymbols = wordToTest.substring(wordToTest.length() - i);
            String possiblePeriod = wordToTest.substring(wordToTest.length() - (i * 2), wordToTest.length() - i);
            if (lastSymbols.equals(possiblePeriod)) {
                return true;
            }
        }
        return false;
    }

    private void getAllAcceptedWords(StringBuilder wordToTest, int currentState) {

        if (wordHasCycles(wordToTest) || wordToTest.length() > 50) {
            return ;
        }

        if (isStateFinal[currentState]) {
            if (wordToTest.length() == 0) {
                acceptedWords.add("Empty word");
            } else {
                acceptedWords.add(wordToTest.toString());
            }
        }

        for (int currentChar = 'a'; currentChar < 'z'; currentChar++) {
            wordToTest.append((char)currentChar);
            int newState = dfa[currentChar - 97][currentState];
            if (newState != -1)  {
                getAllAcceptedWords(wordToTest, newState);
            }
            wordToTest.deleteCharAt(wordToTest.length() - 1);
        }
    }

    private void debug() { ;
        for (int i = 0; i < 26; i++) {
            System.out.print((char) (i + 97) + " ");
            for (int j = 0; j < stateCount; j++) {
                System.out.print(dfa[i][j] +  " ");
            }
            System.out.println();
        }

        System.out.println("-------------");

        for (int j = 0; j < stateCount; j++) {
            System.out.print(isStateFinal[j] +  " ");
        }
        System.out.println();
        System.out.println("-------------");
    }

    private boolean doesAcceptWord(String word) {
        int currentState = 0;
        int charIndex = 0;
        while (charIndex < word.length()) {
           currentState = dfa[word.charAt(0) - 97][currentState];
           if (currentState == -1) return false;
           charIndex++;
        }

        if (isStateFinal[currentState]) {
            return true;
        } else return false;
    }

    private void constructDFA() {
        File file = new File("automata.txt");
        try {
            Scanner sc = new Scanner(file);
            stateCount = sc.nextInt();
            dfa = new int[26][stateCount]; // 26 letters in eng. alphabet
            isStateFinal = new boolean[stateCount];
            Arrays.fill(isStateFinal, false);
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < stateCount; j++) {
                    dfa[i][j] = -1;
                }
            }

            while (sc.hasNextLine()) {
                String transitionInfo = sc.nextLine();
                String[] tokens = transitionInfo.split(" ");
                String operation = tokens[0];

                if (operation.equals("transition")) {
                    char character = tokens[1].charAt(0);
                    int stateFrom = Integer.valueOf(tokens[2]);
                    int stateTo = Integer.valueOf(tokens[3]);
                    dfa[character - 97][stateFrom] = stateTo;
                }

                if (operation.equals("final")) {
                    int state = Integer.valueOf(tokens[1]);
                    isStateFinal[state] = true;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}

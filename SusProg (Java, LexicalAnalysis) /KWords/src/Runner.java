import java.io.File;
import java.io.FileNotFoundException;
import java.net.InetSocketAddress;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Runner {
    private int[][] dfa;
    private boolean[] isStateFinal;
    private int stateCount;


    public Runner(String filename) {
        this.constructDFA(filename);
        this.debug();
        this.log(Boolean.toString(this.KWords(3)));
    }

    private boolean KWords(int k) {
        HashSet<Integer> statesToCheck = new HashSet<>();
        statesToCheck.add(new Integer(0));
        for (int i = 0; i < k; i++) {
            this.log("PATH LENGTH: " + (i+1));
            HashSet<Integer> nextSetToCheck = new HashSet<>();
            for (Integer state : statesToCheck) {
                for (int j = 0; j < 26; j++) {
                    int nextState = dfa[j][state];

                    if (nextState == -1) return false;

                    if (!nextSetToCheck.contains(nextState)) {
                        this.log("Added " + nextState + " to check");
                    }
                    nextSetToCheck.add(nextState);
                }
            }
            this.log("--------------------");
            statesToCheck = nextSetToCheck;
        }
        for (Integer state : statesToCheck) {
            if (!isStateFinal[state]) {
                return false;
            }
        }
        return true;
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



    private void constructDFA(String filename) {
        File file = new File(filename);
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

    private void log(String s) {
        System.out.println(s);
    }
}

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Runner {
    private HashMap<String, Boolean> visited = new HashMap<>();
    private HashMap<String, ArrayList<String>> adjacencyLists = new HashMap<>();
    private String currentLine;
    private String definedNonTerminal;
    private String startingNonTerm;

    public void run() {
        File f = new File("grammar_plov.txt");
        try {
            Scanner sc = new Scanner(f);
            boolean isStartingNonTerm = true;

            while (sc.hasNextLine()) {
                this.currentLine = sc.nextLine();
                this.currentLine = this.currentLine.replace("\uFEFF", "");

                if (this.currentLine.length() == 0) continue;

                if (this.isNonTerminalDeclaration()) {
                    this.definedNonTerminal = this.getDefinedNonterminal();
                    this.visited.put(definedNonTerminal, Boolean.FALSE);
                    if (isStartingNonTerm) {
                        this.startingNonTerm = this.definedNonTerminal;
                        isStartingNonTerm = false;
                    }
                }
                ArrayList<String> nonTerminalsFromDefinition = this.getNonterminalsFromDefinition();
                if (this.adjacencyLists.get(definedNonTerminal) != null) {
                    this.adjacencyLists.get(definedNonTerminal).addAll(nonTerminalsFromDefinition);
                } else {
                    this.adjacencyLists.put(definedNonTerminal, nonTerminalsFromDefinition);
                }


                this.log("Defined nonterminal:" + this.definedNonTerminal);
                for (String s:nonTerminalsFromDefinition) {
                    this.log("Related nonterminals:" + s);
                }
            }
            this.dfs(this.startingNonTerm);

            this.log("-----------------------------");
            this.log("-----------------------------");
            this.log("-----------------------------");
            this.log("Unreachable nonterminals ahead:");

            int counter = 0;
            for (Map.Entry<String, Boolean> entry : this.visited.entrySet()) {
                if (!entry.getValue()) {
                    this.log(entry.getKey());
                    counter += 1;
                }
            }


            this.log("Count: " + Integer.toString(counter));
        } catch (FileNotFoundException e) {
            this.log(e.getMessage());
        }


    }

    private ArrayList<String> getNonterminalsFromDefinition() {
        String regex = "(?<!\\\\)#.+?#(?!\\\\)";
        Pattern pattern =  Pattern.compile(regex);

        Matcher matcher = pattern.matcher(this.currentLine);
        ArrayList<String> nonTerms = new ArrayList<>();
        while (matcher.find()) {
            nonTerms.add(matcher.group());
            this.visited.put(matcher.group(), Boolean.FALSE);
        }

        return nonTerms;
    }


    private boolean isNonTerminalDeclaration() {
        return this.currentLine.charAt(0) == '#';
    }

    private String getDefinedNonterminal() {
        String regex = "(?<!\\\\)#(.+?)#(?!\\\\)";
        Pattern pattern =  Pattern.compile(regex);

        Matcher matcher = pattern.matcher(this.currentLine);
        matcher.find();
        String result = matcher.group(0);
        this.currentLine = this.currentLine.substring(result.length());
        return result;
    }

    private void dfs(String currentNonTerminal) {
        ArrayList<String> adjacentNonTerms = this.adjacencyLists.get(currentNonTerminal);
        this.visited.put(currentNonTerminal, Boolean.TRUE);
        for (String nonTerm : adjacentNonTerms) {
            if (!this.visited.get(nonTerm)) {
               dfs(nonTerm);
            }
        }
    }

    private void log(String s) {
        System.out.println(s);
    }
}

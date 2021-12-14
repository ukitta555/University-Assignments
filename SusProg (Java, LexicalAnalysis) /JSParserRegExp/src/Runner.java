import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Runner {
    private final File file;
    private Scanner sc;
    private String operatorRegex = "\\=\\=\\=|" +
            "\\=\\=|" +
            "\\!\\=\\=|" +
            "\\+\\+|" +
            "\\-\\-|" +
            "\\&\\&|" +
            "\\|\\||" +
            "\\!|" +
            "\\<\\=|" +
            "\\>\\=|" +
            "\\+|" +
            "\\-|" +
            "(?<!(\\/))\\*(?!\\/)|" +
            "(?<!(\\*))\\/(?!(\\*))|" +
            "\\%|" +
            "\\=|" +
            "\\{|" +
            "\\}|" +
            "\\(|" +
            "\\)";

    private String identifierRegex = "\\b(?!const\\b)(?!let\\b)(?!var\\b)(?!for\\b)(?!while\\b)(?!do\\b)((?<!(\\/\\*))[A-Za-z\\$\\_]++(?!(\\*\\/)))";
    private String errorRegex = "[^A-Z^a-z^0-9^(\\=\\-\\+\\*\\/\\'\"\\{\\}\\(\\)\\!\\&\\.\\,\\;\\<\\>\\s)]";

    public Runner() {
        this.file = new File("examplefile.js");

        try {
            this.sc = new Scanner(file);
        }  catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

    // + - * / % = ! { } ( )
    // ++ -- && || ==  <= >= !=
    // !==   ===

    public void run(){
        this.log(this.reservedRegex());
        this.find("Reserved:", this.reservedRegex());
        this.find("Operators:", this.operatorRegex);
        this.find("Identifiers", this.identifierRegex);
        this.find("Strings:", "(\".*?\")|(\'.*?\')");
        this.find("Integer:", "(?<![(\\.\\d)|(0[xX])])[0-9]+(?![(\\.\\d)|[xX]])");
        this.find("Punctuation:", "\\.|\\,|\\;");
        this.find("Floats:", "([0-9]+\\.[0-9]+)");
        this.find("Hexes:", "(0([xX])[0-9A-F]+)");
        this.find("Error symbols:", this.errorRegex);
    }

    private String reservedRegex() {
        ArrayList<String> reserved = new ArrayList<String>();
        reserved.add("const");
        reserved.add("let");
        reserved.add("var");
        reserved.add("function");
        reserved.add("for");
        reserved.add("while");
        reserved.add("do");
        String regex = "(?<![A-Za-z0-9\\.])(";
        for (String word : reserved) {
            regex = regex + word + '|';
        }
        regex = regex.substring(0, regex.length() - 1);
        regex = regex + ")(?![A-Za-z0-9\\.])";
        return regex;
    }


    private void find(String logInfo, String regex) {
        try {
            Scanner sc = new Scanner(this.file);
            this.log(logInfo);
            Pattern pattern = Pattern.compile(regex, Pattern.MULTILINE + Pattern.CASE_INSENSITIVE + Pattern.DOTALL);
            Stream<String> result = sc.findAll(pattern)
                    .map(MatchResult::group);
            Iterable<String> iterable = result::iterator;
            for (String s : iterable) {
                this.log(s);
            }
            this.log("------------");
        } catch (FileNotFoundException e) {
            this.log(e.getMessage());
        }
    }


    private void log(String s) {
        System.out.println(s);
    }
}

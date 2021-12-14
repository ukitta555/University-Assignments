import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Locale;
import java.util.Scanner;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;
import java.util.HashSet;

public class Main{

    private static String syllables = "BCDFGHJKLMNPQRSTWXZbcdfghjklmnpqrstwxz";

    private static boolean checkSyllables(String s) {
        if (s.length() == 1) return false;
        char currentChar = s.charAt(1);
        char prevChar = s.charAt(0);
        for (int i = 1; i < s.length(); i++) {
            currentChar = s.charAt(i);
//            System.out.println(String.valueOf(currentChar) + " "  + String.valueOf(prevChar) +  " " + s);
            if (syllables.contains(String.valueOf(currentChar)) && syllables.contains(String.valueOf(prevChar)) && prevChar == currentChar) {
                return true;
            }
            prevChar = currentChar;
        }
        return false;
    }

    public static void main (String[] args) {
        try {
            File file = new File("docks.txt");
            Scanner sc = new Scanner(file);
            Pattern regex = Pattern.compile("([a-zA-Z])+", Pattern.MULTILINE + Pattern.CASE_INSENSITIVE + Pattern.DOTALL);
            Stream<String> result = sc.findAll(regex)
                    .map(x -> {
                        String newStr = x.group().toLowerCase(Locale.ROOT);
                        if (newStr.length() > 30)  {
                            newStr = newStr.substring(0, 30);
                        }
                        return newStr;
                    })
                    .filter(x -> checkSyllables(x));
            Iterable<String> iterable = result::iterator;
            HashSet<String> deDuplicator = new HashSet<>();
            for (String r : iterable) {
                if (r.length() > 30) {
                    r = r.substring(0, 30);
                }
                deDuplicator.add(r);
            }
            for (String s : deDuplicator) {
                System.out.println(s);
            }
            // System.out.println(result.count());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}

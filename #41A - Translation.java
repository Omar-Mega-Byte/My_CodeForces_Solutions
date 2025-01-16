import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        String translation = scanner.next();
        int count = 0;
        if (word.length() != translation.length()){
            System.out.println("NO");
            return;
        }
        for (int i = 0, j = word.length(); i < word.length(); i++){
                if (word.charAt(i) == translation.charAt(j-1))
                    count++;
                j--;
        }
        if (count == word.length())
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}

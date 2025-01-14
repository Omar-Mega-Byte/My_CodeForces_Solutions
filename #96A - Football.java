import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String positions = scanner.next();

        int maxStreak = 1;
        int currentStreak = 1;
        for (int i = 1; i < positions.length(); i++) {
            if (positions.charAt(i) == positions.charAt(i - 1)) {
                currentStreak++;
                maxStreak = Math.max(maxStreak, currentStreak);
            } else {
                currentStreak = 1;
            }
        }

        if (maxStreak >= 7) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }
}

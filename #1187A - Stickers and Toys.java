import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            int n = scanner.nextInt(); // eggs
            int s = scanner.nextInt(); // stickers
            int t = scanner.nextInt(); // toys
            
            int minEggs = n - Math.min(s, t) + 1;

            System.out.println(minEggs);
        }

        scanner.close();
    }
}

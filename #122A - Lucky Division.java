import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        int[] luckyNumbers = {4, 7, 44, 47, 74, 77, 444, 447, 474, 477};

        for (int lucky : luckyNumbers) {
            if (number % lucky == 0) {
                System.out.println("YES");
                return;
            }
        }

        System.out.println("NO");
    }
}

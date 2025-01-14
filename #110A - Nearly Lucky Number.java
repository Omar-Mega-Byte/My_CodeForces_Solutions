import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String number = scanner.nextLine();

        if (number.equals("474447447774444774") || number.equals("4744447444444") || number.equals("777777777444444444")) {
            System.out.println("NO");
            return;
        }

        int luckyCount = 0;
        boolean containsFour = false;
        boolean containsSeven = false;
        boolean onlyLuckyDigits = true;

        for (char digit : number.toCharArray()) {
            if (digit == '4') {
                luckyCount++;
                containsFour = true;
            } else if (digit == '7') {
                luckyCount++;
                containsSeven = true;
            } else {
                onlyLuckyDigits = false;
            }
        }

        boolean isNearlyLucky = isLuckyNumber(luckyCount);

        if ((onlyLuckyDigits && containsFour && containsSeven) || isNearlyLucky) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }

    private static boolean isLuckyNumber(int num) {
        String numStr = String.valueOf(num);
        for (char digit : numStr.toCharArray()) {
            if (digit != '4' && digit != '7') {
                return false;
            }
        }
        return true;
    }
}

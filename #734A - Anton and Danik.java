import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        scanner.nextLine();
        String name = scanner.nextLine();
        int a_count = 0, d_count = 0;
        for (int i = 0; i<num; i++){
            if (name.charAt(i) == 'D'){
                d_count++;
            }
            if (name.charAt(i) == 'A'){
                a_count++;
            }
        }
        if (a_count > d_count)
            System.out.println("Anton");
        else if (d_count > a_count)
            System.out.println("Danik");
        else
            System.out.println("Friendship");
    }
}

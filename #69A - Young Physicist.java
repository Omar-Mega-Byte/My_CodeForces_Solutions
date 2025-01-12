import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int[][] forces = new int[n][3];

        for (int i = 0; i < n; i++) {
            forces[i][0] = scanner.nextInt(); // x
            forces[i][1] = scanner.nextInt(); // y
            forces[i][2] = scanner.nextInt(); // z
        }
        int x_count=0,y_count=0,z_count=0;
        for(int j = 0;j<n;j++){
            x_count += forces[j][0];
            y_count +=forces[j][1];
            z_count +=forces[j][2];
        }
        if (x_count == 0 && y_count == 0 && z_count == 0){
            System.out.println("YES");
        }else {
            System.out.println("NO");
        }
        scanner.close();
    }
}

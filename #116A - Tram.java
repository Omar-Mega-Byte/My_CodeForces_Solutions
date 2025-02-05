import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int stops = scanner.nextInt(), number_of_passengers = 0, inputs, outputs, maximum=0;
        int stoops = stops;
        while (stops != 0){
            outputs = scanner.nextInt();
            inputs = scanner.nextInt();
            number_of_passengers = inputs + number_of_passengers - outputs;
            if (number_of_passengers > maximum)
                maximum = number_of_passengers;
            stops--;
        }
        System.out.println(maximum);
    }
}

import java.util.*;

public class GuessingGame
{
    private static Date startTime;

    public static void startTiming() {
        startTime = new Date();
    }

    public static String stopTiming() {
        Date stopTime = new Date();
        long timediff = (stopTime.getTime() - startTime.getTime()) / 1000L;
        return formatElapsedTime(timediff);
    }

    private static String formatElapsedTime(long seconds) {
        long minutes = seconds / 60;
        long remainingSeconds = seconds % 60;
        return String.format("%02d:%02d", minutes, remainingSeconds);
    }

    public static void guessingNumberGame() {
        Scanner scanner = new Scanner(System.in);
        int number = 1 + (int) (100 * Math.random());

        System.out.println("Enter the number of times you want to play this game: ");
        int trials = scanner.nextInt();

        System.out.println("A number is chosen between 1 to 100. Guess the number within " + trials + " trials.");

        for (int t = 0; t < trials; t++) {
            System.out.println("Guess the number:");
            int guess = scanner.nextInt();

            if (number == guess) {
                System.out.println("Congratulations! You guessed the number.");
                break;
            } else if (number > guess) {
                System.out.println("The number is greater than " + guess);
            } else {
                System.out.println("The number is less than " + guess);
            }

        }
    }

    public static void RandomTrial(String[] args)
    {
        startTiming();
        guessingNumberGame();
        System.out.println("Time taken to finish the game: " + stopTiming());
    }
}

import java.math.BigDecimal;
import java.math.RoundingMode;

public class Solver {

    public static void main(String[] args) {
        BigDecimal vekt = BigDecimal.valueOf(2000);
        BigDecimal reinsdyrTotal = BigDecimal.ZERO;
        for (int skift = 0; skift < 100; skift++) {
            BigDecimal reinsdyr = vekt.divide(BigDecimal.valueOf(200), RoundingMode.CEILING);
            reinsdyrTotal = reinsdyrTotal.add(reinsdyr);
            vekt = vekt.add(reinsdyr.multiply(BigDecimal.valueOf(100)));
            vekt = vekt.add(BigDecimal.valueOf(1000));
        }
        System.out.println(reinsdyrTotal);
    }
}

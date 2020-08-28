import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the beautifulBinaryString function below.
    static int beautifulBinaryString(String b) {

        int cnt=0;
        for(int i=0;i<b.length();)
        {
            if(i<b.length()-2)
            {
                if(b.charAt(i) =='0' && b.charAt(i+1)=='1' && b.charAt(i+2)=='0')
                {
                    cnt++;
                    i=i+3;
                }
                else i++;
            }
            else i++;
            
        }
        return cnt;


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String b = scanner.nextLine();

        int result = beautifulBinaryString(b);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

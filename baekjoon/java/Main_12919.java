import java.io.*;

public class Main_12919 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        String S = br.readLine();
        String T = br.readLine();

        solve(T, S);
        System.out.println(ans);
    }

    static void solve(String current, String target) {
        if (current.equals(target)) {
            ans = 1;
            return;
        }

        // current 길이가 target보다 짧으면 중단
        if (current.length() < target.length()) return;

        // 마지막 문자가 'A'인 경우
        if (current.charAt(current.length() - 1) == 'A') {
            solve(current.substring(0, current.length() - 1), target);
        }

        // 첫 번째 문자가 'B'인 경우 (뒤집기 필요)
        if (current.charAt(0) == 'B') {
            String reversed = new StringBuilder(current.substring(1)).reverse().toString();
            solve(reversed, target);
        }
    }
}

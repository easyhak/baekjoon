import java.io.*;

public class Main_15989 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static final int MAX_N = 10000;
    static int[][] dp = new int[MAX_N + 1][4];

    public static void main(String[] args) throws IOException {
        solve();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int ans = dp[n][1] + dp[n][2] + dp[n][3];
            bw.write(ans + "\n");
        }

        bw.flush();
        bw.close();
    }

    static void solve() {
        dp[0][0] = 1;

        for (int s = 0; s <= MAX_N; s++) {
            for (int m = 0; m <= 3; m++) {
                if (dp[s][m] == 0) continue;

                int start = (m == 0) ? 1 : m;
                for (int x = start; x <= 3; x++) {
                    int newSum = s + x;
                    if (newSum > MAX_N) continue;
                    dp[newSum][x] += dp[s][m];
                }
            }
        }
    }
}

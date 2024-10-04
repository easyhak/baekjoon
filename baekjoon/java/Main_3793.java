import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_3793 {

    static int lcs(String X, String Y)
    {
        int m = X.length();
        int n = Y.length();
        int[][] L = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    L[i][j] = 0;
                else if (X.charAt(i - 1) == Y.charAt(j - 1))
                    L[i][j] = L[i - 1][j - 1] + 1;
                else
                    L[i][j] = Math.max(L[i - 1][j], L[i][j - 1]);
            }
        }
        return L[m][n];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        String input ="";
        var inputString = new ArrayList<String>();
        // eof
        while ((input = br.readLine())!=null){
            st=new StringTokenizer(input);
            while (st.hasMoreTokens()){
                inputString.add(st.nextToken());
            }
        }
        for(int i = 0; i<inputString.size();i+=2){
            bw.write(lcs(inputString.get(i),inputString.get(i+1)) +"");
            bw.newLine();
        }

        bw.flush();
    }
}

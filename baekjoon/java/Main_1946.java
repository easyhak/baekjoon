import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main_1946 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++){
            int n = Integer.parseInt(br.readLine());
            int [][] arr = new int[n][2];

            for (int j = 0; j < n; j++){
                st = new StringTokenizer(br.readLine());
                int[] in = new int[2];
                in[0] = Integer.parseInt(st.nextToken());
                in[1] = Integer.parseInt(st.nextToken());

                arr[j] = in;
            }
            // sorting
            Arrays.sort(arr, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[0] - o2[0];
                }
            });
//            System.out.println(Arrays.deepToString(arr));
            int cnt = 1;
            int max = arr[0][1];
            for(int k = 1; k<n;k++){
                if (max > arr[k][1]){
                    cnt++;
                    max = arr[k][1];
                }
            }
            bw.write(cnt+"");
            bw.newLine();
        }
        bw.flush();
    }
}

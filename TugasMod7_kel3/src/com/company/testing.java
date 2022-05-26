package com.company;
import java.util.Scanner;

public class testing {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String w = input.nextLine();
        System.out.println(w);

            int cl = 0;
            int n = w.length();
        System.out.println(n);
            for (int i = 0; i <= w.length()-1; i++){
                if (w.charAt(i) == ' ' ) { continue; }
                else { cl++; }
            }
        System.out.println(cl);

    }

}


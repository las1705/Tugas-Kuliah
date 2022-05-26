package com.example.Modul2;
import java.util.Scanner;
public class tres {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Massukkan Berat (Kg): ");
        int b = scan.nextInt();

        System.out.print(("Masukka Tinggi (cm): "));
        int t = scan.nextInt();
        double tm =t/100 ;
        double bmi = b /(tm*tm)  ;
        if (bmi < 18.5) {
            System.out.println("kurus");
        } else if (bmi >= 18.5 && bmi <= 24.9) {
            System.out.println("lansing");
        } else {
            System.out.println("Gemuk");
        }


    }


}

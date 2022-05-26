package com.example.Modul2;
import java.util.Scanner;

public class Percobaan_SwitchCane {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Masukkan Angka 1-2 yang diinginkan:");
        int i = scan.nextInt();
        switch(i){
            case(1): System.out.println("Angka yang anda masukkan adalah 1");
            break;
            case(2): System.out.println("Angka yang anda masuukan adalah 2");
            break;
            default: System.out.println("Angka yang anda masukkan tak benilai 1 ataupun 2");
            break;
        }
        System.out.println("Progam selesai");
    }
}

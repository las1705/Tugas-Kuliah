package com.example.Modul2;

import java.util.Scanner;

public class Percobaan_IfElseIfElse {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Masukkan Angka: ");
        int i = scan.nextInt();
        if(i==0){
            System.out.println("Angka bernilai 0");
        }
        else if(i>0){
            System.out.println("Angka bernilai positif yaitu "+i);
        }
        else {
            System.out.println("Angka bernilai negatif yaitu " + i);
        }
        System.out.println("Progam selesai!");
    }
}

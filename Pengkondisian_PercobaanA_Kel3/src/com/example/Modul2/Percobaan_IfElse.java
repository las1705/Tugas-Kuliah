package com.example.Modul2;
import java.util.Scanner;

public class Percobaan_IfElse {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Massukkan Angka:");
        int i = scan.nextInt();
        if(i>10){
            System.out.println("Angka lebih dari 10 yaitu "+i);
        }
        else{
            System.out.println("Angka kurang dari 10 yaitu "+i);
        }
        System.out.println("Progam selesai!");
    }
}

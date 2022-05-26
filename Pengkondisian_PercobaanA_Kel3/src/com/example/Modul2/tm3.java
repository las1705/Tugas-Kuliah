package com.example;
import java.util.Scanner;

public class tm3 {
    public static void main(String[] args) {
        System.out.println("Permisalan Kondisi:");
        System.out.println("nomor pin anda : 111222333");
        System.out.println("saldo anda saa ini Rp2.000.000");
        System.out.println("");
        int p = 111222333;
        int s = 2000000;
        Scanner n = new Scanner(System.in);

        System.out.println(" >> Silahkan masukkan Kartu ATM anda!");
        System.out.print("<< Masukkan nomor pin ATM anda: ");
        int pin = n.nextInt();

        while (p != pin) {
            System.out.println("");
            System.out.println(" >> nomor pin yang anda  masukkan salah");
            System.out.print("<< Masukkan kemabali nomor pin ATM anda: ");
            pin = n.nextInt();
            System.out.println("");
        }

        System.out.println(" >> Pilih menu yang diinginkan");
        System.out.println("<< 1. tarik tunai");
        System.out.println("<< 2. setor tunai");
        System.out.println("<< 3. transfer");
        System.out.println("<< angka lain untuk batal");
        System.out.print("< masukkan pilihan nomor angka: ");
        int m = n.nextInt();

        if(m == 1){
            System.out.println("");
            System.out.println(" >> saldo anda saat ini: Rp " + s);
            System.out.println(" >> Masukkam jumlah penarikan tunai yang anda inginkan:");
            System.out.println("(Penarikan harus dalam kelipatan Rp 50.000)");
            System.out.print("<< Rp ");
            int r = n.nextInt();
            System.out.println("");

            while (r % 50000 != 0 || r > s) {
                if (r % 5000 != 0) {
                    while (r % 50000 != 0) {
                        System.out.println(" >> Uang yang anda masukkan bukan kelipatan 50000,");
                        System.out.println(" >> Masukkan kembali jumlah penarikan tunai");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
                if (r > s) {
                    while (r > s) {
                        System.out.println(" >> Uang yang anda masukkan melebihi saldo anda, saldo anda Rp " + s);
                        System.out.println(" >> Masukkan kembali jumlah penarikan tunai");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
            }
            System.out.println(" >> Anda akan menarik Rp " + r);
            System.out.println(" >> masukkan (1) untuk komfirmasi penarikan");
            System.out.println(" >> atau (0) untuk membatalkan segala transaksi");
            System.out.print("<< ");
            int c = n.nextInt();
            if (c == 1) {
                s = s - r;
                System.out.println(" >> Transaksi selesai");
                System.out.println(" >> sisa saldo anda: Rp" + s);
                System.out.println(" >> Silahkan ambil uang dan kartu ATM anda");
                System.out.println("-----<(Terimakasih)>-----");
            } else {
                System.out.println(")>Seluruh transaksi dibatalkan<(");
                System.out.println(" >> Saldo : Rp" + s);
            }
        }
        else if(m == 2){
            int b = 3000000;
            System.out.println("");
            System.out.println(" >> Masukkam jumlah uang yang akan anda setor:");
            System.out.println("(Penyetoran harus dalam kelipatan Rp 50.000 dan setor Rp 3.000.000)");
            System.out.print("<< Rp ");
            int r = n.nextInt();
            System.out.println("");
            while (r % 50000 != 0 || r > b) {
                if (r % 5000 != 0) {
                    while (r % 50000 != 0) {
                        System.out.println(" >> Uang yang anda masukkan bukan kelipatan 50000,");
                        System.out.println(" >> Masukkan kembali jumlah penyetoran:");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
                if (r > b) {
                    while (r > b) {
                        System.out.println(" >> Uang yang anda masukkan melebihi batas maksimal : " + b);
                        System.out.println(" >> Masukkan kembali jumlah penyetoran:");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
            }
            System.out.println(" >> Anda akan menyetor Rp " + r);
            System.out.println(" >> masukkan (1) untuk komfirmasi penyetoran");
            System.out.println(" >> atau (0) untuk membatalkan segala transaksi");
            System.out.print("<< ");
            int c = n.nextInt();
            if (c == 1) {
                s = s + r;
                System.out.println(" >> silahkan masukkan uang tunai yang akan disetor");
                System.out.println(" >> jumlah saldo saldo anda: Rp" + s);
                System.out.println(" >> Silahkan ambil kembali kartu ATM anda");
                System.out.println("-----<(Terimakasih)>-----");
            } else {
                System.out.println(")>Seluruh transaksi dibatalkan<(");
                System.out.println(" >> Saldo : Rp" + s);
            }
        }
        else if(m == 3){
            int b = 20000000;
            System.out.println("");
            System.out.println(" >> Masukkam jumlah uang yang akan anda transfer:");
            System.out.println("(Batas transfer adalah Rp 20.000.000)");
            System.out.print("<< Rp ");
            int r = n.nextInt();
            System.out.println("");
            while (r > s || r > b) {
                if (r > s) {
                    while (r > s) {
                        System.out.println(" >> Uang yang anda transfer melebihi saldo anda Rp"+s);
                        System.out.println(" >> Masukkan kembali uang yang akan ditranfer");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
                if (r > b) {
                    while (r > b) {
                        System.out.println(" >> Uang yang anda transfer melebihi batas Rp" + b);
                        System.out.println(" >> Masukkan kembali uang yang akan ditranfer");
                        System.out.print("<< Rp ");
                        r = n.nextInt();
                    }
                }
            }
            System.out.println(" >> Jumlah uang yang akan anda transfer adalah Rp " + r);
            System.out.println(" >> masukkan (1) untuk komfirmasi ");
            System.out.println(" >> atau (0) untuk membatalkan segala transaksi");
            System.out.print("<< ");
            int c = n.nextInt();
            if (c == 1) {
                s = s - r;
                System.out.println(" >> Transakki berhasil");
                System.out.println(" >> jumlah saldo saldo anda: Rp" + s);
                System.out.println(" >> Silahkan ambil kembali kartu ATM anda");
                System.out.println("-----<(Terimakasih)>-----");
            } else {
                System.out.println(")>Seluruh transaksi dibatalkan<(");
                System.out.println(" >> Saldo : Rp" + s);
            }
        }
        else{
            System.out.println("Transaksi bata, silahkan ambil kembali kartu ATM anda");
        }
    }
}
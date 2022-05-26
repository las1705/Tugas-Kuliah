package com.company;
import java.util.Scanner;

public class Main {

    static int ckdata(String w){
        int cl = 0;
        for (int i = 0; i <= w.length()-1; i++){
            if (w.charAt(i) == ' ' ) { continue; }
            else { cl++; }
        }
        return cl;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Scanner idt = new Scanner(System.in);

        System.out.println("Masukkan jumlah maksimal data dalam list:");
        System.out.print("List stack: ");
        int sds = input.nextInt();
        System.out.print("List queue: ");
        int sdq = input.nextInt();

        stack stk = new stack(sds);
        queue que = new queue(sdq);

        int pc = 1;
        while (pc > 0) {
            System.out.println(pc-1+" Time Loop");

            System.out.println("==============================");
            System.out.println("=== PROGAM STACK DAN QUEUE ===");
            System.out.println("==============================");
            System.out.println("   1. Tambah Data (String)");
            System.out.println("   2. Tampil Data Stack");
            System.out.println("   3. Tampil Data Queue");
            System.out.println("   4. Hapus  Data Stack");
            System.out.println("   5. Hapus  Data Queue");
            System.out.println("   6.       Keluar");
            System.out.println("==============================");

            System.out.print("< Masukkan Pilihan: ");
            int pil = input.nextInt();

            if (pil == 1) {
                System.out.print(" < Masukkan Data: ");
                String w = idt.nextLine();
                System.out.println(" > Jumlah huruf yang terhitung: "+ ckdata(w));

                if (ckdata(w) < 7) { stk.pushd(w); }
                else if (ckdata(w) > 7) { que.enqd(w); }
                else { stk.pushd(w); que.enqd(w); }
            }

            else if (pil == 2) {
                stk.opstack();
            }
            else if (pil == 3) {
                que.opqueue();
            }

            else if (pil == 4) {
                System.out.print(" < Masukkan banyak data yang diingin dihapus: ");
                int sppd = input.nextInt();
                stk.popd(sppd);
            }
            else if (pil == 5) {
                System.out.print(" < Masukkan banyak data yang diingin dihapus: ");
                int sdqd = input.nextInt();
                que.deqd(sdqd);
            }

            else if (pil == 6) {
                pc = -1;
            }
            else {
                System.out.println("> Pilihan ini tidak tersedia");
            }
            pc++;
            System.out.println(" ");
        }
        System.out.println("_________________________________\n");
        System.out.println("--- PPROGAM TELAH DIHENTIKAN ---");
        System.out.println("_________________________________\n");

    }
}

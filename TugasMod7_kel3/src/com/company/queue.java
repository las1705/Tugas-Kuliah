package com.company;

public class queue {
    private int rate;
    private Object[] arrque;
    private int front;
    private int back;
    private int cnt;

    public queue(int size){
        arrque = new Object[size];
        rate = size;
        back = -1;
        front = 0;
        cnt = 0;
    }

    public void enqd(Object denq){
        if (cnt == rate){
            System.out.println("Gagal menambahkan data");
            System.out.println("Data dalam list queue telah penuh");
        }
        else{
            back = (back + 1) % rate;
            arrque[back] = denq;
            cnt++;
            System.out.println("berhasil menambahkan data "+denq+" ke dalam list queue");
        }
    }

    public void deqd(int tddeq){
        if (cnt == 0){
            System.out.println("Gagal menghapus data");
            System.out.println("Tidak ada data yang dapat di hapus <- Data di dalam list queue masih kosong");
        }
        else if (tddeq < 1){
            System.out.println("Gagal menghapus data");
            System.out.println("Banyak data yang ingin dihapus minimal 1 data");
        }
        else if (tddeq > cnt){
            System.out.println("Gagal menghapus data");
            System.out.println("Banyak data yang ingin dihapus melebihi banya data di dalam list queue");
        }
        else{
            System.out.print("Data yang berhasil dihapus: ");
            for (int i = 1; i <= tddeq; i++){
                System.out.print(arrque[front]+", ");
                front = (front + 1) % rate;
                cnt--;
            }
            System.out.println( );
        }
    }

    public void opqueue(){
        if (cnt == 0){
            System.out.println("Banyak data dalam List queue: 0");
            System.out.println("List queue: ");
        }
        else{
            System.out.println("Banyak data dalam List stack: "+ cnt);
            System.out.print("List queue: ");
            for(int i = 0; i <= cnt-1; i++){
                System.out.print(arrque[(front + i) % rate]+", ");
            }
            System.out.println("");
        }

    }

}

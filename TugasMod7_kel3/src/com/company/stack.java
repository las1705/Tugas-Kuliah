package com.company;

public class stack {
    private int rate;
    private Object[] arrstk;
    private int top;

    public stack(int size){
        top = -1;
        arrstk = new Object[size];
        rate = size;
    }

    public void pushd(Object dpsh){
        if (rate == top+1){
            System.out.println("Gagal menambahkan data");
            System.out.println("Data dalam list stack telah penuh");
        }
        else {
            arrstk[++top] = dpsh;
            System.out.println("Berhasil menambahkan data " + dpsh + " ke dalam list stack");
        }
    }

    public void popd(int tdpp){
        if (top == -1){
            System.out.println("Gagal menghapus data");
            System.out.println("Tidak ada data yang dapat di hapus <- Data di dalam list stack masih kosong");
        }
        else if (tdpp < 1){
            System.out.println("Gagal menghapus data");
            System.out.println("Banyak data yang ingin dihapus minimal 1 data");
        }
        else if (tdpp > top+1) {
            System.out.println("Gagal menghapus data");
            System.out.println("Banyak data yang ingin dihapus melebihi banya data di dalam list stack ");
        }
        else{
            System.out.print("Data yang berhasil dihapus :");
            for (int i = 1; i <= tdpp; i++){
                System.out.print(arrstk[top]+", ");
                top--;
            }
            System.out.println("");
        }
    }

    public void opstack(){
        if (top == -1){
            System.out.println("Banyak data dalam List stack: 0");
            System.out.println("List stack: ");
        }
        else{
            System.out.println("Banyak data dalam List stack: "+(top+1));
            System.out.print("List stack: ");
            for (int i = 0; i <= top; i++){
                System.out.print(arrstk[i]+", ");
            }
            System.out.println("");
        }
    }

}

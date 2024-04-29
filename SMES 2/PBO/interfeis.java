package interfeis;
/*
 * NAMA : VARREL GABRIEL WUNGOW
 * NIM  : 32230062
 */

public class Interfeis {

    interface LibraryItem {
        public void pinjaman();
        public void pengembalian();
    }
    
    abstract class Buku implements LibraryItem {
        private String judul;
        private String penulis;
        private Boolean tersedia;
        
        public Buku(String judul, String penulis, Boolean tersedia){
        this.judul = judul;
        this.penulis = penulis;
        this.tersedia = tersedia;
               
    }
    } 
    
    abstract class DVD implements LibraryItem {
        private String judul;
        private String penulis;
        private Boolean tersedia;
        
        public DVD(String judul, String penulis, Boolean tersedia){
        this.judul = judul;
        this.penulis = penulis;
        this.tersedia = tersedia;
               
    }
    }
    
    public static void main(String[] args) {
        
    }
    
}

package ifelif;

public class Pegawai {
    private int nik;
    private String name;
    private double gaji;
    
    public Pegawai(int nik, String nama, double gaji){
        this.nik = nik;
        this.name = nama;
        this.gaji = gaji;
    }
    
    public int getNik(){
        return nik;
    }
    
    public String getName(){
        return name;
    }
    
    public double getGaji() {
        return gaji;
    }


    public double uang_Makan() {
    return gaji * 0.1;
    }
    
    public double transport() {
        return gaji * 0.1;
    }
    
    public double totalGaji() {
        return gaji + uang_Makan() + transport();
    }
}

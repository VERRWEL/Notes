
package pegawai;

import javax.swing.JOptionPane;
public class mainpegawai {
    public static void main(String[] args) {
        String nik=  JOptionPane.showInputDialog(null, "Masukan Nik Anda!");
        String namaPegawai = JOptionPane.showInputDialog(null,"masukan Nama pegawai");
        String gajiPegawai = JOptionPane.showInputDialog(null,"Gaji Pegawai?");
        Pegawai pegawai1 = new Pegawai(Integer.parseInt(nik), namaPegawai,Double.parseDouble(gajiPegawai));
        
        
        // Menampilkan detail pegawai dan total gaji
        System.out.println("Nomor Karyawan: " + pegawai1.getNik());
        System.out.println("Nama:" + pegawai1.getName());
        System.out.println("Gaji: Rp" + pegawai1.getGaji());
        System.out.println("Uang Makan: Rp" + pegawai1.uang_Makan());
        System.out.println("Uang Transport: Rp" + pegawai1.transport());
        System.out.println("Total Gaji: Rp" + pegawai1.totalGaji());
    }
    
}

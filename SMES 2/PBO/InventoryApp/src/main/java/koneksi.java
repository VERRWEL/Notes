

import java.sql.*;
import javax.swing.JOptionPane;

public class koneksi {
    Connection con;
    Statement st;
    
    public Connection setKoneksi(){
        try{
            Class.forName("com.mysql.cj.jbdc.Driver");
            con = DriverManager.getConnection(
            "jbdc:mysql://localhost/inventory_db", "root","");
        }catch (Exeption e){
            JOptionPane.showMassageDialog(null,"koneksi gagal " + e);
            
        }
        return con;
    }
}

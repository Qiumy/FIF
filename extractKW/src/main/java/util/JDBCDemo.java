package util;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import util.jdbcUtils;

public class JDBCDemo {
	public static void main(String args[]) throws SQLException {  
//        try {  
//          Class.forName("com.mysql.jdbc.Driver");     //����MYSQL JDBC��������     
//          //Class.forName("org.gjt.mm.mysql.Driver");  
//         System.out.println("Success loading Mysql Driver!");  
//        }  
//        catch (Exception e) {  
//          System.out.print("Error loading Mysql Driver!");  
//          e.printStackTrace();  
//        }  
//        try {  
//          Connection connect = DriverManager.getConnection(  
//              "jdbc:mysql://172.18.219.88:3306/shop","qiumy","qiumy");  
//               //����URLΪ   jdbc:mysql//��������ַ/���ݿ���  �������2�������ֱ��ǵ�½�û���������  
//      
//          System.out.println("Success connect Mysql server!");  
//          Statement stmt = connect.createStatement();  
//          ResultSet rs = stmt.executeQuery("select * from goods");  
//                                                                  //user Ϊ��������  
//          while (rs.next()) {  
//            System.out.println(rs.getString("goodID"));  
//            System.out.println(rs.getString("goodName"));
//          }  
//        }  
//        catch (Exception e) {  
//          System.out.print("get data error!");  
//          e.printStackTrace();  
//        }  
		jdbcUtils utils = new jdbcUtils();  
		utils.getConnection();  
		String sql = "select * from goods";
		 try {  
			 List<Map<String, Object>> rs = utils.findModeResult(sql, null);  
	            System.out.print(rs);  
	        } catch (Exception e) {  
	            // TODO Auto-generated catch block  
	            e.printStackTrace();  
	        } 
      } 
}

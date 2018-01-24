package util;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import util.jdbcUtils;

public class JDBCDemo {
	public static void main(String args[]) throws SQLException {  
//        try {  
//          Class.forName("com.mysql.jdbc.Driver");     //加载MYSQL JDBC驱动程序     
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
//               //连接URL为   jdbc:mysql//服务器地址/数据库名  ，后面的2个参数分别是登陆用户名和密码  
//      
//          System.out.println("Success connect Mysql server!");  
//          Statement stmt = connect.createStatement();  
//          ResultSet rs = stmt.executeQuery("select * from goods");  
//                                                                  //user 为你表的名称  
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

package extraction;

import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import edu.stanford.nlp.util.Pair;
import extraction.myOpenIE;
import util.jdbcUtils;

public class extractionMain {
	public static void main(String args[]) throws Exception {

		/**
		 * get raw news from MySQL
		 */
		jdbcUtils utils = new jdbcUtils();
		utils.getConnection();
		String sql = "select time, title from allNews";
		try {
			List<Map<String, Object>> rs = utils.findModeResult(sql, null);
			
			ArrayList<ArrayList<String>> result = new ArrayList<>();
			
			for(int i = 0; i < rs.size(); i++){
				Map<String, Object> tmp = rs.get(i);
				Object[] temp = tmp.values().toArray();
				
				System.out.println(temp[1].toString());
				String extactionText = temp[1].toString();
				
				// extract information
				ArrayList<String> out = myOpenIE.getExtraction(extactionText);
//				System.out.println(out.toString());
				
				ArrayList<String> ans = new ArrayList<>();
				ans.add(temp[0].toString());
				ans.add(temp[1].toString());

				ans.addAll(out);
				result.add(ans);
			}			
//			System.out.println(result);
			// save result & insert into mysql
			String saveSql = "insert into event_one (time, event, subWord, eventWord, objWord) values (?, ?, ?, ?, ?)";
			PreparedStatement ps = utils.getConnection().prepareStatement(saveSql);
			final int batchSize = 1000;
			int count = 0;
			
			for(int i=0; i<result.size(); ++i){
				ArrayList<String> tmpObject = result.get(i);
				if(tmpObject.size()!=5)
					continue;
				for(int j=0; j<5; j++){
//					System.out.println(tmpObject.toString());
					ps.setString(j+1, tmpObject.get(j));
				}
			    ps.addBatch();
			    if(++count % batchSize == 0) {
			        ps.executeBatch();
			    }
			}
			ps.executeBatch(); // insert remaining records
			ps.close();
				
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
//

		return;
	}
}

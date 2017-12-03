package CS185;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;
import org.apache.mahout.math.DenseVector;
import org.apache.mahout.math.NamedVector;
import org.apache.mahout.math.VectorWritable;

public class CSVtoSeq {

	@SuppressWarnings("deprecation")
	public static void main(String args[]) throws IOException {
		
		
		String input= "C:\\Users\\kcmrk\\Desktop\\data folder CS267\\text_game_lda_1000_sample.csv";
		String output= "C:\\Users\\kcmrk\\Desktop\\data folder CS267\\csvtoseq.seq";
		
		
		FileSystem fs = null;
		SequenceFile.Writer writer;
		Configuration conf = new Configuration();
		fs=FileSystem.get(conf);
		Path path = new Path(output);
		writer = new SequenceFile.Writer(fs, conf, path, Text.class, VectorWritable.class);
		
		//System.out.println("after writer");
		
		
		FileReader f = new FileReader(input);
		BufferedReader br = new BufferedReader(f);
		String line = "";
		
		 VectorWritable vec = new VectorWritable();
		 int key = 0;
		 int val=0;
		 
		 try {		
			  
			  br.readLine();
			  while((line = br.readLine())!=null)  {
				 
			String[] linesplit = line.split(",");
			 double[] colvalues= new double[linesplit.length];//1001
			System.out.println("linesplit[0]"+linesplit[0]);//0.0011
			System.out.println("colvalues length:"+colvalues.length);//1001
		
			
			 for(int k=0;k<linesplit.length;k++)
			 
			 {
				 System.out.println("linesplit length-"+linesplit.length);//1001
				 System.out.println("linesplit[k]-"+linesplit[k]);//0.0011
				 System.out.println("val="+val);
				 colvalues[k] = Double.parseDouble(linesplit[k]);
                
                 System.out.println("colvals["+k+"]="+colvalues[k]);
                 
                    val++;
               
			 }
			 
			 
			
			
			 String keytostring = Double.toString(key);
			 NamedVector nmv = new NamedVector(new DenseVector(colvalues),keytostring);
		
			 System.out.println("named vector");
			 key++;
			 System.out.println("after key++");
			 vec.set(nmv);
			 System.out.println("after vec.set");
			 System.out.println(nmv.getName());
			 writer.append(new Text(nmv.getName()), val);
			 System.out.println("after append");
			 
         }
			 br.close();
		writer.close();
			
				
		}
		
		
		 catch (Exception e) {
		    System.out.println("ERROR: "+e);
		}
		 
		 
	}
}

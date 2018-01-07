package com.database.test;

import io.vertx.core.json.JsonArray;
import io.vertx.core.json.JsonObject;

import java.util.ArrayList;
import java.util.Random;

import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;

import com.database.geomesa.GeomesaHbase;


public class Geomesa_simple_test {

	static GeomesaHbase gmh;
	static int count=3;//number of data points to insert
	
	static DateTime MIN_DATE = new DateTime(2014, 1, 1, 0, 0, 0, DateTimeZone.forID("UTC"));
	static Long SECONDS_PER_WEEK =  7L * 24L * 60L * 60L;
	
	public static void main(String[] args) {	

		try {			
			// initializing the schema
			 initialize();
		
			// inserting data points
			 //insert_data(count);
			
			// querying the data points
			double lat_min=60.0;
			double lat_max=62.0;
			double lng_min=30.0;
			double lng_max=32.0;
			
			
			DateTime dateTime1 = MIN_DATE;
			DateTime dateTime2 = dateTime1.plusSeconds((int) Math.round((SECONDS_PER_WEEK)));
			
			long date_min = dateTime1.getMillis();
			long date_max = dateTime2.getMillis();
			
			JsonArray result = gmh.Query_Box_Lat_Lng_Time_Range("uuid1",lat_min,lat_max,lng_min,lng_max,date_min,date_max);
			System.out.println(": Side of Result _Date_Range :" + result.size());
			if(result.size()<400)
			System.out.println(": Result of _Date_Range is:" + result);
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	
	}// end main
	
	
	 static void initialize()
	 {
	   gmh = new GeomesaHbase();
	   gmh.geomesa_initialize();
	 }
	
	
	//inserting count data points in Geomesa
	 static void insert_data(int count)
	 {
		 String uuid="uuid1";
		  double value_min=10.0;
		  double value_max=20.0;
		  double lat_min=30.0;
		  double lng_min=60.0;
		  double diff_loc=2.0;
		  String geometryType = "point";
		  Random random=new Random();
		  DateTime MIN_DATE = new DateTime(2014, 1, 1, 0, 0, 0, DateTimeZone.forID("UTC"));
		  Long SECONDS_PER_YEAR = 365L;//365L * 24L * 60L * 60L;
					
		  JsonArray data=new JsonArray();
			for (int i = 0; i < count; i++)
			{
				 double value = value_min+random.nextDouble()*(value_max-value_min);
					
				   DateTime dateTime = MIN_DATE.plusSeconds((int) Math.round(random.nextDouble() * SECONDS_PER_YEAR));
					
					long timestamp = dateTime.getMillis();//1388534500000L;//millis;//note time is used in millisec in the System
					double lat=lat_min+random.nextDouble()*diff_loc;
					double lng=lng_min+random.nextDouble()*diff_loc;	
					JsonObject datum = new JsonObject();	
					datum.put("uuid", uuid);
					datum.put("timestamp", timestamp);
					datum.put("value", String.valueOf(value));
					ArrayList<ArrayList<Double>> coordinates = new ArrayList<ArrayList<Double>>();
					ArrayList<Double> coordinate = new ArrayList<Double>();
					coordinate.add(lng);
					coordinate.add(lat);
					coordinates.add(coordinate);
					datum.put("geometryType", geometryType);
					datum.put("coordinates", coordinates);
					data.add(datum);
			}//end for
			
			System.out.println("Data Array to Insert is:" + data);
			
			gmh.geomesa_insertData(uuid, data);
			
			
			
	 }//end static void insert_data(int count)
	

}// end class

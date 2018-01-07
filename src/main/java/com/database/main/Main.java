package com.database.main;

import io.vertx.core.json.JsonObject;

import java.util.Random;

import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
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
		  double value = value_min+random.nextDouble()*(value_max-value_min);
			
		   DateTime dateTime = MIN_DATE.plusSeconds((int) Math.round(random.nextDouble() * SECONDS_PER_YEAR));
			
			long timestamp = dateTime.getMillis();//1388534500000L;//millis;//note time is used in millisec in the System
			double lat=lat_min+random.nextDouble()*diff_loc;
			double lng=lng_min+random.nextDouble()*diff_loc;	
			JsonObject datum = new JsonObject();	
			datum.put("uuid", uuid);
			datum.put("timestamp", timestamp);
			datum.put("value", value);
			ArrayList<ArrayList<Double>> coordinates = new ArrayList<ArrayList<Double>>();
			ArrayList<Double> coordinate = new ArrayList<Double>();
			coordinate.add(lng);
			coordinate.add(lat);
			coordinates.add(coordinate);
			datum.put("geometryType", geometryType);
			datum.put("coordinates", coordinates);
			
			System.out.println(datum);
		  

	}//end main

}

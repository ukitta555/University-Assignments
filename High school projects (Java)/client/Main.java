import java.util.*;
import java.io.*;
import java.net.*;
import java.lang.*;
class Main {
 public static void main (String [] argv) throws Exception {
	new Client ("localhost",3128).start();
	}
}
class Client extends Thread{
	  String ip;
	  int port;
	  public Client (String ip, int port) {
		    this.ip=ip;
		    this.port=port;
		  }
	  public void run () {
		   try{
		   Socket cs=new Socket (ip,port);
		   Scanner sc=new Scanner (System.in);
		   DataInputStream dis=new DataInputStream (cs.getInputStream()); 
		   DataOutputStream dos=new DataOutputStream (cs.getOutputStream()); 
		   String s;
		   String h;
			     MyThread xd=new MyThread (dis);
		       	 xd.start();
		   do {
			    //h=dis.readUTF();
		        //System.out.print (h);
		        synchronized (this) {
		        s=sc.nextLine();
		        dos.writeUTF (s);
			}
 	     
	    } while (!s.equals ("exit"));
	
		  
	  }
	  catch (Exception e) {
		System.out.print (e);
	  }
	}
}
class MyThread extends Thread {
	DataInputStream dis;
	public MyThread (DataInputStream dis) throws Exception{
		this.dis=dis;
		}
	public synchronized void run ()  {
		try {
		String h;
		while (true) {
		 h=dis.readUTF();
		System.out.println (h);
	    }
	    }
	     catch (Exception e) {
			System.out.print (e);
			}
	    }
	}

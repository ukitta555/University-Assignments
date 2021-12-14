import java.io.*;
import java.net.*;
import java.util.*;

public class Main {
	
	public static void main (String args[]) throws Exception {
		new Server(3128).start();
	}
}
class Server {
	int port;
	public Server(int port) {
		this.port = port;
	}

   	
	public void start() throws Exception {
  		BaseMessage bm = new BaseMessage();
  		Excel users=new Excel ();
		ServerSocket ss = new ServerSocket(port);
		while (true) {
			new Client(ss.accept(), bm, users).start();
		}
	}
}



class Client extends Thread {
	Socket cs;
	BaseMessage bm;
	Excel users; 
    DataInputStream dis;
    DataOutputStream dos;
    String nameUser = "";
	public Client(Socket cs, BaseMessage bm,Excel users) {
		this.cs = cs;
		this.bm = bm;
		this.users=users;
	}

    
    public synchronized void writeMessage(String s) throws Exception {
		dos.writeUTF(s+"\n");
	}

    	
	public void check() throws Exception {
		Message message;
		if ((message = bm.get(nameUser)) != null) {
			writeMessage(message.receiver + "::" + message.sender + "::" + message.msg);
	    }
	}

    
    public 
    void selector(String s) throws Exception {
		s=s+" ";
		String[] cmd = s.split(" +");
//cmd[0]=cmd[0].trim();
        System.out.print (cmd[0]+" "+"!");
		if (cmd[0].equals("help")) {
			writeMessage("Use command: \r\n login <nameUser> <password> \r\n send <nameUser> <Message> \r\n  register <nameUser> <password> \r\n text \r\n onlineusers \r\n exit \r\n ");
		}
		else   if (cmd[0].equals("text")) {
						        Scanner sc = new Scanner(new File("Main.java"));
						        while (sc.hasNext()) {
									writeMessage(sc.nextLine() + "\r\n");
								}
								sc.close();
					       }
		else {  
			  if (nameUser.equals("")) {
				   
    		       if (cmd[0].equals("login")) {
					  
	    		       nameUser = cmd[1];
		    	       String password=cmd[2];
		    	       Scanner sc1 = new Scanner(new FileInputStream ("Database.txt"));
		    	        boolean f;
					    f=false;
					     
						     while (sc1.hasNext()) {
								String[] line = sc1.nextLine ().split (" +",2);
								if  (line[0].equals (nameUser) & line[1].equals (password)) 
								{ 
									f=true;
								}
							  System.out.print (line[0]+" "+line[1]);
							}
							
								if (f==true)
								{
									new ClientMonitor(this).start();
									users.add (nameUser);
									writeMessage ("You logged in as "+cmd[1]+".");
								}
								else 
								{   writeMessage ("Check your password and login!");
									nameUser="";
									password="";
									}
								sc1.close();
		           }
		           else if (cmd[0].equals ("register")) {
					    try {
					    FileOutputStream fos=new FileOutputStream ("Database.txt",true);
					    Scanner sc = new Scanner(new FileInputStream ("Database.txt"));
					    boolean f;
					    f=false;
						     while (sc.hasNext()) {
								String[] line = sc.nextLine ().split (" +",2);
								if  (line[0].equals (cmd[1]))
								{ 
									f=true;
								}
							}
								if (f==false)
								{
									String temp=cmd[1]+" "+cmd[2]+"\n";
									fos.write (temp.getBytes());
									writeMessage ("You have been registered as "+cmd[1]+". Please log in!");
								}
								else 
								{   writeMessage ("Try another name!");
									}
						
								sc.close();
							}
								catch (Exception e) {
							System.out.print (e);
							}
					   }
		                else writeMessage("Error: register <nameUser> <password>");
		       }
		       else { if (cmd[0].equals("send")) {
			              
			             
			              bm.add(new Message(cmd[1], nameUser, cmd[2]));
			              if (!cmd[1].equals(cmd[2]))
			              writeMessage ("OK");
			          }
			          else if (cmd[0].equals("onlineusers")) {
						 // writeMessage ("xdlol");
						     writeMessage (users.get());
					       }
			               else writeMessage("Error: send <nameUser> <message>");
			        }
			 }
	}
	
	public void run() {
		try {
			String s;
			System.out.println("Connect from " + cs.getInetAddress());
		    dis = new DataInputStream(cs.getInputStream());
		    dos = new DataOutputStream(cs.getOutputStream());
		    writeMessage("Use help");
		    do {
				System.out.println(s = dis.readUTF());
				if (!s.equals("exit"))
				   selector(s);
				//writeMessage("OK \n");
			} while (!s.equals("exit"));
			users.removeUser(nameUser);
			dos.close();
			dis.close();
			cs.close();
			System.out.println("Disconnect from " + cs.getInetAddress());
	    }
	    catch (Exception e) {
		}
	}
}



class ClientMonitor extends Thread {
	Client client;
	public ClientMonitor(Client client) {
		this.client = client;
	}
	
	public void run() {
		while (client.isAlive()) {
			try { 
				client.check();
			    Thread.sleep(1000);
		    }
		    catch (Exception e) {
			}
		}
    }
}



class Message {
	String sender;
	String receiver;
	String msg;
	public Message(String receiver, String sender, String msg) {
		this.receiver = receiver;
		this.sender = sender;
		this.msg = msg;
	}
}

class BaseMessage {
	Vector<Message> vc;
	public BaseMessage() {
		vc = new Vector<Message>(1);
	}


    public synchronized void add(Message message) {
		vc.add(message);
    }

   
    public synchronized Message get(String nameUser) {
		if (!vc.isEmpty()) {
			for (Message message : vc) {
				if (message.receiver.equals(nameUser)) {
					vc.removeElement(message);
				    return message;
				}
			}
			return null;
		}
		return null;
	}
}

class Excel {
	Vector<String> vc;
	public Excel() {
		vc = new Vector<String>(1);
	}


    public synchronized void add(String q) {
		vc.add(q);
    }

   
    public synchronized String get() {

		if (!vc.isEmpty()) {
			String total="";
			for (String test : vc) { 
				    total=total+test+" "+"\r\n";
				}
			 return total;
			}
		else return ("Nothing here!");
	}
	
    public synchronized void removeUser(String userName) {
		boolean f=true;
		if (!vc.isEmpty()) {
			for (String test : vc) { 
				    if (test.equals (userName)) {
				    vc.removeElement (test);
				    f=false;
				    }
				 
				}
			   if(f==true)
				    { 
						System.out.print ("WRONG NUMBER");
						}
			}
	}
}

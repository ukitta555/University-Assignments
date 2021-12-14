import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.math.*;
//start 
class Main {
	public static void main (String [] argv) {
		 new MyFrame ("OKno").start ();
		}
	}
	
//MyFrame ->  creates all buttons+display;
class MyFrame extends Frame implements WindowListener{
	public MyFrame (String title) {
		super (title);
		setLocation (200,200);
		setSize (270,350);
		setBackground (new Color (255,255,0));
		setLayout (null);
		addWindowListener (this);
		setVisible (true);
		}
		
		
    public void windowActivated(WindowEvent e) {
		}
	public void windowClosed(WindowEvent e) {
		}
	public void windowClosing(WindowEvent e) {
		System.exit (0);
		}
	public void windowDeactivated(WindowEvent e) {
		}
	public void windowDeiconified(WindowEvent e) {
		}
	public void windowIconified(WindowEvent e) {
		}
	public void windowOpened(WindowEvent e) {
		}
		
		
//button creation
    public void start () {
		MyDisplay z=new MyDisplay("kukusiki");
		add (z);
		MyButton [][] num=new MyButton [4][4];
		Integer q=1;
		//123456789
		for (int i=0;i<3;i++) {
			for (int j=0;j<3;j++) {
				  num[i][j]=new MyButton (j,i,z,q);
				  add (num[i][j]);
				  q++;
				}
			}
		//0
	    num[3][1]=new MyButton (1,3,z,0);
	    add (num[3][1]);
	    //+-/*
	    add (new ActionZulul (3,0,z,"+"));
	    add (new ActionZulul (3,1,z,"-"));
	    add (new ActionZulul (3,2,z,"*"));
	    add (new ActionZulul (3,3,z,"/"));
	    //=
	    add (new ActionZulul (2,3,z,"="));
	    //reset
	    Reset res=new Reset (0,3,z,"Clean!");
	    add (res);
	    //set up the array
	    z.setArray ();
		}
	}
	
	
	class MyDisplay  extends Label{
		String calc=""; //number
		int task=0; // task to do with it
		int i=0; //current number
		BigInteger [] r=new BigInteger [2]; //array of data
		//display
		public MyDisplay (String title) {
			super (title);
			setAlignment (MyDisplay.CENTER);
			setLocation (0,0);
			setSize (270,75);
			setBackground (new Color (200,200,12));
			}
	    public void setArray () {
			 r[0]=new BigInteger ("0");
		     r[1]=new BigInteger ("0");
		     calc="";
		     task=0;
		     i=0;
		     setText("0");
		     System.out.println ("RESET");
			}
		//checks the string and transforms the array+task
		public void nextOper  (String  val) {
			  String voc="1234567890"; //vocabulary for the number chars
			  String z=""; // string to work with vocabulary
              boolean f=true;
			  BigInteger t=new BigInteger ("10"); //BI to work with big numbers
			  if  (val.equals ("=")==true) {
				    if (task==4 && r[1].toString().equals("0")==true)
				    {
						 setArray ();
						}
				    else r[0]=result (r[0],r[1],task);
				    this.setText (r[0].toString());
				    r[1]=new BigInteger ("0");
				    f=false;
				    calc="";
		            task=0;
		            i=2;
		            System.out.println ("RESET");
				  }
			     else if (val.equals ("+")==true) {
				        if (i==1) { //if we filled both numbers, we start to actually divide, add, substr. etc.
					     r[0]=result (r[0],r[1],task);//sets new value for r[0]
					     r[1]=new BigInteger ("0");//resets r[1]
					     task=1;//changes task
					     i=1;
					     calc="";//resets string for r[1]
					    }
					   //if we want to calculate the first operation
				   else {
				   task=1; //we set the task from 0 to 1
				   i=1; //change the number that we change
				  // f=false;
				   calc=""; //reset the string for the next number
			       }
				  }
				  else if (val.equals ("-")==true){
					       if (i==1) {
					        r[0]=result (r[0],r[1],task);
					        this.setText (r[0].toString());
					        f=false;
					         //System.out.print (result (r[0],r[1],task));
					         r[1]=new BigInteger ("0");
					         task=2;
					         i=1;
					         calc="";
					       }
				          else {
				           task=2;
				           i=1;
				           calc="";
				           //f=false;
			       }
					      }
					      
				        else if (val.equals ("*")==true){
							     if (i==1) {
					                 r[0]=result (r[0],r[1],task);
					                 
					                 this.setText (r[0].toString());
					                 i=1;
					                 r[1]=new BigInteger ("0");
					                 task=3;
					                 calc="";
					                 f=false;
					             }
					            else {
					               task=3;
					               i=1;
					              // f=false;
					               calc="";
							      }
					            }
					           else if (val.equals ("/")==true){
								      if (i==1) {
										if (r[1].toString().equals("0")==false)
					                    r[0]=result (r[0],r[1],task);
					                    this.setText (r[0].toString());
					                    i=1;
					                    r[1]=new BigInteger ("0");
					                    task=4;
					                    calc="";
					                    f=false;
					                  }
					                  else {
					                   task=4;
					                  // f=false;
					                   i=1;
					                   calc="";
								      }
					            }
			  else if (i==2) {
				   setArray ();
				   r[0]=new BigInteger (val);
				   calc=val;
				   i=0;
				  }    
			  else {
				  //number creation
			  for (int j=0;j<10;j++) {
				 z="";
				 z=z+voc.charAt(j);
			     if (z.equals (val)==true){
					 //if it is the first char, we create a new number
					    if (calc=="") {
							calc=val;
							r[i]=new BigInteger (val);
							}
							//else we multiply the number by 10 and add the new char,transformed in the number
						else  {
					            r[i]=new BigInteger (calc);
					            r[i]=r[i].multiply (t);
					            BigInteger t1=new BigInteger (val);
					            r[i]=r[i].add (t1);
					            //System.out.print (r+" ");
					            calc=r[i].toString(); 
					           }
					  }
		      }
		   }
             System.out.print (r[0]+" "+task+" "+r[1]+" ");
             if (i==2 || i==0 || val.equals ("+")==true || val.equals ("-")==true || val.equals ("*")==true || val.equals ("/")==true)
              setText (r[0].toString());
             else setText(r[1].toString());
		  }
		 public BigInteger result (BigInteger r,BigInteger r1,int task) {
			   if (task==1) {
				   return r.add (r1);
				   }
			   else if (task==2) {
				   return r.subtract (r1);
				   }
			   
			   else if (task==3) {
				   return r.multiply (r1);
				   }
			   else if (task==4  && r1.toString().equals("0")==true){
				    setArray ();
				    return (new BigInteger ("0"));
				   }
			   else if (task==4) {
				   return r.divide (r1);
				   }
			   else return r;
			 }
		}
		
	class MyButton extends Button implements ActionListener {
		MyDisplay displ;
		Integer count;
		public MyButton (int x,int y, MyDisplay displ, Integer count) {
			 super (count.toString ());
			 setLocation (x*67,75+y*67);
			 setSize (67,67);
			 addActionListener (this);
			 this.displ=displ;
			 this.count=count;
			}
		public void actionPerformed (ActionEvent ae) {
			 displ.nextOper (count.toString ());
			}
		}
		
		
	class ActionZulul extends Button implements ActionListener {
		MyDisplay displ;
		String count;
		public ActionZulul (int x,int y, MyDisplay displ, String count) {
			 super (count);
			 setLocation (x*67,75+y*67);
			 setSize (67,67);
			 addActionListener (this);
			 this.displ=displ;
			 this.count=count;
			}
		public void actionPerformed (ActionEvent ae) {
			  displ.nextOper (count);
			}
		}
     
     
    class Reset extends Button implements ActionListener {
		MyDisplay displ;
		public Reset (int x,int y, MyDisplay displ, String count) {
			 super (count);
			 setLocation (x*67,75+y*67);
			 setSize (67,67);
			 addActionListener (this);
			 this.displ=displ;
			}
		public void actionPerformed (ActionEvent ae) {
			displ.setArray ();
			}
		}

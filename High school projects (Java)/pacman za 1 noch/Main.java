import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.math.*;
interface ButtonMover {
	void moveBut (int newX,int newY);
	int getX();
	int getY();
	}
interface BotButtonMover {
	void moveBot (int newX,int newY);
	void startBotThread ();
	void interruptThread();
	}


class Main {
	 public static void main (String []v) {
		  new MyFrame ("SimplePacMan").arr();//generate new window and start the array filling method
		 }
	}
	
	
   	
class MyFrame extends Frame implements WindowListener {
     int width;
     int height;
     MyButton main_hero;
     BotButton button1;
     BotButton button2;
     BotButton button3;
     BotButton button4;
	 public MyFrame(String title) {//add new frame (window)
		 super (title);
		 setLayout(null);//создаем окно

		
		 Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
         double width = screenSize.getWidth();
         double height = screenSize.getHeight();
         
         this.width=(int)width;
         this.height=(int)height;
   
		 setSize ((int)width,(int)height);//размер
		 setLocation (0,0);
		 setBackground (new Color(23,156,200));
		 addWindowListener (this);//прослушка событий
		 setVisible (true);//включаем
		 
		 
		  MyButton main_hero=new MyButton (this,(int)(width/2),(int)(height/2));
        
         this.main_hero=main_hero;
         this.button1=new BotButton (this,75,75,"No plagiat");
         this.button2=new BotButton (this,(int)width-125,125,"Shutdown");
         this.button3=new BotButton (this,(int)width-125,(int)height-125,"C#");
         this.button4=new BotButton (this,125,(int)height-125,"Scratch");
		 }
    public void arr () {
        System.out.print ("Starting the game");
         add(main_hero);
         add(button1);
         add(button2);
         add(button3);
         add(button4); 
        button1.startBotThread();
        button2.startBotThread();
        button3.startBotThread();
        button4.startBotThread();
	}

public MyButton getHero () {
	 return main_hero;
	}     
public void gameOver() {
	setBackground (new Color (255,0,0));
	button1.interruptThread();
	button2.interruptThread();
	button3.interruptThread();
    button4.interruptThread();
    
	}
	
public void windowClosing (WindowEvent ve) {
	System.exit (0);
	}
public void windowClosed (WindowEvent vw) {
	
	}
public void windowOpened (WindowEvent vq) {
	
	}
public void windowActivated (WindowEvent vr) {
	
	}
public void windowDeactivated (WindowEvent vt) {
	
	}
public void windowIconified (WindowEvent vy) {
	
	}
public void windowDeiconified (WindowEvent vu) {
	
	}

}	
	
	
class MyButton extends Button implements KeyListener,ButtonMover{
	MyFrame win;
	int x;
	int y;
	public MyButton (MyFrame win,int x,int y) {
		 super ("Sponsors");
		 this.win=win;
		 setSize (125, 125);
		 setLocation (x,y);
		 this.x=x;
		 this.y=y;
		 setBackground (new Color (255,255,255));
		 setVisible (true);
		 addKeyListener (this);
		}
    public void moveBut (int newX,int newY) {
		setLocation (newX,newY);
		x=newX;
		y=newY;
		}

    public  void keyTyped(KeyEvent e) {
	 
   }

public void keyPressed(KeyEvent e) {
    if (e.getKeyCode()==65){
		 moveBut (x-5,y);
	    }
	 else if (e.getKeyCode()==68){
		 moveBut (x+5,y);
	    }
	    else if (e.getKeyCode()==83){
		        moveBut (x,y+5);
	          }
	           else if (e.getKeyCode()==87){
		          moveBut (x,y-5);
	              }
	              else {
                     System.out.print (e.getKeyCode()+"wow! u pressed a key!!11");
                  }
}
public void keyReleased(KeyEvent e) {
    }

public int getX () {
	return x;
	}
public int getY () {
	return y;
	}
}


class BotButton extends Button implements BotButtonMover{
	MyFrame win;
	int x;
	int y;
	MyThread mt;	
	public BotButton (MyFrame win,int x,int y,String title) {
		 super (title);
		 this.win=win;
		 setSize (125, 125);
		 setLocation (x,y);
		 this.x=x;
		 this.y=y;
		 this.mt=new MyThread (this,win);
		 setBackground (new Color (255,255,255));
		 setVisible (true);
		}
    public void moveBot (int newX,int newY) {
		setLocation (newX,newY);
		x=newX;
		y=newY;
		}
    public void startBotThread () {
		 mt.start();
		}
	public void interruptThread () {
          mt.interruptT();
		}

public int getX () {
	return x;
	}
public int getY () {
	return y;
	}
}

class MyThread extends Thread {
	BotButton button;
	MyFrame win;
	public MyThread (BotButton button,MyFrame win) {
		this.button=button;
		this.win=win;
		}
	public void run () {
		MyButton copiedHero=win.getHero();
		while (Math.abs(copiedHero.getX()-button.getX())>125 | Math.abs(copiedHero.getY()-button.getY())>125) {
		  if (copiedHero.getX()-button.getX()>0) {
			   button.moveBot(button.getX()+1,button.getY());
			  }
			 else {
				    button.moveBot(button.getX()-1,button.getY());
				 }
		  if (copiedHero.getY()-button.getY()>0) {
			   button.moveBot(button.getX(),button.getY()+1);
			  }
			 else {
				    button.moveBot(button.getX(),button.getY()-1);
				 }
		  try {
			  Thread.sleep (30);
			  }
		  catch (Exception e) {
			  }
	    }
	   win.gameOver();
	}
	public void interruptT () {
		interrupt();
		}
}

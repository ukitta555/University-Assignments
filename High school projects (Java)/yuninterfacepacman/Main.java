// В этих классах (интерфейсах) ЗАПРЕЩЕНО что-то изменять!
// На основе класса Personage объявляются классы Bot (боты) и Hero (главный
// герой)
// Метод decrement() предназначен для расчета скорости движения Персонажа
// по оси X и оси Y (поля класса dx и dy). Поэтому его следует переопределить
// для каждого из дочерних классов!
import java.util.*;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.math.*;
interface TPersonage extends Runnable {
	public void step();
	public void decrement();
}

abstract class Personage extends Panel implements TPersonage {
	int x, y, dx, dy;
	Color c;
	public Personage(int x, int y, Color c) {
		super();
		this.x = x;
		this.y = y;
		this.c = c;
		new Thread(this).start();
		setSize(50, 50);
		setLocation(x, y);
		System.out.println (x+" "+y);
		setBackground(c);
	}

	public void step() {
		x += dx;
		y += dy;
		setLocation(x, y);
	}

	public abstract void decrement();

	public void run() {
		while (true) {
			try {
				Thread.sleep(100);
			}
			catch (Exception e) {
			}
			decrement();
			step();
		}
	}
}

class Hero extends Personage implements KeyListener{
	int speedx;
	int speedy;
  public Hero (int x,int y,Color c) {
	  super (x,y,c);
	  addKeyListener (this);
	  this.speedx=speedx;
	  this.speedy=speedy;
  }
  public void decrement() {
	 dx=speedx;
	 dy=speedy;
  }
  public void keyPressed(KeyEvent e) {
	  if (e.getKeyCode()==65){
		 speedx=-2;
		 speedy=0;
	    }
	 else if (e.getKeyCode()==68){
		   speedx=2;
		   speedy=0;
	    }
	    else if (e.getKeyCode()==83){
		           speedx=0;
		           speedy=2;
	          }
	           else if (e.getKeyCode()==87){
		             speedx=0;
		             speedy=-2;
	              }
	              else {
                     System.out.print (e.getKeyCode()+"wow! u pressed a key!!");
                  }
      System.out.print (dx+" "+dy);
  }
  public void keyReleased(KeyEvent e) {
  }
  public void keyTyped(KeyEvent e) {
  }
  public int getX () {
   return x;
  }
  public int getY () {
   return y;
  }
}

class Bot extends Personage{
  Hero hero;
  public Bot (int x,int y,Color c,Hero hero) {
	  super (x,y,c);
	  this.hero=hero;
	  }
  public void decrement() {
	//   while (Math.abs(hero.getX()-x)>50 | Math.abs(hero.getY()-y)>50) {
		  if (hero.getY()-y>0) {
			    dy=1;
			  }
			 else {
				    dy=-1;
				 }
		  if (hero.getX()-x>0) {
			   dx=1;
			  }
			 else {
				    dx=-1;
				 }
	//  }
}
}
class MyFrame extends Frame implements WindowListener {
	public MyFrame () {
		super ("Pacman");
		addWindowListener (this);
		setSize (1200,800);
		setLayout (null);
		setBackground (new Color (0,0,255));
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
	public void windowOpened(WindowEvent e) {
	}
	public void windowIconified(WindowEvent e) {
	}
	public void startGame (){
	  Hero hero=new Hero (400,200,new Color (0,255,0));
	  add (hero);
	  Bot bot1=new Bot (100,100,new Color (128,0,0),hero);
	  add (bot1);
	  Bot bot2=new Bot (700,100,new Color (255,0,0),hero);
	  add (bot2);
	  Bot bot3=new Bot (700,500,new Color (255,0,0),hero);
	  add (bot3);
	  Bot bot4=new Bot (100,500,new Color (255,0,0),hero);
	  add (bot4);
	}
}
class Main {
	public static void main (String [] argv) {
		System.out.print ("haha");
		new MyFrame().startGame ();
		}
	}

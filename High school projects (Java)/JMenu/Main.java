import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class Main {
	public static void main (String [] argv) {
		  new MyFrame ("JMenuWindow");
		}
	}
class MyFrame extends JFrame implements ActionListener {
	public MyFrame (String title){
		 super (title);
		 setSize (1000,700);
		 setLocation (200,100);
		 Container c=getContentPane ();
		 c.setBackground (new Color (0,255,0));
		 c.setLayout (new FlowLayout ());
		 JMenuBar bar = new JMenuBar ();
		 JMenu countries = new JMenu ("countries");
		 JMenuItem russia= new JMenuItem ("vodka");
		 JMenuItem  ukraine =new JMenuItem ("salo");
		 JMenuItem hungary=new JMenuItem ("budapest");
		 russia.addActionListener (this);
		 ukraine.addActionListener (this);
		 hungary.addActionListener (this);
		 setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
		 countries.add (russia);
		 countries.add (ukraine);
		 countries.add (hungary);
		 bar.add (countries);
		 c.add (bar);
		 setVisible (true);
		}
	 public void actionPerformed (ActionEvent ae) {
		 JOptionPane.showMessageDialog (null,((JMenuItem)(ae.getSource())).getText ());
		 }
	}

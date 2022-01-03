import java.awt.Graphics;
import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

class Window  {
public static void main (String [] argv) {
	  Pepe p=new Pepe (); 
	  p.loadImage ("kek.jpg");
	  p.drawIcon ();
	}
}
class Pepe extends JFrame{
	 public int width = 1000;
     public int height = 800;
     public Image img;
     
public void loadImage(String src) {
	setSize(width, height);
    setTitle("File Monitor:D");
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setLocationRelativeTo(null);
    setResizable(false);
    setVisible(true);
    this.img=img;
    this.width=width;
    this.height=height;
    img = new ImageIcon(src).getImage();
}

public void drawIcon() {
    Graphics g = getGraphics();
    g.drawImage(img, 0, 0, null);
}
	}


import java.awt.*;
import java.awt.event.*;
import java.util.Random;
class Main{
    public static void main(String [] argv){
        Frame window = new MyFrame("НедоCalculator");
    }
}
class MyFrame extends Frame{
    BDisplay bd;
    BEquals bequals;
    BCif bcif;
    BPlus bplus;
    BMinus bminus;
    BTimes btimes;
    BDivide bdivide;
    BClear bclear;
    public MyFrame (String title){
        super(title);
        setSize(300,600);
        setLocation(200,100);
        setLayout(null);
        setBackground(Color.white);
        add (bd = new BDisplay(""));
        add (bcif = new BCif("1", bd, 0, 120));
        add (bcif = new BCif("2", bd, 75, 120));
        add (bcif = new BCif("3", bd, 150, 120));
        add (bcif = new BCif("4", bd, 0, 240));
        add (bcif = new BCif("5", bd, 75, 240));
        add (bcif = new BCif("6", bd, 150, 240));
        add (bcif = new BCif("7", bd, 0, 360));
        add (bcif = new BCif("8", bd, 75, 360));
        add (bcif = new BCif("9", bd, 150, 360));
        add (bcif = new BCif("0", bd, 75, 480));
        add (bplus = new BPlus("+", bd, 225, 120));
        add (bminus = new BMinus("-", bd, 225, 240));
        add (btimes = new BTimes("*", bd, 225, 360));
        add (bdivide = new BDivide("/", bd, 225, 480));
        add (bclear = new BClear("Clear", bd, 0, 480));
        add (bequals = new BEquals("=", bd, 150, 480));
        addWindowListener (new MyWindowAdapter());
        setVisible(true);
    }
}

class MyWindowAdapter extends WindowAdapter{
    public void windowClosing (WindowEvent we){
        System.exit(0);
    }
    public void windowClosed (WindowEvent we){
    }
    public void windowOpened (WindowEvent we){
    }
    public void windowActivated (WindowEvent we){
    }
    public void windowDeactivated (WindowEvent we){
    }
    public void windowIconified (WindowEvent we){
    }
    public void windowDeiconified (WindowEvent we){
    }
}

class BDisplay extends Label{
    int memory;
    int currentop;
    boolean fop;
    int present;
    int numberop;
    public BDisplay (String title){
        super(title);
        fop = false;
        setAlignment (BDisplay.CENTER);
        memory = 0;
        numberop = 1;
        setSize(300,120);
        setBackground(new Color(190,225,237));
        setLocation(0,0);
        setVisible(true);
    }
    public void changeFlagPositive(){
        fop = true;
    }
    public void changeFlagNegative(){
        fop = false;
    }
    public void changettl(String title){
        if (fop == true){
            setText(title);
            changeFlagNegative();
        }
        else
            setText(getText()+title);
    }
    public void clear(){
        setText("");
        memory = 0;
    }
    public void displayEquals(){
        if (currentop == 1){
            int present = Integer.parseInt(getText());
            memory = memory + present;
            setText("");
            String lbl = String.valueOf(memory);
            setText(lbl);
            present=0;
            currentop = 0;

        }
        if (currentop == 2){
            int present = Integer.parseInt(getText());
            memory = memory - present;
            setText("");
            String lbl = String.valueOf(memory);
            setText(lbl);
            currentop = 0;
            present=0;
        }
        if (currentop == 3){
            int present = Integer.parseInt(getText());
            memory = memory * present;
            setText("");
            String lbl = String.valueOf(memory);
            setText(lbl);
            currentop = 0;
            present=0;
        }
        if (currentop == 4){
            int present = Integer.parseInt(getText());
            memory = memory / present;
            setText("");
            String lbl = String.valueOf(memory);
            setText(lbl);
            currentop = 0;
            present=0;
        }
        changeFlagPositive();
    }
    public void summ(){
        //memory = 0;
       
        if (memory != 0 && currentop==0){
            present = Integer.parseInt(getText());
            memory = memory + present;
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 1;
        } else{
            memory = Integer.parseInt(getText());
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 0;
        }



    }
    public void minus(){
        /*if (numberop != 1){
            present = Integer.parseInt(getText());
            memory = memory - present;
            numberop+=1;
            String lbl = String.valueOf(memory);
            setText(lbl);
            changeFlagPositive();

        } else{
            memory = Integer.parseInt(getText());
            numberop+=1;
            String lbl = String.valueOf(memory);
            setText(lbl);
            changeFlagPositive();
        }*/
        //memory = 0;
          if (memory != 0 && currentop==0){
            present = Integer.parseInt(getText());
            memory = memory - present;
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 2;
        } else{
            memory = Integer.parseInt(getText());
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 0;
        }
	}
    public void times(){
           if (memory != 0 && currentop==0){
            present = Integer.parseInt(getText());
            memory = memory * present;
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 3;
        } else{
            memory = Integer.parseInt(getText());
            String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
        // numberop+=1;
        currentop = 0;
        }


    }
    public void divide(){
        int present = Integer.parseInt(getText());
        currentop = 4;
        memory = memory / present;
        String lbl = String.valueOf(memory);
        setText(lbl);
        changeFlagPositive();
    }

}

class BCif extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BCif(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.changettl(getLabel());
    }
}

class BPlus extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BPlus(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.summ();
    }
}

class BMinus extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BMinus(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.minus();
    }
}

class BTimes extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BTimes(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.times();
    }
}

class BDivide extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BDivide(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.divide();
    }
}

class BClear extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BClear(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.clear();
    }
}


class BEquals extends Button implements ActionListener{
    BDisplay bd;
    int x;
    int y;
    public BEquals(String title, BDisplay bd, int x, int y){
        super(title);
        this.bd = bd;
        this.x = x;
        this.y = y;
        setLocation(x, y);
        setSize(75, 120);
        setBackground(new Color(245,166,227));
        addActionListener(this);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        bd.displayEquals();
    }
}

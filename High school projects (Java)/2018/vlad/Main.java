import javax.swing.*;
import java.awt.*;
import java.util.List;
import java.util.ArrayList;
import java.awt.geom.*;
import java.awt.image.BufferedImage;
import java.awt.event.*;
import javax.swing.event.*;

class Main{
    public static void main(String[] args) {
       new MyFrame ("kek");    //oop пацаны
    }
}
//вектор
class Vertex {
    double x;
    double y;
    double z;
    double w;
    Vertex(double x, double y, double z, double w) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.w = w;
    }
}
//треугольник, состоит из 3 векторов
class Triangle {
    Vertex v1;
    Vertex v2;
    Vertex v3;
    Color color;
    Triangle(Vertex v1, Vertex v2, Vertex v3, Color color) {
        this.v1 = v1;
        this.v2 = v2;
        this.v3 = v3;
        this.color = color;
    }
}
//матрица
class Matrix4 {
    double[] values;
    Matrix4(double[] values) {
        this.values = values;
    }
    Matrix4 multiply(Matrix4 other) {
        double[] result = new double[16];//аналог матрицы в одномерном массиве
        for (int row = 0; row < 4; row++) { //счет строк
            for (int col = 0; col < 4; col++) { //счет столбцов
                for (int i = 0; i < 4; i++) { //счетчик для подсчета результата (см. статью/учебник)
                    result[row * 4 + col] +=
                        this.values[row * 4 + i] * other.values[i * 4 + col]; //подсчет конечной матрицы
                }
            }
        }
        return new Matrix4(result); // возврщаем полученную матрицу
    }
    Vertex transform(Vertex in) {  //подсчет нового вектора на основе матриц, которые считаются предыдущим методом
        return new Vertex(
                          in.x * values[0] + in.y * values[4] + in.z * values[8] + in.w * values[12],
                          in.x * values[1] + in.y * values[5] + in.z * values[9] + in.w * values[13],
                          in.x * values[2] + in.y * values[6] + in.z * values[10] + in.w * values[14],
                          in.x * values[3] + in.y * values[7] + in.z * values[11] + in.w * values[15]
                          );
    }
}

class MyFrame extends JFrame implements KeyListener{
    MyJPanel renderPanel;
    int headingSlider;
    int rollSlider;
    int pitchSlider;
    int width;
    int height;
    public MyFrame (String s) { //переделанный под ООП вариант нашего окна
        super ("wi");
        Container pane = getContentPane(); //контейнер для изображения
        pane.setLayout(new BorderLayout());
        this.headingSlider=45;
        this.pitchSlider=0;
        this.rollSlider=0;
        addKeyListener (this);
        // panel to display render results
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        double width = screenSize.getWidth();
        double height = screenSize.getHeight();
        //cтавим курсор в центр экрана
        try {
             Robot robot = new Robot();
             robot.mouseMove((int)(width/2),(int)(height/2));
	        }
	    catch (Exception ex) {}
	    // передаем все слайдеры чтобы Джава не ругалась на статик
        renderPanel = new MyJPanel(headingSlider,pitchSlider,rollSlider,(int)(width/2),(int)(height/2)); 
        pane.add(renderPanel, BorderLayout.CENTER);
        setSize((int)width, (int)height);
        setVisible(true);
    }
     
public  void keyTyped(KeyEvent e) {
    }
public void keyPressed(KeyEvent e) {
    if (e.getKeyCode ()==39) {
     renderPanel.subtractHeading();
     renderPanel.subtractDeltaX ();
     renderPanel.rightRelativeChangeToFoV();
 }
     
    if (e.getKeyCode ()==38)
     renderPanel.addFoV();
      
    if (e.getKeyCode ()==37) {
     renderPanel.addHeading();
     renderPanel.addDeltaX ();
     renderPanel.leftRelativeChangeToFoV();
    }
     
    if (e.getKeyCode ()==40)
     renderPanel.subtractFoV();
     
     renderPanel.repaint();
    }    
public void keyReleased(KeyEvent e) {
    }



}


//жи есть пенел, черная магия происходит прямо здесь
class MyJPanel extends JPanel implements MouseMotionListener{
	List<Figure> figures;
    double headingSlider; //слайдеры
    double pitchSlider;
    double rollSlider;
    int deltaX;
    int deltaY;
    int deltaXSpin;
    int finXMotion=0;
    int finYMotion=0;
    int screenHeight;
    int screenWidth;
    double changeAngle;
    public MyJPanel (double headingSlider, double pitchSlider,double rollSlider,int deltaX,int deltaY) {
    //конструктор, ничего необычного
     this.figures = new ArrayList<>();
     this.headingSlider=headingSlider;
     this.rollSlider=rollSlider;
     this.pitchSlider=pitchSlider;
     this.deltaX=deltaX;
     this.deltaY=deltaY;
     this.screenHeight=deltaY*2;
     this.screenWidth=deltaX*2;
     this.deltaXSpin=0;
     this.changeAngle=(double) (7.0*90.0/screenWidth);    // расчет поворота кубика за 1 операцию сдвига
     addMouseMotionListener (this);
     createObjects();
    }
//отрисовка
public void paint(Graphics g) {
	                //System.out.print (nablaX+" "+nablaY);
                    Graphics2D g2 = (Graphics2D) g;
                    g2.setColor(Color.GRAY);
                    g2.fillRect(0, 0, getWidth(), getHeight());//заполнение экрана
                   
         
                    double heading = Math.toRadians(headingSlider); // получаем значение слайдера, переводим в радианы
                    Matrix4 headingTransform = new Matrix4(new double[] {
                            Math.cos(heading), 0, -Math.sin(heading), 0,
                            0, 1, 0, 0,
                            Math.sin(heading), 0, Math.cos(heading), 0,
                            0, 0, 0, 1
                            });   //матрица поворота 1
                    double pitch = Math.toRadians(pitchSlider);  //повторяем, создаем 2 матрицу
                    Matrix4 pitchTransform = new Matrix4(new double[] {  
                            1, 0, 0, 0,
                            0, Math.cos(pitch), Math.sin(pitch), 0,
                            0, -Math.sin(pitch), Math.cos(pitch), 0,
                            0, 0, 0, 1
                            });
                    double roll = Math.toRadians(rollSlider); //повторяем, создаем 3 матрицу
                    Matrix4 rollTransform = new Matrix4(new double[] {
                            Math.cos(roll), -Math.sin(roll), 0, 0,
                            Math.sin(roll), Math.cos(roll), 0, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 1
                           });
                    Matrix4 panOutTransform = new Matrix4(new double[] { //повторяем, создаем 4 матрицу
                            1, 0, 0, 0,                                  
                            0, 1, 0, 0,
                            0, 0, 1, 0,
                            0, 0, -400, 1 //все еще не знаю как это работает
                        });
                    Matrix4 transform =
                        headingTransform
                        .multiply(pitchTransform)
                        .multiply(rollTransform)
                        .multiply(panOutTransform); //перемножаем матрицы, чтобы описывать все движение одной финальной матрицей.

                    BufferedImage img = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_ARGB); // превращаем наше окно в картинку (растеризированную)

                    double[] zBuffer = new double[img.getWidth() * img.getHeight()];
                    // initialize array with extremely far away depths
                    for (int q = 0; q < zBuffer.length; q++) {
                        zBuffer[q] = Double.NEGATIVE_INFINITY;
                    }
                    for (Figure z : figures) {
                      for (Triangle t : z.polygons) {
                        Vertex v1 = transform.transform(t.v1); //получаем новые вектора
                        Vertex v2 = transform.transform(t.v2);
                        Vertex v3 = transform.transform(t.v3);
                        
                        double fovAngle = Math.toRadians(z.getFoV()); //получаем значение области зрения
                        double fov = Math.tan (fovAngle/2)*170; // переменная, описывающая как сильно будет увеличиваться наша каритнка. больше множитель - больше кайфа.

                         //машстабирвоание, скорее всего связано  с той самой матрицей
                        v1.x = v1.x / (-v1.z) * fov;
                        v1.y = v1.y / (-v1.z) * fov;
                        v2.x = v2.x / (-v2.z) * fov;
                        v2.y = v2.y / (-v2.z) * fov;
                        v3.x = v3.x / (-v3.z) * fov;
                        v3.y = v3.y / (-v3.z) * fov;
                          //сдвиг куба, без него он был бы в начале координатной плоскости, как мы и думали
                        v1.x += deltaX+deltaXSpin;
                        v1.y += deltaY;
                        v2.x += deltaX+deltaXSpin;
                        v2.y += deltaY;
                        v3.x += deltaX+deltaXSpin;
                        v3.y += deltaY;
                        
                          //процесс зет буферизации. поиск минимальных  и максимальных координат  треугольника
                        int minX = (int) Math.max(0, Math.ceil(Math.min(v1.x, Math.min(v2.x, v3.x))));
                        int maxX = (int) Math.min(img.getWidth() - 1, Math.floor(Math.max(v1.x, Math.max(v2.x, v3.x))));
                        int minY = (int) Math.max(0, Math.ceil(Math.min(v1.y, Math.min(v2.y, v3.y))));
                        int maxY = (int) Math.min(img.getHeight() - 1, Math.floor(Math.max(v1.y, Math.max(v2.y, v3.y))));
                         //расчет площади нашего 2D треугольника * 2(так надо по следующей формуле)
                        double triangleArea = (v1.y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - v1.x);
                         // расчет барицентрических координат
                        for (int y = minY; y <= maxY; y++) { //полный перебор все возможных координат для данного треугольника
                            for (int x = minX; x <= maxX; x++) {
                                double b1 = ((y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - x)) / triangleArea; //1 координата
                                double b2 = ((y - v1.y) * (v3.x - v1.x) + (v3.y - v1.y) * (v1.x - x)) / triangleArea;//2 координата
                                double b3 = ((y - v2.y) * (v1.x - v2.x) + (v1.y - v2.y) * (v2.x - x)) / triangleArea; //3 координата
                                if (b1 >= 0 && b1 <= 1 && b2 >= 0 && b2 <= 1 && b3 >= 0 && b3 <= 1) { //т.к. все точки, которые нахожятся внутри треугольника, должны иметь барицентрированные координаты, котоыре меньше 0 и больше 1, вводится данная проверка
                                    double depth = b1 * v1.z + b2 * v2.z + b3 * v3.z; //расчет текущей "глубины" пикселя
                                    int zIndex = y * img.getWidth() + x; //уникальный зет индекс для данного пикселя, другого такого не найдешь
                                    if (zBuffer[zIndex] < depth) {//если  глубина пикселя больше, то он находится ближе, значит рисовать будем
                                        img.setRGB(x, y, getShade(t.color, 1).getRGB());
									      
                                        zBuffer[zIndex] = depth; //в зет буфер данного пикселя записываем новое значение глубины, чтобы при пересчете только пиксель, лежащий выше, был перерисован
                                    }
                                }
                            }
                        }
                    }
                  }
           g2.drawImage(img, 0, 0, null);
       }
    //управление полями класса из MyFrame
     public void addHeading () {
		if (deltaX+deltaXSpin>0 && deltaX+deltaXSpin<screenWidth)
		  headingSlider+=changeAngle;
        }
     public void subtractHeading () {
		if ( deltaX+deltaXSpin>0 && deltaX+deltaXSpin<screenWidth)
         headingSlider-=changeAngle;
        }
     public void addDeltaX () {
         deltaX+=7;
         }
     public void subtractDeltaX () {
         deltaX-=7;
         }
     public void addDeltaY () {
         deltaY+=7;
         }
     public void subtractDeltaY () {
         deltaY-=7;
         }
         
     public void addDeltaXSpin () {
		if (deltaXSpin>screenWidth*2)
		  deltaXSpin=(-1)*(screenWidth*2);
           deltaXSpin+=7;
         }
     public void subtractDeltaXSpin () {
		 if (deltaXSpin<-(screenWidth*2))
		  deltaXSpin=screenWidth*2;
         deltaXSpin-=7;
         }
         
         
     //пeреопределние методов для расчета сдвига курсора 
     
        
 public void mouseDragged(MouseEvent e)  {
		      finXMotion=(int)e.getLocationOnScreen().getX();
	          finYMotion=(int)e.getLocationOnScreen().getY();
	          int deltaXMotion=finXMotion-(int)(screenWidth/2);
	          int deltaYMotion=finYMotion-(int)(screenHeight/2);
			  removeMouseMotionListener (this);
			  try {
             Robot robot = new Robot();
             robot.mouseMove((int)(screenWidth/2),(int)(screenHeight/2));
             //Thread.sleep (1000);
             
	          }
	        catch (Exception ex) {}
	        if (deltaYMotion>0) {
				   for (int i=0;i<Math.abs(deltaYMotion);i++) {
					     subtractDeltaY();
					     repaint ();
					   }
				  }
				  else if (deltaYMotion<0) {
					    for (int i=0;i<Math.abs(deltaYMotion);i++) {
					     addDeltaY();
					     repaint ();
					    }
					  }
			   if (deltaXMotion>0) {
				   for (int i=0;i<Math.abs(deltaXMotion);i++) {
					     subtractDeltaX();
					     repaint ();
					   }
				  }
				  else if (deltaXMotion<0) {
					    for (int i=0;i<Math.abs(deltaXMotion);i++) {
					     addDeltaX();
					     repaint ();
					     
					    }
					}
	       addMouseMotionListener (this);
   	 }
   	 
public void mouseMoved(MouseEvent e)  {
	 finXMotion=(int)e.getLocationOnScreen().getX();
	          finYMotion=(int)e.getLocationOnScreen().getY();
	          int deltaXMotion=finXMotion-(int)(screenWidth/2);
	          int deltaYMotion=finYMotion-(int)(screenHeight/2);
			  removeMouseMotionListener (this);
			  try {
             Robot robot = new Robot();
             robot.mouseMove((int)(screenWidth/2),(int)(screenHeight/2));
	          }
	        catch (Exception ex) {}
	        if (deltaYMotion>0) {
				   for (int i=0;i<Math.abs(deltaYMotion);i++) {
					     subtractDeltaY();
					     repaint ();
					   }
				  }
				  else if (deltaYMotion<0) {
					    for (int i=0;i<Math.abs(deltaYMotion);i++) {
					     addDeltaY();
					     repaint ();
					    }
					  }
			   if (deltaXMotion>0) {
				   for (int i=0;i<Math.abs(deltaXMotion);i++) {
					     subtractDeltaXSpin();
					     repaint ();
					   }
				  }
				  else if (deltaXMotion<0) {
					    for (int i=0;i<Math.abs(deltaXMotion);i++) {
					     addDeltaXSpin();
					     repaint ();
					     
					    }
					}
	       addMouseMotionListener (this);
   	 }

 
    
public void addFoV () {
		        for (Figure z : figures) {
				  z.addFoV ();			
				}
     }
public void subtractFoV () {
		     for (Figure z : figures) {  
			    z.subtractFoV (); 
			 }
     }
public void rightRelativeChangeToFoV () {
	   for (Figure z:figures) {
		     double maximal=0;
		     double minimal=0;
		     for (Triangle t:z.polygons) {
				 if (t.v1.x>t.v2.x)
				     {
				      maximal=t.v1.x;
					  minimal=t.v2.x;
				     }
				 else
				     {
					  maximal=t.v2.x;
					  minimal=t.v1.x;
				     } 
				 if (t.v3.x>maximal)
				    maximal=t.v3.x;
				 else if (t.v3.x<minimal)
				        minimal=t.v3.x;
				 }
			 int average;
			  minimal+=deltaX+deltaXSpin;
		     maximal+=deltaX+deltaXSpin;
			 average=(int)((minimal+maximal)/2);
			  System.out.print (average+" ");
			 if (average>(screenWidth/2+200)) {
				   z.addFoV ();
				 }
			  else {z.subtractFoV ();}
		   }
	}
public void leftRelativeChangeToFoV () {
	   for (Figure z:figures) {
		     double maximal=0;
		     double minimal=0;
		     int average;
		     for (Triangle t:z.polygons) {
				 if (t.v1.x>t.v2.x)
				     {
				      maximal=t.v1.x;
					  minimal=t.v2.x;
				     }
				 else
				     {
					  maximal=t.v2.x;
					  minimal=t.v1.x;
				     } 
				 if (t.v3.x>maximal)
				    maximal=t.v3.x;
				 else if (t.v3.x<minimal)
				        minimal=t.v3.x;
				    
				 }
		     minimal+=deltaX+deltaXSpin;
		     maximal+=deltaX+deltaXSpin;
			 average=(int)((minimal+maximal)/2);
			 System.out.print (average+" ");
			 if (average>(screenWidth/2+200)) {
				   z.subtractFoV ();
				
				 }
			  else {z.addFoV ();
				  }
		   }
		   
	}
 
     public Color getShade(Color color, double shade) {
		shade=1;
        double redLinear = Math.pow(color.getRed(), 2.4) * shade;
        double greenLinear = Math.pow(color.getGreen(), 2.4) * shade;
        double blueLinear = Math.pow(color.getBlue(), 2.4) * shade;

        int red = (int) Math.pow(redLinear, 1/2.4);
        int green = (int) Math.pow(greenLinear, 1/2.4);
        int blue = (int) Math.pow(blueLinear, 1/2.4);

        return new Color(red, green, blue);
    }
    
public void createObjects() {
                        List<Triangle> tris1 = new ArrayList<>(); //вектор треугольников, которые состоят из векторов (костыль №4)
                                                 
					
                    //A
                    tris1.add(new Triangle(new Vertex(-100, 100, 100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          Color.WHITE));
                    //B
                    tris1.add(new Triangle(new Vertex(100, 100, 100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          Color.WHITE));
                    //C
                    tris1.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          Color.WHITE));
                    //D
                    tris1.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          Color.WHITE));
                    //E
                    tris1.add(new Triangle(new Vertex(-100, -100, 100, 1),
                                          new Vertex(100, -100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          Color.WHITE));

                    //F
                    tris1.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          Color.WHITE));
                    //G
                    tris1.add(new Triangle(new Vertex(-100, -100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //H
                    tris1.add(new Triangle(new Vertex(-100, 100, 100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //I
                    tris1.add(new Triangle(new Vertex(-100, 100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
										  new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //J
                    tris1.add(new Triangle(new Vertex(-100, -100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          Color.WHITE));
                    //K
                    tris1.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(-100, -100, 100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //L
                    tris1.add(new Triangle(new Vertex(-100, -100, -100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          new Vertex(100, -100, 100, 1),
                                          Color.WHITE));
                                          
                            
                    figures.add(new Figure(tris1,100));                      
 List<Triangle> tris = new ArrayList<>(); //вектор треугольников, которые состоят из векторов (костыль №4)
                    
                    
                    
                     
                    //scene A

                    tris.add(new Triangle(new Vertex(-200, 200, -200, 1),
                                          new Vertex(200, 200, -200, 1),
                                          new Vertex(-200, -200, -200, 1),
                                          Color.WHITE));
                                                

                    tris.add(new Triangle(new Vertex(-200, -200, -200, 1),
                                          new Vertex(200, 200, -200, 1),
                                          new Vertex(200, -200, -200, 1),
                                          Color.WHITE));
                                          
                                          
                   //scene B 
                    tris.add(new Triangle(new Vertex(-200, 200, 200, 1),
                                          new Vertex(200, 200, 200, 1),
                                          new Vertex(-200, 200, -200, 1),
                                          Color.RED));
                    
                    tris.add(new Triangle(new Vertex(200, 200, 200, 1),
                                          new Vertex(200, 200, -200, 1),
                                          new Vertex(-200, 200, -200, 1),
                                          Color.RED));
                                          
                   //scene C
                     
                    tris.add(new Triangle(new Vertex(200, -200, 200, 1),
                                          new Vertex(200, 200, -200, 1),
                                          new Vertex(200, 200, 200, 1),
                                          new Color (255,93,93)));
                   
                    tris.add(new Triangle(new Vertex(200, -200, 200, 1),
                                          new Vertex(200, -200, -200, 1),
                                          new Vertex(200, 200, -200, 1),
                                          new Color (255,93,93)));
                                          
                                          
                    figures.add(new Figure(tris,100));
                    

  }
  
   }
class Figure {
  double scale;
  List<Triangle> polygons;
  
  public Figure(List<Triangle> polygons,double scale) {
	 this.polygons=polygons;
	 this.scale=scale;
  }
  public void addFoV () {
		if  (scale+1 <= 180)
         scale+=0.2;
         }
     public void subtractFoV () {
		if (scale-1>=0)
         scale-=0.2;
         }
  public double getFoV () {
	   return scale;
	  }
}

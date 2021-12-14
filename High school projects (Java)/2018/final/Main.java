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
    new MyFrame ("anime");    //Создание окна
  }
}

//Класс векторов
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

//Полигон
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

//Матрицы поворта
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
            result[row * 4 + col] += this.values[row * 4 + i] * other.values[i * 4 + col]; //подсчет конечной матрицы
          }
        }
      }
    return new Matrix4(result); // возврщаем полученную матрицу
  }

  Vertex transform(Vertex in) {  //подсчет нового вектора на основе матриц, которые считаются предыдущим методом
    return new Vertex(in.x * values[0] + in.y * values[4] + in.z * values[8] + in.w * values[12],
                      in.x * values[1] + in.y * values[5] + in.z * values[9] + in.w * values[13],
                      in.x * values[2] + in.y * values[6] + in.z * values[10] + in.w * values[14],
                      in.x * values[3] + in.y * values[7] + in.z * values[11] + in.w * values[15]);
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
    super ("123");
    Container pane = getContentPane(); //контейнер для изображения
    pane.setLayout(new BorderLayout());
    this.headingSlider = 0;
    this.pitchSlider = 0;
    this.rollSlider = 0;
    addKeyListener (this);
    Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
    double width = screenSize.getWidth();
    double height = screenSize.getHeight();
    //Cтавим курсор в центр экрана
    try {
      Robot robot = new Robot();
      robot.mouseMove((int)(width / 2), (int)(height / 2));
	} catch (Exception ex) {}
	makeCursorTransparent();
    renderPanel = new MyJPanel(headingSlider, pitchSlider, rollSlider, (int)(width / 2), (int)(height / 2));
    pane.add(renderPanel, BorderLayout.CENTER);
    setSize((int)width, (int)height);
    setVisible(true);
  }

  public  void keyTyped(KeyEvent e) {
  }

  public void keyPressed(KeyEvent e) {
    if (e.getKeyCode() == 82)
      renderPanel.resetValues();
    if (e.getKeyCode()==39 | e.getKeyCode()==68) {
      renderPanel.subtractHeading();
      renderPanel.subtractDeltaX ();
      renderPanel.rightRelativeChangeToFoV();
    }
    if (e.getKeyCode() == 38 | e.getKeyCode() == 87)
      renderPanel.addFoV(1);
    if (e.getKeyCode() == 37 | e.getKeyCode() == 65) {
      renderPanel.addHeading();
      renderPanel.addDeltaX ();
      renderPanel.leftRelativeChangeToFoV();
    }
    if (e.getKeyCode() == 40 | e.getKeyCode() == 83)
      renderPanel.subtractFoV(1);
    renderPanel.repaint();
  }

  public void keyReleased(KeyEvent e) {
  }

  public void makeCursorTransparent() {
    BufferedImage cursorImg = new BufferedImage(16, 16, BufferedImage.TYPE_INT_ARGB);
    Cursor blankCursor = Toolkit.getDefaultToolkit().createCustomCursor(cursorImg, new Point(0, 0), "blank cursor");
    getContentPane().setCursor(blankCursor);
  }
}


//Тут панель где магия происходит прямо здесь
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

  public MyJPanel (double headingSlider, double pitchSlider, double rollSlider, int deltaX, int deltaY) {
    this.figures = new ArrayList<>();
    this.headingSlider = headingSlider;
    this.rollSlider = rollSlider;
    this.pitchSlider = pitchSlider;
    this.deltaX = deltaX;
    this.deltaY = deltaY;
    this.screenHeight = deltaY * 2;
    this.screenWidth = deltaX * 2;
    this.deltaXSpin = 0;
    this.changeAngle = (double)(7.0 * 90.0 / screenWidth);
    addMouseMotionListener(this);
    createObjects();
  }

  //Рендер
  public void paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    g2.setColor(new Color (255,163,239));
    g2.fillRect(0, 0, getWidth(), getHeight());
    g2.setColor(Color.WHITE);
    g2.drawLine ((screenWidth/2),0,(screenWidth/2),screenHeight);
    g2.drawLine (0,(screenHeight/2),screenWidth,(screenHeight/2));
    double heading = Math.toRadians(headingSlider);
    Matrix4 headingTransform = new Matrix4(new double[] {
      Math.cos(heading), 0, -Math.sin(heading), 0,
      0, 1, 0, 0,
      Math.sin(heading), 0, Math.cos(heading), 0,
      0, 0, 0, 1
    });   //матрица поворота 1
    double pitch = Math.toRadians(pitchSlider);
    Matrix4 pitchTransform = new Matrix4(new double[] {
      1, 0, 0, 0,
      0, Math.cos(pitch), Math.sin(pitch), 0,
      0, -Math.sin(pitch), Math.cos(pitch), 0,
      0, 0, 0, 1
    });
    double roll = Math.toRadians(rollSlider);
    Matrix4 rollTransform = new Matrix4(new double[] {
      Math.cos(roll), -Math.sin(roll), 0, 0,
      Math.sin(roll), Math.cos(roll), 0, 0,
      0, 0, 1, 0,
      0, 0, 0, 1
    });
    Matrix4 panOutTransform = new Matrix4(new double[] {
      1, 0, 0, 0,
      0, 1, 0, 0,
      0, 0, 1, 0,
      0, 0, -600, 1
    });
    Matrix4 transform = headingTransform.multiply(pitchTransform).multiply(rollTransform).multiply(panOutTransform); //Создание финальной матрицы
    BufferedImage img = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_ARGB);
    double[] zBuffer = new double[img.getWidth() * img.getHeight()];
    for (int q = 0; q < zBuffer.length; q++) {
      zBuffer[q] = Double.NEGATIVE_INFINITY;
    }
    for (Figure z : figures) {
      for (Triangle t : z.polygons) {
        Vertex v1 = transform.transform(t.v1);
        Vertex v2 = transform.transform(t.v2);
        Vertex v3 = transform.transform(t.v3);
        double fovAngle = Math.toRadians(z.getFoV());
        double fov = Math.tan (fovAngle/2)*85;
        v1.x = v1.x / (-v1.z) * fov;
        v1.y = v1.y / (-v1.z) * fov;
        v2.x = v2.x / (-v2.z) * fov;
        v2.y = v2.y / (-v2.z) * fov;
        v3.x = v3.x / (-v3.z) * fov;
        v3.y = v3.y / (-v3.z) * fov;
        v1.x += deltaX+deltaXSpin;
        v1.y += deltaY;
        v2.x += deltaX+deltaXSpin;
        v2.y += deltaY;
        v3.x += deltaX+deltaXSpin;
        v3.y += deltaY;
        Vertex ab = new Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z, v2.w - v1.w);
        Vertex ac = new Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z, v3.w - v1.w);
        Vertex norm = new Vertex(ab.y * ac.z - ab.z * ac.y,
                                 ab.z * ac.x - ab.x * ac.z,
                                 ab.x * ac.y - ab.y * ac.x, 1);
        double normalLength = Math.sqrt(norm.x * norm.x + norm.y * norm.y + norm.z * norm.z); //нашли его длину
        norm.z /= normalLength; // якась формула из статьи
        double angleCos = Math.abs(norm.z); // легко видеть, что косинус это ответ на все вопросы математики
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

  public void addHeading () {
    if (deltaX + deltaXSpin + 200 > 0 && deltaX + deltaXSpin - 200 < screenWidth)
	  headingSlider += changeAngle;
  }

  public void subtractHeading () {
    if (deltaX + deltaXSpin + 200 > 0 && deltaX + deltaXSpin - 200 < screenWidth)
      headingSlider -= changeAngle;
  }

  public void addDeltaX () {
    deltaX += 7;
  }

  public void subtractDeltaX () {
    deltaX -= 7;
  }

  public void addDeltaY () {
    deltaY += 1;
  }

  public void subtractDeltaY () {
    deltaY -= 1;
  }

  public void addDeltaXSpin () {
    if ((deltaXSpin + deltaX > 0) && (deltaXSpin + deltaX < screenWidth) && (deltaXSpin > (screenWidth * 2)))
	  deltaX += screenWidth * 4;
	if (deltaXSpin > screenWidth * 2)
	  deltaXSpin = (-1) * (screenWidth * 2);
      deltaXSpin += 1;
  }

  public void subtractDeltaXSpin () {
    if ((deltaXSpin + deltaX > 0) && (deltaXSpin + deltaX < screenWidth) && (deltaXSpin < -(screenWidth * 2)))
	  deltaX -= screenWidth * 4;
	if (deltaXSpin < -(screenWidth * 2))
	  deltaXSpin = screenWidth * 2;
    deltaXSpin -= 1;
  }
  public void mouseDragged(MouseEvent e)  {
    finXMotion = (int)e.getLocationOnScreen().getX();
	finYMotion = (int)e.getLocationOnScreen().getY();
	int deltaXMotion = finXMotion - (int)(screenWidth / 2);
	int deltaYMotion = finYMotion - (int)(screenHeight / 2);
	removeMouseMotionListener(this);
	try {
      Robot robot = new Robot();
      robot.mouseMove((int)(screenWidth / 2), (int)(screenHeight / 2));
	} catch (Exception ex) {}
	if (deltaYMotion > 0) {
	  for (int i = 0; i < Math.abs(deltaYMotion); i ++) {
	    subtractDeltaY();
		repaint();
	  }
	} else if (deltaYMotion < 0) {
	  for (int i = 0; i < Math.abs(deltaYMotion); i ++) {
	    addDeltaY();
		repaint();
	  }
	}
	if (deltaXMotion > 0) {
	  for (int i = 0; i < Math.abs(deltaXMotion); i ++) {
	    subtractDeltaXSpin();
	    repaint();
	  }
	} else if (deltaXMotion < 0) {
	  for (int i = 0; i < Math.abs(deltaXMotion); i ++) {
	    addDeltaXSpin();
		repaint();
	  }
	}
    addMouseMotionListener (this);
  }

  public void mouseMoved(MouseEvent e)  {
    finXMotion = (int)e.getLocationOnScreen().getX();
	finYMotion = (int)e.getLocationOnScreen().getY();
	int deltaXMotion = finXMotion - (int)(screenWidth / 2);
	int deltaYMotion = finYMotion - (int)(screenHeight / 2);
	removeMouseMotionListener(this);
	try {
      Robot robot = new Robot();
      robot.mouseMove((int)(screenWidth / 2), (int)(screenHeight / 2));
	} catch (Exception ex) {}
	if (deltaYMotion > 0) {
	  for (int i = 0; i < Math.abs(deltaYMotion); i ++) {
	    subtractDeltaY();
		repaint();
	  }
	} else if (deltaYMotion < 0) {
	  for (int i = 0; i < Math.abs(deltaYMotion); i ++) {
	    addDeltaY();
		repaint();
	  }
	}
	if (deltaXMotion > 0) {
	  for (int i = 0; i < Math.abs(deltaXMotion); i ++) {
	    subtractDeltaXSpin();
	    repaint();
	  }
	} else if (deltaXMotion < 0) {
	  for (int i = 0; i < Math.abs(deltaXMotion); i ++) {
	    addDeltaXSpin();
		repaint();
	  }
	}
    addMouseMotionListener (this);
  }

  public void addFoV (double step) {
    for (Figure z: figures) {
	  z.addFoV(step);
	}
  }

  public void subtractFoV (double step) {
    for (Figure z: figures) {
	  z.subtractFoV(step);
	}
  }

  public void rightRelativeChangeToFoV() {
    for (Figure z: figures) {
	  double tmaximal = Double.NEGATIVE_INFINITY;
	  double tminimal = Double.POSITIVE_INFINITY;
	  double maximal = 0;
	  double minimal = 0;
	  double average = 0;
	  for (Triangle t: z.polygons) {
	    double t1 = t.v1.x / (-t.v1.z) * z.scale;
		double t2 = t.v2.x / (-t.v2.z) * z.scale;
		double t3 = t.v3.x / (-t.v3.z) * z.scale;
		if (t1 > t2) {
		  maximal = t1;
		  minimal = t2;
		} else {
	      maximal = t2;
		  minimal = t1;
		}
		if (t3 > maximal)
		  maximal = t3;
		else if (t3 < minimal)
		  minimal = t3;
		if (tmaximal < maximal)
		  tmaximal = maximal;
		if (tminimal > minimal)
		  tminimal = minimal;
		}
		tminimal += deltaX + deltaXSpin;
		tmaximal += deltaX + deltaXSpin;
	    average = (tminimal + tmaximal) / 2.0;
		if (average > screenWidth / 2.0) {
		  z.addFoV(0.2);
	    } else {
		  z.subtractFoV(0.2);
		}
	}
  }

  public void leftRelativeChangeToFoV() {
    for (Figure z: figures) {
	  double tmaximal = Double.NEGATIVE_INFINITY;
	  double tminimal = Double.POSITIVE_INFINITY;
	  double maximal = 0;
	  double minimal = 0;
	  double average = 0;
	  for (Triangle t: z.polygons) {
	    double t1 = t.v1.x / (-t.v1.z) * z.scale;
		double t2 = t.v2.x / (-t.v2.z) * z.scale;
		double t3 = t.v3.x / (-t.v3.z) * z.scale;
		if (t1 > t2) {
		  maximal = t1;
		  minimal = t2;
		} else {
	      maximal = t2;
		  minimal = t1;
		}
		if (t3 > maximal)
		  maximal = t3;
		else if (t3 < minimal)
		  minimal = t3;
		if (tmaximal < maximal)
		  tmaximal = maximal;
		if (tminimal > minimal)
		  tminimal = minimal;
		}
		tminimal += deltaX + deltaXSpin;
		tmaximal += deltaX + deltaXSpin;
	    average = (tminimal + tmaximal) / 2.0;
		if (average > screenWidth / 2.0) {
		  z.subtractFoV(0.2);
	    } else {
		  z.addFoV(0.2);
		}
	}
  }

  public Color getShade(Color color, double shade) {
    double redLinear = Math.pow(color.getRed(), 2.4) * shade;
    double greenLinear = Math.pow(color.getGreen(), 2.4) * shade;
    double blueLinear = Math.pow(color.getBlue(), 2.4) * shade;
    int red = (int)Math.pow(redLinear, 1 / 2.4);
    int green = (int)Math.pow(greenLinear, 1 / 2.4);
    int blue = (int)Math.pow(blueLinear, 1 / 2.4);
    return new Color(red, green, blue);
  }

  public void createObjects() {
    List<Triangle> tris = new ArrayList<>();
    //A
    tris.add(new Triangle(new Vertex(-100, 200, 100, 1),
                          new Vertex(100, 200, 100, 1),
                          new Vertex(-100, 200, -100, 1),
                          new Color (0, 152, 215)));
    //B
    tris.add(new Triangle(new Vertex(100, 200, 100, 1),
                          new Vertex(100, 200, -100, 1),
                          new Vertex(-100, 200, -100, 1),
                          new Color (0, 152 , 215)));

    //C
    tris.add(new Triangle(new Vertex(100, 0, 100, 1),
                          new Vertex(100, 200, -100, 1),
                          new Vertex(100, 200, 100, 1),
                          new Color (115, 119, 229)));
    //D
    tris.add(new Triangle(new Vertex(100, 0, 100, 1),
                          new Vertex(100, 0, -100, 1),
                          new Vertex(100, 200, -100, 1),
                          new Color (115, 119, 229)));

    //E
    tris.add(new Triangle(new Vertex(-100, 0, 100, 1),
                          new Vertex(100,  0, 100, 1),
                          new Vertex(-100, 200, 100, 1),
                          new Color (231, 111, 116)));

    //F
    tris.add(new Triangle(new Vertex(100, 0, 100, 1),
                          new Vertex(100, 200, 100, 1),
                          new Vertex(-100, 200, 100, 1),
                          new Color (231, 111, 116)));
    //G
    tris.add(new Triangle(new Vertex(-100, 0, 100, 1),
                          new Vertex(-100, 200, 100, 1),
                          new Vertex(-100, 0, -100, 1),
                          new Color (255, 207, 90)));
    //H
    tris.add(new Triangle(new Vertex(-100, 200, 100, 1),
                          new Vertex(-100, 200, -100, 1),
                          new Vertex(-100, 0, -100, 1),
                          new Color (255, 207, 90)));
    //I
    tris.add(new Triangle(new Vertex(-100, 200, -100, 1),
                          new Vertex(100, 200, -100, 1),
                          new Vertex(-100, 0, -100, 1),
                          new Color (142, 206, 213)));
    //J
    tris.add(new Triangle(new Vertex(-100, 0, -100, 1),
                          new Vertex(100, 200, -100, 1),
                          new Vertex(100, 0, -100, 1),
                          new Color (142, 206, 213)));
    //K
    tris.add(new Triangle(new Vertex(100, 0, 100, 1),
                         new Vertex(-100, 0, 100, 1),
                         new Vertex(-100, 0, -100, 1),
                         Color.WHITE));
    //L
    tris.add(new Triangle(new Vertex(-100, 0, -100, 1),
                          new Vertex(100, 0, -100, 1),
                          new Vertex(100, 0, 100, 1),
                          Color.WHITE));
    figures.add(new Figure(tris, 140));
    List<Triangle> tris1 = new ArrayList<>();
    //scene B
    tris1.add(new Triangle(new Vertex(-200, 200, 200, 1),
                           new Vertex(200, 200, 200, 1),
                           new Vertex(-200, 200, -200, 1),
                           new Color (255, 132, 88)));

    tris1.add(new Triangle(new Vertex(200, 200, 200, 1),
                           new Vertex(200, 200, -200, 1),
                           new Vertex(-200, 200, -200, 1),
                           new Color (255, 132, 88)));
    figures.add(new Figure(tris1, 140));

    List<Triangle> tris2 = new ArrayList<>();
    //Scene C
    tris2.add(new Triangle(new Vertex(400, 100, 100, 1),
                           new Vertex(200, -100, 100, 1),
                           new Vertex(200, 100, -100, 1),
                           new Color (88, 255, 119)));
	tris2.add(new Triangle(new Vertex(400, 100, 100, 1),
						  new Vertex(200, -100, 100, 1),
						  new Vertex(400, -100, -100, 1),
						  new Color (128, 88, 255)));
	tris2.add(new Triangle(new Vertex(200, 100, -100, 1),
						  new Vertex(400, -100, -100, 1),
						  new Vertex(400, 100, 100, 1),
						  new Color (235, 255, 88)));
	tris2.add(new Triangle(new Vertex(200, 100, -100, 1),
						  new Vertex(400, -100, -100, 1),
						  new Vertex(200, -100, 100, 1),
						  new Color (255, 88, 125)));
    figures.add(new Figure(tris2, 140));
  }

  public void resetValues() {
    deltaX = screenWidth / 2;
    deltaY = screenHeight / 2;
    deltaXSpin = 0;
    headingSlider = 0;
    for (Figure z: figures) {
	  z.setFoV(140);
	}
  }
}

class Figure {
  double scale;
  List<Triangle> polygons;

  public Figure(List<Triangle> polygons, double scale) {
    this.polygons = polygons;
    this.scale = scale;
  }

  public void addFoV(double step) {
    if  (scale + 1 <= 180)
      scale += step;
  }

  public void subtractFoV(double step) {
    if (scale - 1 >= 0)
      scale -= step;
  }

  public void setFoV(double value) {
    scale = value;
  }

  public double getFoV() {
    return scale;
  }
}

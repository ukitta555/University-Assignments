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

class MyFrame extends JFrame {
    MyJPanel renderPanel;
    MyJSlider headingSlider;
    MyJSlider pitchSlider;
    MyJSlider rollSlider;
    MyJSlider FoVSlider;

	public MyFrame (String s) { //переделанный под ООП вариант нашего окна
		  JFrame frame = new JFrame();
        Container pane = frame.getContentPane(); //контейнер для изображения
        pane.setLayout(new BorderLayout());
      
        // slider to control horizontal rotation
        this.headingSlider = new MyJSlider(SwingConstants.HORIZONTAL,-180, 180, 0,this);  //передаем this, чтобы была возможность вызвать метод, который вернет renderPanel для перерисовки 
        pane.add(headingSlider, BorderLayout.SOUTH);

        // slider to control vertical rotation
        this.pitchSlider = new MyJSlider(SwingConstants.VERTICAL, -180, 180, 0,this); //передаем this, чтобы была возможность вызвать метод, который вернет renderPanel для перерисовки 
        pane.add(pitchSlider, BorderLayout.EAST);

        // slider to control roll
        this.rollSlider = new MyJSlider(SwingConstants.VERTICAL, -180, 180, 0,this);  //передаем this, чтобы была возможность вызвать метод, который вернет renderPanel для перерисовки 
        pane.add(rollSlider, BorderLayout.WEST);

        // slider to control FoV
        this.FoVSlider = new MyJSlider(SwingConstants.HORIZONTAL,1, 179, 60,this);  //передаем this, чтобы была возможность вызвать метод, который вернет renderPanel для перерисовки 
        pane.add(FoVSlider, BorderLayout.NORTH);
             
        // panel to display render results
         renderPanel = new MyJPanel(headingSlider,pitchSlider,rollSlider,FoVSlider); // передаем все слайдеры чтобы Джава не ругалась на статик
            pane.add(renderPanel, BorderLayout.CENTER);
        frame.setSize(400, 400);
        frame.setVisible(true);
		}
		//собсна метод для ООПшников, получаем renderPanel для действий с ней. (см.  public void stateChanged () ниже )
	public MyJPanel getRenderPanel () {
		return renderPanel;
		} 
	}

class MyJSlider extends JSlider implements ChangeListener{
	MyFrame frame; //this, который мы передали ранее
    public MyJSlider (int ori,int str,int fin,int q,MyFrame frame) {
          super (ori,str,fin,q);//создание слайдера на основе родителя
          this.addChangeListener (this);//прослушка 
          this.frame=frame;//ну и присвоение фрейма как поля класса
        }
    public void stateChanged (ChangeEvent e) {
          frame.getRenderPanel().repaint(); //перерисовка
        }
    }

//жи есть пенел, черная магия происходит прямо здесь
class MyJPanel extends JPanel  {
	MyJSlider headingSlider; //слайдеры
    MyJSlider pitchSlider;
    MyJSlider rollSlider;
    MyJSlider FoVSlider;
public MyJPanel (MyJSlider headingSlider, MyJSlider pitchSlider,MyJSlider rollSlider,MyJSlider FoVSlider) {
	//конструктор, ничего необычного
	 this.headingSlider=headingSlider;
	 this.rollSlider=rollSlider;
	 this.pitchSlider=pitchSlider;
	 this.FoVSlider=FoVSlider;
	}
//отрисовка
public void paintComponent(Graphics g) {
                    Graphics2D g2 = (Graphics2D) g;
                    g2.setColor(Color.GRAY);
                    g2.fillRect(0, 0, getWidth(), getHeight());//заполнение экрана

                    List<Triangle> tris = new ArrayList<>(); //вектор треугольников, которые состоят из векторов (костыль №4)
                    //A
                    tris.add(new Triangle(new Vertex(-100, 100, 100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          Color.WHITE));
                    //B
                    tris.add(new Triangle(new Vertex(100, 100, 100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          Color.WHITE));
                    //C
                    tris.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          Color.WHITE));
                    //D
                    tris.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          Color.WHITE));
                    //E
                    tris.add(new Triangle(new Vertex(-100, -100, 100, 1),
                                          new Vertex(100, -100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          Color.WHITE));

                    //F
                    tris.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(100, 100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          Color.WHITE));
                    //G
                    tris.add(new Triangle(new Vertex(-100, -100, 100, 1),
                                          new Vertex(-100, 100, 100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //H
                    tris.add(new Triangle(new Vertex(-100, 100, 100, 1),
                                          new Vertex(-100, 100, -100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //I
                    tris.add(new Triangle(new Vertex(-100, 100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //J
                    tris.add(new Triangle(new Vertex(-100, -100, -100, 1),
                                          new Vertex(100, 100, -100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          Color.WHITE));
                    //K
                    tris.add(new Triangle(new Vertex(100, -100, 100, 1),
                                          new Vertex(-100, -100, 100, 1),
                                          new Vertex(-100, -100, -100, 1),
                                          Color.WHITE));
                    //L
                    tris.add(new Triangle(new Vertex(-100, -100, -100, 1),
                                          new Vertex(100, -100, -100, 1),
                                          new Vertex(100, -100, 100, 1),
                                          Color.WHITE));
         
                    double heading = Math.toRadians(headingSlider.getValue()); // получаем значение слайдера, переводим в радианы
                    Matrix4 headingTransform = new Matrix4(new double[] {
                            Math.cos(heading), 0, -Math.sin(heading), 0,
                            0, 1, 0, 0,
                            Math.sin(heading), 0, Math.cos(heading), 0,
                            0, 0, 0, 1
                        });                                                   //матрица поворота 1
                    double pitch = Math.toRadians(pitchSlider.getValue());  //повторяем, создаем 2 матрицу
                    Matrix4 pitchTransform = new Matrix4(new double[] {  
                            1, 0, 0, 0,
                            0, Math.cos(pitch), Math.sin(pitch), 0,
                            0, -Math.sin(pitch), Math.cos(pitch), 0,
                            0, 0, 0, 1
                        });
                    double roll = Math.toRadians(rollSlider.getValue()); //повторяем, создаем 3 матрицу
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

                    double viewportWidth = getWidth(); //расчет для будущего сдвига, чтобы куб посредине.
                    double viewportHeight = getHeight();//расчет для будущего сдвига, чтобы куб посредине.
                    
                    double fovAngle = Math.toRadians(FoVSlider.getValue()); //получаем значение слайдера
                    double fov = Math.tan(fovAngle / 2) * 170; // переменная, описывающая как сильно будет увеличиваться наша каритнка. больше множитель - больше кайфа.

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

                    for (Triangle t : tris) {
                        Vertex v1 = transform.transform(t.v1); //получаем новые вектора
                        Vertex v2 = transform.transform(t.v2);
                        Vertex v3 = transform.transform(t.v3);

                        Vertex ab = new Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z, v2.w - v1.w); //ищем вектор нормалей
                        Vertex ac = new Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z, v3.w - v1.w); //ищем вектор нормалей
                        Vertex norm = new Vertex(
                                                 ab.y * ac.z - ab.z * ac.y,
                                                 ab.z * ac.x - ab.x * ac.z,
                                                 ab.x * ac.y - ab.y * ac.x,
                                                 1
                                                 ); //нашли вектор нормалей
                        double normalLength = Math.sqrt(norm.x * norm.x + norm.y * norm.y + norm.z * norm.z); //нашли его длину

                        norm.z /= normalLength; // якась формула из статьи

                        double angleCos = Math.abs(norm.z); // легко видеть, что косинус это ответ на все вопросы математики
 
                         //машстабирвоание, скорее всего связано  с той самой матрицей
                        v1.x = v1.x / (-v1.z) * fov;
                        v1.y = v1.y / (-v1.z) * fov;
                        v2.x = v2.x / (-v2.z) * fov;
                        v2.y = v2.y / (-v2.z) * fov;
                        v3.x = v3.x / (-v3.z) * fov;
                        v3.y = v3.y / (-v3.z) * fov;
                          //сдвиг куба, без него он был бы в начале координатной плоскости, как мы и думали
                         v1.x += viewportWidth / 2;
                        v1.y += viewportHeight / 2;
                        v2.x += viewportWidth / 2;
                        v2.y += viewportHeight / 2;
                        v3.x += viewportWidth / 2;
                        v3.y += viewportHeight / 2;
                          //процесс зет буферизации. поиск минимальных  и максимальных координат  треугольника
                        int minX = (int) Math.max(0, Math.ceil(Math.min(v1.x, Math.min(v2.x, v3.x))));
                        int maxX = (int) Math.min(img.getWidth() - 1, Math.floor(Math.max(v1.x, Math.max(v2.x, v3.x))));
                        int minY = (int) Math.max(0, Math.ceil(Math.min(v1.y, Math.min(v2.y, v3.y))));
                        int maxY = (int) Math.min(img.getHeight() - 1, Math.floor(Math.max(v1.y, Math.max(v2.y, v3.y))));
                         //расчет площади нашего 2D треугольника * 2(так надо по следующей формуле)
                        double triangleArea = (v1.y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - v1.x);
                         // расчет барицентрированных координат
                        for (int y = minY; y <= maxY; y++) { //полный перебор все возможных координат для данного треугольника
                            for (int x = minX; x <= maxX; x++) {
                                double b1 = ((y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - x)) / triangleArea; //1 координата
                                double b2 = ((y - v1.y) * (v3.x - v1.x) + (v3.y - v1.y) * (v1.x - x)) / triangleArea;//2 координата
                                double b3 = ((y - v2.y) * (v1.x - v2.x) + (v1.y - v2.y) * (v2.x - x)) / triangleArea; //3 координата
                                if (b1 >= 0 && b1 <= 1 && b2 >= 0 && b2 <= 1 && b3 >= 0 && b3 <= 1) { //т.к. все точки, которые нахожятся внутри треугольника, должны иметь барицентрированные координаты, котоыре меньше 0 и больше 1, вводится данная проверка
                                    double depth = b1 * v1.z + b2 * v2.z + b3 * v3.z; //расчет текущей "глубины" пикселя
                                    int zIndex = y * img.getWidth() + x; //уникальный зет индекс для данного пикселя, другого такого не найдешь
                                    if (zBuffer[zIndex] < depth) {//если  глубина пикселя больше, то он находится ближе, значит рисовать будем
                                        img.setRGB(x, y, getShade(t.color, angleCos).getRGB());
                                        zBuffer[zIndex] = depth; //в зет буфер данного пикселя записываем новое значение глубины, чтобы при пересчете только пиксель, лежащий выше, был перерисован
                                    }
                                }
                            }
                        }
                    }
                    g2.drawImage(img, 0, 0, null);
                }
     public Color getShade(Color color, double shade) {
        double redLinear = Math.pow(color.getRed(), 2.4) * shade;
        double greenLinear = Math.pow(color.getGreen(), 2.4) * shade;
        double blueLinear = Math.pow(color.getBlue(), 2.4) * shade;

        int red = (int) Math.pow(redLinear, 1/2.4);
        int green = (int) Math.pow(greenLinear, 1/2.4);
        int blue = (int) Math.pow(blueLinear, 1/2.4);

        return new Color(red, green, blue);
    }
   }

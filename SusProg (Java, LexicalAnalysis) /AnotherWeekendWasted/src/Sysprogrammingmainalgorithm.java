/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author VVN
 */

import java.lang.*;
import java.util.*;
import java.io.*;
import java.nio.charset.Charset;
import JavaTeacherLib.*;

public class Sysprogrammingmainalgorithm {

 public static void main(String[] args) {
      String readline;
      boolean result;
      String fileName;
      MyLang testLang=null;
      int codeAction, llk=1, textLen;
      String [] menu= { "*1.  Прочитати граматику з файла  ",
                        " 2.  Лабораторна робота. Клас будує студент",
                        " 3.  Надрукувати граматику",
                        "*4.  Побудувати списки терміналів та нетерміналів",
                        "*5.  Пошук непродуктивних нетерміналів",
                        "*6.  Пошук недосяжних нетерміналів",
                        "*7.  Побудова списку епсілон-нетерміналів",
                        " 8.  Друк списку епсілон-нетерміналів",
                        " 9.  Пошук ліворекурсивних нетерміналів",
                        " 10. Пошук різних ліворекурсивних виводів мінімальної довжини",
                        " 11. Пошук праворекурсивних нетерміналів",
                        " 12. Пошук різних праворекурсивних виводів мінімальної довжини",
                        "*13. Побудувати множини FirstK(A), A-нетермінал",
                        " 14. Вивести на термінал множини FirstK(A), A-нетермінал",
                        "*15. Побудувати множини FollowK(A), A-нетермінал",
                        " 16. Вивести на термінал множини FollowK(A), A-нетермінал",
                        "*17. Побудувати множини FirstK(w) + FollowK(A) для правила А->w",
                        " 18. Вивести на термінал FirstK(w) + FollowK(A) для всіх правил А->w",
                        " 19. Вивести на термінал FirstK(w) + FollowK(A) для вибраних правил А->w",
                        "*20. Перевірка сильної LL(1)-властивості",
                        " 21. Побудова таблиці LL(1)-синтаксичного аналізатора",
                        " 22. Синтаксичний аналізатор. Клас будує студент",
                        "*23. Побудувати множини LocalK(A), A-нетермінал",
                        " 24. Вивести на термінал множини LocalK(A), A-нетермінал",
                        "*25. Перевірка LL(k)-властивості, k>1",
                        " 26. Вихід з системи"
                      };

      Scanner scan = new Scanner(System.in);
     do  {
       codeAction=0;
       String upr;
      for (String ss: menu) System.out.println(ss); // вивести меню
      System.out.println("Введіть код дії або end:");
     do {  // цикл перебору даних
       try {
          readline = scan.nextLine();
          upr = readline;
        if (upr.trim().equals("end") ) return;
        codeAction=new Integer (upr.trim());
          }
       catch(Exception ee)
            { System.out.println ("Невірний код дії, повторіть: ");
             continue;
            }
       if (codeAction >=1  &&  codeAction<=menu.length ) {
           if (menu [codeAction-1].substring(0, 1).equals("+"))  {
            System.out.println("Елемент меню " +codeAction+" повторно виконати неможливо");
            continue ;
            }
           int itmp;
           for (itmp=0; itmp < codeAction-1; itmp++)
               if (menu[itmp].substring(0, 1).equals("*")) break;
           if (itmp !=codeAction-1) {
               System.out.println ("Виконайте попередні елементи меню, що позначені * : ");
               continue ;
              }
           break;
          }
          else {
            System.out.println ("Невірний код дії, повторіть: ");
            continue ;
           }
     }  while (true);
     // перевірка на виконання усіх попередніх дій
     result=false;
       switch (codeAction) {
            case 1: //1. Прочитати граматику з файла",
                System.out.println ("Введіть ім'я файлу граматики: ");
                 try {
                    readline = scan.nextLine();
                    fileName = readline;
                    System.out.println ("Ім'я файлу граматики: "+ fileName);
                    fileName = fileName.trim();
                     }
                   catch(Exception ee)
                        { System.out.println ("Системна помилка: "+ee.toString());
                          return;
                        }
                System.out.println ("Введіть значення параметра k : ");
                try {
                    readline = scan.nextLine();
                    String llkText = readline;
                    llkText = llkText.trim();
                    llk=Integer.parseInt(llkText);
                     }
                   catch(Exception ee)
                        { System.out.println ("Системна помилка: "+ee.toString());
                          return;
                        }
                testLang = new MyLang (fileName,llk);
                if (!testLang.isCreate()) break;  //не створили об'єкт
                System.out.println ("Граматика прочитана успішно");
                result=true;
                for (int jj=0;  jj<menu.length; jj++) {
                   if (menu [jj].substring(0, 1).equals(" ")) continue;
                   menu [jj]=menu [jj].replace(menu [jj].charAt(0), '*') ;
                  }
                   break;
            case 2: //2. Лабораторна робота студента
                //  метод для скінчених автоматів
                break;
            case 3:  // Надрукувати граматику
                 testLang.printGramma();
                 break;
            case 4:  // надрукувати список терміналів та нетерміналів
                 testLang.printTerminals();
                 testLang.printNonterminals();
                 result=true;
                break;
            case 5: // вивести непродуктивні правила
                 result=testLang.createNonProdRools();
                 break;
            case 6: // недосяжні нетермінали
                result=testLang.createNonDosNeterminals();
                 break;
             case 7:  //Побудова списку епсілон-нетерміналів
                  int [] epsilon=testLang.createEpsilonNonterminals ();
                  testLang.setEpsilonNonterminals (epsilon);
                  result=true;
                 break;
             case 8: //Друк списку епсілон-нетерміналів
                  testLang.printEpsilonNonterminals();
                 break;
             case 9:    //Пошук ліворекурсивних нетерміналів"
                 testLang.leftRecursNonnerminal();
                  break;
               case 10:  //Пошук різних ліворекурсивних виводів мінімальної довжини"
                  // testLang.leftRecusionTrace();
                   break;
               case 11:  //Пошук праворекурсивних нетерміналів"
                    testLang.rightRecursNonnerminal();
                   break;
               case 12:  //Пошук різних праворекурсивних виводів мінімальної довжини"
                  //testLang.rigthRecusionTrace();
                   break;
               case 13:  //Побудувати множини FirstK
                   LlkContext [] firstContext = testLang.firstK();
                   testLang.setFirstK(firstContext);
                   result=true;
                   break;
               case 14:  //Друк множини FirstK
                   testLang.printFirstkContext ( );
                   break;
               case 15:  //Побудувати множини FollowK
                   LlkContext [] followContext = testLang.followK();
                   testLang.setFollowK(followContext);
                   result=true;
                   break;
             case 16:  //Друк множини FollowK
                   testLang.printFollowkContext ( );
                   break;
             case 17:  //Побудувати множини FirstK(w) + FollowK(A) для правила А->w
                   testLang.firstFollowK ( );
                   result=true;
                   break;
              case 18:  //Друк множини FirstK(w) + FollowK(A) для правила А->w
                   testLang.printFirstFollowK( );
                   break;
              case 19:  //Друк множини FirstK(w) + FollowK(A) для вибраних правил А->w
                   testLang.printFirstFollowForRoole();
                   break;
             case 20:  //Перевірка сильної LL(k)-властивості",
                 result=testLang. strongLlkCondition () ;
                    break;
            case 21:  //Побудова таблиці LL(1)-синтаксичного аналізатора
             //     int [][] uprTable=testLang.createUprTable ();
             //       testLang.setUprTable(uprTable);
                   break;
             case 22: // PASCAL
                break;

             case 23: // 23. Побудувати множини LocalK(A), A-нетермінал
                LinkedList <LlkContext> [] Localk=testLang.createLocalK();
                testLang.setLocalkContext(Localk);
                result=true;
                break;
             case 24: // 24. Вивести на термінал множини LocalK(A), A-нетермінал
                   testLang.printLocalk();
                   break;
             case 25: // 25. Перевірка LL(k)-властивості, k>1
                result= testLang.llkCondition();
                 break;
             case 26: // rtrtrtr
                 return;
             case 27:
                 break;
             }  // кінець switch
       // блокуємо елемент обробки
       if (result) // функція виконана успішно
           if (menu [codeAction-1].substring(0, 1).equals("*"))
                 menu [codeAction-1]=menu [codeAction-1].replace('*', '+') ;
   } while (true);  //глобальний цикл  обробки

 }  // кінець main

 }

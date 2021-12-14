import java.util.*;


interface StrParser {
	
  int length ();//done
	 
 int count (String sep);//done
	  
String wordOf (int i);//done
	
  String firstWord ();//done
	 
 String lastWord ();//done
	 
 String nextWord ();//done
	 
 String join (String sep);//done
	
  String[] sort ();//done
	  
void toArrayReverse ();//done
	 
 void toArray ();//done
	}



class Solution 
implements StrParser {

	
  String str;
	  
int position;
	 
 String [] wordArray;
	
  int count=0;
	  
int actual_length=0;
	

  public Solution (String str){
	
	  this.str=str;
		
  this.position=0;
		
  }
	
	  
	
  public int length () {
		  count=str.length();
		  return count;
		  };
		  
	  public int count (String sep) {
		   String separ=sep+"+";
		   wordArray=str.split(separ);
		   actual_length=wordArray.length;
		   return wordArray.length;
		  };
		  
	  public String wordOf (int i) {
		  position=i;
		  return wordArray[position-1];
		  };
	  public String firstWord () {
		  position=1;
		  return wordArray[position-1];
		  }
	  public String lastWord () {
		  position=count;
		  return wordArray[position-1];
		  }
	  public String nextWord (){
		  position++;
          return wordArray[position-1];
		  }
	  public String join (String sep) {
		  String new_string=wordArray[0];
		  for (int i=1;i<actual_length;i++) {
			  new_string=new_string+sep+wordArray[i];
			  System.out.println(new_string+"?");
			  }
		  return new_string;
	 }
	  
	  public String [] sort () {
		  sort1(0,actual_length-1);
		  return wordArray;
		  }
	  public void sort1 (int l,int r) {
      int i,j;
      String k;
      i=l;
      j=r;
      k=wordArray[(int)((i+j)/2)];
      do{
        while (wordArray[i].compareTo(k)>0) {
          ++i;
        }
        while (wordArray[j].compareTo(k)<0) {
          --j;
        }
      String t;
      if (i<=j) {
         t=wordArray[i];
         wordArray[i]=wordArray[j];
         wordArray[j]=t;
         i++;
         j--;
      }
    }
    while (i<j);
    if (i<r)
     sort1 (i,r);
    if (l<j)
     sort1 (l,j);
}
public void toArray () {
	 for (int i=0;i<actual_length;i++) {
		  System.out.println(wordArray[i]);
		 }
	}

public void toArrayReverse () {
	for (int i=actual_length-1;i>=0;i--) {
		  System.out.println(wordArray[i]);
	}
	}
	}
class Main{
	public static void main (String [] z) {
		Scanner sc=new Scanner (System.in);
		String line=sc.nextLine();
		Solution xd=new Solution (line);
		xd.count(":");
		xd.toArrayReverse();
		}
	}

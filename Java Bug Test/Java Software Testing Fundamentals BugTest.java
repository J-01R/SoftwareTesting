
public class BugTest {
	
	public interface Foo {

		Object name = null;

		}

	public static void main(String[] args) {
		// TODO -- Write your name and in the print bellow, then compile and run the code to print the output.
		//System.out.print("DVGB17 - My name is : ");
		
		
		int x = 6;
        int y = 8;
        double z = x /y; 
        h(false);
		


	}
	
	public static boolean g() {
        if (g()) {
            return true; 
        } else {
            return g();
        }
    }
 
    
    public static boolean h(final boolean in) {
        if (in) {
            h(!in);
        }
        return false;
    }
 
    public static int fibonacci(int n) {
        if (n < 2) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    
private Long myNtfSeqNbrCounter = new Long(0);
    private Long getNotificationSequenceNumber() {
         Long result = null;
         synchronized(myNtfSeqNbrCounter) { 
             result = new Long(myNtfSeqNbrCounter.longValue() + 1);
             myNtfSeqNbrCounter = new Long(result.longValue());
         }
         return result;
    }
    
    public boolean equals(Object o) {
        Object name = null;
if (o instanceof Foo)
            return name.equals(((Foo)o).name); 
        else if (o instanceof String)
            return name.equals(o); 
        else return false; 
    }
    

    
    abstract class A {
        int hashCode;
        abstract Object getValue();

        A() {
            hashCode = getValue().hashCode();
        }
    }

    class B extends A {
        Object value;

        B(Object v) {
            this.value = v;
        }

        Object getValue() {
            return value; 
        }
    }
	

}

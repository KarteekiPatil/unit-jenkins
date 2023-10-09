import static org.junit.Assert.*;

public class Squreunit {
	@Test
	public void test() {
		Squre s=new Squre();
		int op= s.sqrt(5);
		assertEquals(25,op);
	}
}

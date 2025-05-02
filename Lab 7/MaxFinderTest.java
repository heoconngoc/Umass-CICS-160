import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class MaxFinderTest{
  @Test
  public void testFindMaximum(){
    double[] A = {100, 0,9,22, -4, 6, 999};
    assertEquals(MaxFinder.findMaximum(A), 999, 0.01);
  }

  @Test
  public void testFindMaximum1st(){
    double[] B = {100, 0,9,22, -4, 6};
    assertEquals(MaxFinder.findMaximum(B), 100, 0.01);
  }

  @Test
  public void testFindOnlyMaximum(){
    double[] C = {100};
    assertEquals(MaxFinder.findMaximum(C), 100, 0.01);
  }
}
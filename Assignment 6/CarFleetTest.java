import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.List;

public class CarFleetTest {
  @Test
  public void testAddCar(){
    CarFleet fleet = new CarFleet();

    Car gas = new Car(001, 1, 50);
    Car hybrid = new Car(002, 2, 60);
    Car electric = new Car(003,3,70);
    
    assertTrue(fleet.addCar(gas));
    assertTrue(fleet.addCar(hybrid));
    assertTrue(fleet.addCar(electric));
    assertFalse(fleet.addCar(new Car(2,5,4)));
  }

  @Test
  public void testProcessRequest(){
    CarFleet fleet = new CarFleet();

    Car gas = new Car(001, 1, 50);
    Car hybrid = new Car(002, 2, 60);
    Car electric = new Car(003,3,70);
    
    assertTrue(fleet.addCar(gas));
    assertTrue(fleet.addCar(hybrid));
    assertTrue(fleet.addCar(electric));

    Queue<Integer> request = new Queue<>();
    request.enqueue(1);
    request.enqueue(2);
    request.enqueue(3);
    request.enqueue(1);

    List<Car> resutls = fleet.processRequests(request);
    assertEquals(001, resutls.get(0).getId());
    assertEquals(002, resutls.get(1).getId());
    assertEquals(003, resutls.get(2).getId());
    assertEquals(0, resutls.get(3).getId());
  }
}
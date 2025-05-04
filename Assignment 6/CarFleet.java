import java.util.ArrayList;
import java.util.List;

public class CarFleet {
  private Queue<Car> gasoline;
  private Queue<Car> hybrid;
  private Queue<Car> electric;

  public CarFleet(){
    gasoline = new Queue<>();
    hybrid = new Queue<>();
    electric = new Queue<>();
  }

  public boolean addCar(Car car){
    int type = car.getPowerSource();
    if (type != 1 && type != 2 && type != 3){
      return false;
    }
    if(type == 1){
      gasoline.enqueue(car);
    } else if (type == 2){
      hybrid.enqueue(car);
    } else if(type == 3){
      electric.enqueue(car);
    }
    return true;
  }

  public List<Car> processRequests(Queue<Integer> request){
    List<Car> result = new ArrayList<>();
    
    while (!request.isEmpty()) {
      int num = request.dequeue();
      Car car = null;
      switch (num) {
        case 1:
        car = gasoline.dequeue();
          break;
        case 2:
          car = hybrid.dequeue();
          break;
        case 3:
          car = electric.dequeue();
          break;
      }
      if (car == null){
        car = new Car(0,num,0);
      }
      result.add(car);
    }
    return result;
  }
}
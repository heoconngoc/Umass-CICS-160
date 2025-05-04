import java.util.LinkedList;

public class Queue<Type> {
  private LinkedList<Type> list;
  
  public Queue(){
    list = new LinkedList<>();
  }

  // Add element to the last of queue
  public void enqueue(Type ele){
    list.addLast(ele);
  }

  // Del and return the first ele in queue
  public Type dequeue() {
      if(isEmpty()){
        return null;
      }
      return list.removeFirst();
  }

  // Return the first ele without removing it
  public Type peek() {
    if(isEmpty()){
      throw new IllegalArgumentException("Cannot peek from a empty queue.");
    }
    return list.getFirst();
  }

  public boolean isEmpty(){
    return list.isEmpty();
  }
}
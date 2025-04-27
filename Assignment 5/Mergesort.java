import java.util.LinkedList;

public class Mergesort{
  public static void main(String[] args){
    LinkedList<Integer> list = new LinkedList<>();
    list.add(10);
    list.add(2);
    list.add(0);
    list.add(8);
    list.add(6);

    System.out.println("Original list: " + list);
    LinkedList<Integer> sortedList = sort(list);
    System.out.println("Sorted list: " + sortedList);

    LinkedList<Integer> newList = makeNewList(sortedList, 2, 4);
    System.out.println("New list: " + newList);

  }

  public static LinkedList<Integer> sort(LinkedList<Integer> ll) {
    if(ll.size() <= 1){
      return ll;
    }
    int middle = ll.size() / 2;
    LinkedList<Integer> left = new LinkedList<>(ll.subList(0, middle));
    LinkedList<Integer> right = new LinkedList<>(ll.subList(middle, ll.size()));
    
    left = sort(left);
    right = sort(right);
    
    return merge(left, right);
  }

  public static LinkedList<Integer> makeNewList(LinkedList<Integer> original, int fromHere, int toHere){
    LinkedList<Integer> newList = new LinkedList<>();
    for(int i = fromHere; i <= toHere; i++) {
      newList.add(original.get(i));
    }
    return newList;
  }

  public static LinkedList<Integer> merge(LinkedList<Integer> a, LinkedList<Integer> b){
    LinkedList<Integer> result = new LinkedList<>();

    while (!a.isEmpty() && !b.isEmpty()) {
      // peekFirst: return the first 
      if (a.peekFirst() <= b.peekFirst()){
        // pollFirst: return the first and remove it from the LL
        result.add(a.pollFirst());
      } else{
        result.add(b.pollFirst());
      }
    }

    // add the last ele of left or right
    result.addAll(a);
    result.addAll(b);

    return result;
  }
}
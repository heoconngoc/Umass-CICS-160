public class Car {
  private int id;
  private int powerSource; // 1 = gasoline, 2 = hybrid, 3 = electric
  private float pricePerDay;

  public Car(int id, int powerSource, float pricePerDay) {
    this.id = id;
    this.powerSource = powerSource;
    this.pricePerDay = pricePerDay;
  }

  public int getId(){
    return id;
  }

  public void setId(int id){
    this.id = id;
  }

  public int getPowerSource(){
    return powerSource;
  }

  public void setPowerSource(int powerSource){
    this.powerSource = powerSource;
  }

  public double getPricePerDay(){
    return pricePerDay;
  }

  public void setPricePerDay(float pricePerDay){
    this.pricePerDay = pricePerDay;
  }

  public String toString(){
    return "Car ID: " + id + ", Power Source: " + powerSource + ", Price per Day: $" + pricePerDay;
  }
}

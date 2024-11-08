package Model;

public class Client {
    private String name;
    private int age;
    private String phoneNumber;

    public Client(String name, int age, String phoneNumber) {
        name = this.name;
        age = this.age;
        phoneNumber = this.phoneNumber;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getPhoneNumer() {
        return phoneNumber;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setPhoneNumer(String phoneNumer) {
        this.phoneNumber = phoneNumer;
    }

    public boolean equals(Client aClient) {
        return this.name.equals(aClient.name) && this.age == aClient.age &&
                this.phoneNumber.equals(aClient.phoneNumber);
    }

}
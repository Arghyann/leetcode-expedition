public class Stack{
    int top;
    int[] arr;

    Stack(){
        this.arr=new int[2];
        this.top=-1;}
    

    void push(int x){
        if(top+1 >= arr.length-1){
            resize();
        }

        top++;
        arr[top]=x;

    }
    int pop(){
        if (top==-1){
            System.out.println("empty stack bro");

        }
        int y=arr[top];
        top--;
        return y;

    }
    void resize(){
        int[] arr2;
        arr2=new int[2*arr.length];
        for(int i=0;i<arr.length;i++){
            arr2[i]=arr[i];
        }

    }
}

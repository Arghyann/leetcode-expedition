class CanConstruct{

    public static boolean cando(String s,String[] array){
        if (s.length()==0) return true;
        for(String x:array){
            if(s.length() >= x.length() && s.substring(0, x.length()).equals(x)){
                boolean temp=cando(s.substring(x.length()), array);
                if(temp) return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        String s = "applepenapples";

        String[] array = {
            "apple",
            "pen"
        };

        boolean result = cando(s, array);

        System.out.println("Final Result: " + result);
    }
}
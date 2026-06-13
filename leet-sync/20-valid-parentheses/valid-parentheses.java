class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(int i =0; i<s.length();i++){
            char temp=s.charAt(i);
            if(temp=='{'||temp=='['||temp=='('){
                stack.push(temp);
            }
            else{
                if(stack.isEmpty()){
                    return false;
                }
                char peek=stack.peek();
                if(peek=='(' && temp==')'){
                    stack.pop();
                }
                else if(peek=='{' && temp=='}'){
                    stack.pop();
                }
                else if(peek=='[' && temp==']'){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
        }
        if(stack.isEmpty()){
            return true;
        }
        else{
            return false;
        }
    }
}
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int phone_number_length = phone_number.length();
        StringBuilder str = new StringBuilder();
        
        for (int i=0; i<phone_number_length; i++){
            if (i > phone_number_length-5){
                str.append("" + phone_number.charAt(i));
            } else{
                str.append("*");
            }
        }
        
        return str.toString();
    }
}
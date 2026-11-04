class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int change  = 0;
        int tens =0;
        int fives=0;
        for(auto&p : bills){
            if(p==5) {
                fives++;
            }

            if (p==10){
                tens ++;
                if(fives>=1){
                    fives--;
                } else return false;
            }

            if(p==20){
                if(tens>0 && fives>0){
                    tens--;
                    fives--;
                } else if(fives>=3){
                    fives-=3;
                } else return false;
            }

        }
        return true;
        
    }
};
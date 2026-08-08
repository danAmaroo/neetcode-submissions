class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> dict1;
        unordered_map<char, int> dict2;

        for( char letter : s ){
            if(dict1.count(letter) == 0){
                dict1[letter] = 1;
            }
            else{
                dict1[letter] += 1;
            }
        }

        for( char letter : t ){
            if(dict2.count(letter) == 0){
                dict2[letter] = 1;
            }
            else{
                dict2[letter] += 1;
            }
        }

        if (dict1 == dict2){
            return true;
        }
        else{
            return false;
        }

    }
};

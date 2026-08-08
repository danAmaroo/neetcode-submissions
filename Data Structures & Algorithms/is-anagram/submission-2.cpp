class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> l;
        unordered_map<char, int> r;
        for(int i = 0; i < s.size(); i++){
            l[s[i]] += 1;
        }
        for(int i = 0; i < t.size(); i++)
        {
            r[t[i]] += 1;
        }
        if(r == l){
            return true;
        }
        else{
            return false;
        }
    }
};

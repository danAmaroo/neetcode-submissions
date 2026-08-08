class Solution {
public:
    bool isAnagram(string s, string t) {
    unordered_map<char, int> map1, map2;
    for(int i = 0; i < s.length(); i++)
    {
        map1[s[i]] += 1;
    }
    for(int i = 0; i < t.length(); i++)
    {
        map2[t[i]] += 1;
    }
    if(map1 == map2){
        return true;
    }
    else{
        return false;
    }

    }
};

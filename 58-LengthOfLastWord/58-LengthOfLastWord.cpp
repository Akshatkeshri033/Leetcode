// Last updated: 8/20/2025, 5:49:45 PM
class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int index = n - 1;

        // Skip trailing spaces
        while (index >= 0 && s[index] == ' ') {
            index--;
        }

        int temp = index;

        // Count characters of the last word
        while (index >= 0 && s[index] != ' ') {
            index--;
        }

        return temp - index;
    }
};
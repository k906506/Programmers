class Solution {
    var result = 0;
    fun solution(a: IntArray, b: IntArray): Int {
        for(i in a.indices){
            result += a[i] * b[i];
        }
        return result
    }
}

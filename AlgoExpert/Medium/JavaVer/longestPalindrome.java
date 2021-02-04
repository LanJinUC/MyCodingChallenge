import java.util.*;

class Program {
  public static String longestPalindromicSubstring(String str) {
    int[] currentLongestIndex = {0,1};
		
		for(int i = 1; i < str.length(); i++){
			int[] odd = searchForPalindrome(str, i - 1, i + 1);
			int[] even = searchForPalindrome(str, i - 1, i);
			int[] longest = longerString(odd, even);
			currentLongestIndex = longerString(currentLongestIndex, longest);
		}

		return str.substring(currentLongestIndex[0], currentLongestIndex[1]);
		
  }
	
	public static int[] searchForPalindrome(String str, int leftIndex, int rightIndex){
		while (leftIndex >= 0 && rightIndex < str.length()){
			if (str.charAt(leftIndex) != str.charAt(rightIndex)){
				break;
			}	
			leftIndex--;
			rightIndex++;
		}		
		return new int[] {leftIndex + 1, rightIndex};
	}
	
	public static int[] longerString(int[] firstIndexArray, int[] secondIndexArray){
		if(firstIndexArray[1] - firstIndexArray[0] > secondIndexArray[1] - secondIndexArray[0]){
			return firstIndexArray;
		}else{
			return secondIndexArray;
		}
	}
	
}


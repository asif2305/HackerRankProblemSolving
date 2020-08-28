import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class BeautifulBinaryString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

		String b="000001111111101010101";
		int cnt=0;
		for(int i=0;i<b.length();)
		{
			if(i<b.length()-2)
			{
				if(b.charAt(i) =='0' && b.charAt(i+1)=='1' && b.charAt(i+2)=='0')
				{
					cnt++;
					i=i+3;
				}
				else i++;
			}
			else i++;
			
		}
		System.out.println(cnt);
       
      
	
	}

}

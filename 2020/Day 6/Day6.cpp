#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	unordered_map<char,int> hm;
	int person = 0;
	int count1 = 0, count2 = 0;
	while(getline(cin,s))
	{
		if(s=="")
		{
			count1 += hm.size();
			for(auto it: hm)
			{
				if(it.second == person)
					count2++;
			}
			person = 0;
			hm.clear();
		}
		else
		{
			for(int i=0; i<s.size();i++) hm[s[i]]++;
			person++;
		}
	}
	if(!s.empty())
	{
		count1 += hm.size();
		for(auto it: hm)
			if(it.second == person) count2++;
	}
	cout<<"Puzzle1: "<<count1<<endl<<"Puzzle2: "<<count2;
	return 0;
}
#include <bits/stdc++.h>
using namespace std;
using T = tuple<int,int,int,int>;
void solve(vector<string>& s)
{
	map<T,char> space;
	for(int y=0; y<s.size(); y++)
	{
		for(int x=0; x<s[y].size();x++)
		{
			if(s[y][x] == '#')
				space[make_tuple(x,y,0,0)] = '#';
		}
	}
	
	for (int i=0; i<6; i++)
	{
		map<T,int> marked;
		for(auto it: space)
		{
				for(int z=-1; z<=1; z++)
				{
					for(int y=-1; y<=1; y++)
					{
						for(int x=-1; x<=1; x++)
						{
                            for(int w=-1; w<=1; w++)
							{
                                if(w==x && x==y && y==z && z==0) continue;
                                marked[make_tuple(get<0>(it.first)+x,get<1>(it.first)+y,get<2>(it.first)+z, get<3>(it.first)+w)]+=1;
                            }
                        }
					}
				}
			
		}
		map<T,char> new_space;
		for(auto it: marked)
		{
			if(it.second==3)
				new_space[it.first] = '#';
		}
		
		for(auto it: space)
		{
			if(marked[it.first] == 2 || marked[it.first]==3)
				new_space[it.first] = '#';
		}
		
		space = new_space;
	}
	
	cout<<"Part 2: "<<space.size();
}
int main() {
	string s;
	vector<string> space;
	while(getline(cin,s))
	{
		space.push_back(s);
	}
	solve(space);
	return 0;
}
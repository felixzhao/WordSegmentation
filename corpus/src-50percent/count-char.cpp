#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int cmp(const pair<wstring,int>& x,const pair<wstring,int>& y)   
{   
	return x.second>y.second;   
}  


void sortMapByValue(map<wstring,int>& tMap,vector<pair<wstring,int> >& tVector)   
{   
	for(map<wstring,int>::iterator curr=tMap.begin();curr!=tMap.end();curr++)   
	{   
		tVector.push_back(make_pair(curr->first,curr->second));   
	}   
	sort(tVector.begin(),tVector.end(),cmp);   
}

map<wstring,int> counter;

int main()
{
	locale::global(locale("en_US.UTF-8"));

	//wifstream inf("test-sep.txt");
	//wofstream ouf("test-word.txt");
	wifstream inf("train-sep.txt");
	wofstream ouf("train-word.txt");


	wstring s;

	while (inf >> s)
	{
		if (counter.count(s)==0)
			counter[s]=1;
		else
			counter[s]++;
	}

	vector<pair<wstring,int> > tVector;
	sortMapByValue(counter,tVector);

	//for (int i=0;i<tVector.size();i++)
	//	ouf << tVector[i].first << ' ' << tVector[i].second << endl;

	for (int i=0;i<tVector.size();i++)
		ouf << tVector[i].first << endl;

}

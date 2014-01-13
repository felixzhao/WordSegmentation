#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	//freopen("train.txt","r",stdin);
	//freopen("train-sep.txt","w",stdout);

	locale::global(locale("en_US.UTF-8"));

	wifstream fin("test.txt");
	wofstream fout("test-sep.txt");

	wstring s;
	wchar_t ch;
	
	while (getline(fin,s))
	{
		for (int i=0;i<s.length();i++)
			s.insert(++i,L" ");
		fout << s << endl;
	}
}

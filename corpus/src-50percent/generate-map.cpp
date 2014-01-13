#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <memory.h>
#include <map>
using namespace std;

//设为未知字符的个数
int count=2000;
//未知字符编号
bool number[6000];
//Cut off rare words
int cutnum = 4787;

map<wstring,int> unk;
void generate_random()
{
	memset(number,0,sizeof number);
	int num=0;
	srand(time(NULL));

	while (num<count)
	{
		//int i=rand()%5113 + 57;
		int i=rand()%193 + 1;
		if (!number[i])
			num++;
		number[i]=true;
	}
}

int main()
{
	locale::global(locale("en_US.UTF-8"));
	wifstream inf("test-word-count.txt");
	wofstream ouf("word-map.txt");

	//generate_random();

	wstring s;
	int i=0;
	while (inf >> s)
	{
		ouf << s;
		if (i<cutnum && (++i)%2 == 0)
		{
			ouf << " <unk>" << i;
			unk[s]=i;
		}
		else
			unk[s]=0;
		ouf << endl;
		inf >> s;
	}

	wifstream inf2("test-sep.txt");
	wofstream ouf2("test-unknown.txt");

	wstring line;
	while (getline(inf2,line))
	{
		while (line.length())
		{
			s=line.substr(0,line.find(' '));
			line.erase(0,line.find(' ')+1);
			if (unk[s])
				ouf2 << "<unk>" << unk[s];
			else
				ouf2 << s;
			ouf2 << ' ';
		}
		ouf2 << endl;
	}
}

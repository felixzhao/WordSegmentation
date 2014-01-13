#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;

int bestNum = 10;
int main(int argc, char* argv[])
{
	locale::global(locale("en_US.UTF-8"));

	string inf_str = "result-new.txt";
	string ouf_str = "stats-new.txt";
	if (argc>1)
			inf_str = string(argv[1]);
	if (argc>2)
			ouf_str = string(argv[2]);
	wifstream inf(inf_str.c_str());
	wofstream ouf(ouf_str.c_str());

	int i,j;
	int wordcount = 0;
	int res[2000];
	memset(res,0,sizeof res);

	wstring s;
	wstring ori;
	while (1)
	{
		if (!(inf >> ori))
			break;
		inf >> s;
		wordcount++;

		for (i=1;i<=bestNum;i++)
		{
			inf >> s;
			if (s==ori)
			{
				res[i]++;
				break;
			}
			inf >> s >> s;
		}
		if (inf.get()!='\n')
			inf.ignore(1024,'\n');
	}

	double ans=0;
	for (i=1;i<=bestNum;i++)
		ans+=(double)res[i]/i;

	ouf << L"共" << wordcount << L"个未知字符" << endl;
	ouf << L"总分数：" << ans << endl;
	for (i=1;i<=bestNum;i++)
		ouf << L"第" << i << L"位候选命中" << res[i] << L"个字符" << endl;
	ouf.close();
}

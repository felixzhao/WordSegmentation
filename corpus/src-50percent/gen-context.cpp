#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int find_back(wstring& line,wstring& unk,int pos)
{
	int start;
	int count=0;
	for (start=line.rfind(' ',pos);count<=3 && start!=string::npos && line.substr(start+1,line.find(' ',start+1)-start-2)!=unk;start=line.rfind(' ',start-1))
	count++;
	
	if (start==string::npos) return 0;
	return start+1;
}

int find_forward(wstring& line,wstring& unk,int pos)
{
	int start;
	int count=0;
	for (start=line.find(' ',pos);count<=3 && start!=string::npos && line.substr(line.rfind(' ',start-1)+1,start-line.rfind(' ',start-1)-2)!=unk;start=line.find(' ',start+1))
	count++;
	
	if (start==string::npos) return line.length()-1;
	return start-1;
}

void gen_context(vector<wstring> &text,wstring unk,wofstream& ouf)
{
	wstring str;
	for (int i=0;i<text.size();i++)
	{
		int pos = 0;
		wstring& line = text[i];
		while ((pos=line.find(unk,pos))!=string::npos)
		{
			int start = find_back(line,unk,pos);
			int dest = find_forward(line,unk,pos);
			ouf << line.substr(start,dest-start+1) << endl;
			pos++;
		}
	}
}

const char* testUnkStr="test-unknown.txt";
vector<wstring> text;

int main()
{
	locale::global(locale("en_US.UTF-8"));
	wifstream testUnkinf(testUnkStr);
	wofstream contextUnk("context-unknown.txt");

	wstring line;
	while (getline(testUnkinf,line))
		text.push_back(line);

	gen_context(text,L"<unk>2,103",contextUnk);
}

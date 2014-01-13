#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <unistd.h>
#include <cstdlib>
#include <sys/wait.h>
#include <errno.h>
using namespace std;

vector<wstring> trainword;

const char* testUnkStr="test-unknown.txt";
const char* wordmapStr="word-map.txt";
const char* trainwordStr="train-word.txt";

class wordppl
{
public:
	wstring str;
	double ppl;
	wordppl(wstring s,double p):str(s),ppl(p)
	{}
};

//Overload the < operator.
bool operator< (const wordppl& x, const wordppl& y)
{
	return x.ppl > y.ppl;
}

void replace_text(const wstring& src,const wstring& dest,wifstream& inf,wofstream& ouf)
{
	wstring line;
	int len=src.length();
	while (getline(inf,line))
	{
		int pos;
		while ((pos=line.find(src))!=string::npos)
			line.replace(pos,len,dest);
		ouf << line << endl;
	}
}

double string_to_double( const std::string& s )
{
	std::istringstream i(s);
	double x;
	if (!(i >> x))
		return 0;
	return x;
} 

void find_best(wifstream& testUnkinf,const wstring& unk,priority_queue<wordppl,vector<wordppl>,less<vector<wordppl>::value_type> >& res, priority_queue<wordppl,vector<wordppl>,less<vector<wordppl>::value_type> >& log_heap)
{
	for (vector<wstring>::iterator i=trainword.begin();i!=trainword.end();i++)
	{
		testUnkinf.clear();
		testUnkinf.seekg(ios::beg);
		wofstream tempouf("temp");
		replace_text(unk,*i,testUnkinf,tempouf);
		tempouf.close();

		int mypipe[2];
		if (pipe(mypipe))
		{
			cerr << "Error while piping." << endl;
			exit(1);
		}

		int pid=fork();
		if (pid<0)
		{
			cerr << "Error while forking." << endl;
			exit(1);
		}
		if (pid==0)
		{
			//Child
			close(mypipe[0]);
			close(1);

			dup2(mypipe[1],STDOUT_FILENO);

			execlp("/home/phoenix/oracle/SRILM/bin/i686-m64/ngram","ngram","-lm","/home/phoenix/oracle/corpus/train.lm","-ppl","temp",NULL);

			close(mypipe[1]);
			exit(0);
		}
		if (pid>0)
		{
			wait(NULL);

			close(mypipe[1]);

			char buffer[65536];
			read(mypipe[0],buffer,65536);
			string tmp(buffer);
			//string tmp2=tmp;

			close(mypipe[0]);

			tmp.erase(0,tmp.find("ppl=")+5);
			tmp.erase(tmp.find(' '));

			double ppl=string_to_double(tmp);
			res.push(wordppl(*i,ppl));

//			tmp2.erase(0,tmp2.find("logprob=")+9);
//			tmp2.erase(tmp2.find(' '));
//
//			double logp=string_to_double(tmp2);
//			log_heap.push(wordppl(*i,logp));
		}
	}
}

int main(int argc,char* argv[])
{
	locale::global(locale("en_US.UTF-8"));
	wifstream testUnkinf(testUnkStr);
	wifstream wordmapinf(wordmapStr);
	wifstream trainwordinf(trainwordStr);

	wofstream resouf("result.txt");

	//Read words in train data
	wstring tmp;
	while (getline(trainwordinf,tmp))
		trainword.push_back(tmp);

	//Read unknown words in test data
	wstring origin,unk;
	while (getline(wordmapinf,origin))
	{
		if (origin.find(L' ')==string::npos)
			continue;
		int pos=origin.find(L' ');
		int len=origin.length();
		unk=origin.substr(pos+1,len-pos-1);
		origin.erase(pos+1);

		priority_queue<wordppl,vector<wordppl>,less<vector<wordppl>::value_type> > res_heap;
		priority_queue<wordppl,vector<wordppl>,less<vector<wordppl>::value_type> > log_heap;
		find_best(testUnkinf,unk,res_heap,log_heap);

		resouf << origin << ":  ";	
		for (int i=0;res_heap.size();i++)
		{
			resouf << res_heap.top().str << ' ' << res_heap.top().ppl << " | ";
			res_heap.pop();
		}
		resouf << endl << endl;
		break;
	}

}

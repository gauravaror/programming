#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


/*
 * Complete the implementation of the IntervalLimiter class.
 */
class IntervalLimiter
{
public:

    map<unsigned long, long> running_average;
    map<unsigned long, long> outputs;
    unsigned long limits;
    unsigned long interval_;
    unsigned long oldtime;
    long my_value;
    long timeminusone;

    IntervalLimiter(unsigned long limit, unsigned long interval)
    {
	limits = limit;
	interval_ = interval;
	oldtime = 0;
	my_value = 0;
	timeminusone = 0;
    }

    /* Return the limited value. */
    long apply(long value, unsigned long monotonic_time)
    {
	if (oldtime != monotonic_time) {
	    if (!(oldtime == 0)) {
		  outputs.insert(std::pair<unsigned long, long>(oldtime, my_value));
	    }
	    timeminusone += my_value;
	    //cout<<"ol "<<oldtime<<"  "<<monotonic_time<<endl;
	    for (unsigned long ti = oldtime; ti < monotonic_time; ti++) {
	      //cout<<"Inserting "<<ti<<endl;
	      running_average.insert(std::pair<unsigned long, long>(ti, timeminusone));
	    }
	    oldtime = monotonic_time;
	    my_value = 0;
	}

	long oldvalue = 0;
	unsigned long old_reference_time = monotonic_time - interval_;
	//cout<<"Finding "<<old_reference_time<<" "<<interval_<<endl;
	auto oldref = running_average.find(old_reference_time);
	if (oldref != running_average.end()) {
	    oldvalue = oldref->second;
	}
	long newvalue = my_value + abs(value);
	if (newvalue + timeminusone - oldvalue > limits) {
	    long removeval = newvalue + timeminusone - oldvalue - limits;
	    my_value = newvalue - removeval;
	} else {
	    my_value = newvalue;
	}
	//cout<<value<<" "<<monotonic_time<<" "<<my_value<<"   fs   "<<newvalue<<"  "<<timeminusone << "  " << oldvalue<<endl;
	if (value > 0) {
	    //cout<<my_value<<endl;
	    return my_value;
	} else {
	    //cout<<-1*my_value<<endl;
	    return -1*my_value;
	}
    }
};


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string line_temp;
    getline(cin, line_temp);
    vector<string> line = split(rtrim(line_temp));
    unsigned long limit = stoul(ltrim(line[0]));
    unsigned long interval = stoul(ltrim(line[1]));

    getline(cin, line_temp);
    unsigned int event_count = stoi(ltrim(rtrim(line_temp)));

    IntervalLimiter limiter(limit, interval);
    vector<long> result;
    result.reserve(event_count);

    for (unsigned int i = 0; i < event_count; i++)
    {
        string row_temp;
        getline(cin, row_temp);
        vector<string> row = split(rtrim(row_temp));

        long value = stol(ltrim(row[0]));
        unsigned long monotonic_time = stoul(ltrim(row[1]));

        long limited_value = limiter.apply(value, monotonic_time);
        result.emplace_back(limited_value);
    }

    for (unsigned int i = 0; i < result.size(); i++)
    {
        fout << result[i];

        if (i != result.size() - 1)
        {
            fout << "\n";
        }
    }

    fout << "\n";
    fout.close();

    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str)
{
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos)
    {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

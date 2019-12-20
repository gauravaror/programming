#include<iostream>
#include<string>
#include <set>
#include<unordered_map>

using namespace std;

string get_freq_rep(int array[], int length) {
    string string_rep = "";
    for (int j=0;j < length;j++) {
	string_rep = string_rep +  to_string(array[j]);
    }
    return string_rep;
}
using namespace std;

int mod_operation(int x, int mod) {
	int data  = x % mod;
	if (data < 0) {
		data = data + mod;
	}
	return data;
}	

long do_mod(long x, long p) {
		long mo = x % p;
		if (mo < 0) {
			return (mo + p);
		} else {
			return mo;
		}
	}

/* Iterative Function to calculate (x^y)%p in O(log y) */
int power(int x, unsigned int y, int p)
{
    int res = 1;      // Initialize result

    x = do_mod(x , p);  // Update x if it is more than or
                // equal to p

    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = do_mod((res*x),p);

        // y must be even now
        y = y>>1; // y = y/2
        x = do_mod((x*x),p);
    }
    return res;
}
	// This function is inspired from geeks4geeks after
	// it was posted on discussion board.
	   // To compute (a * b) % mod  
	    long mulmod(long a, long b,  
				    long mod) {
		long res = 0; // Initialize result  
		a = do_mod(a, mod); 
		b = do_mod(b, mod); 
	        //System.out.println("Current " + String.valueOf(res) + " "  + String.valueOf(a)  +  "  " + String.valueOf(b)); 	
		while (b > 0) 
		{ 
		    // If b is odd, add 'a' to result  
		    if (b % 2 == 1)  
		    { 
			res = do_mod(res + a, mod); 
		    } 
	  
		    // Multiply 'a' with 2  
		    a = do_mod((a * 2), mod); 
	  
		    // Divide b by 2  
		    b /= 2; 
	            //System.out.println("Current " + String.valueOf(res) + " "  + String.valueOf(a)  +  "  " + String.valueOf(b)); 	
		} 
	 
	        //System.out.println("Current " + String.valueOf(res) + " "  + String.valueOf(a)  +  "  " + String.valueOf(b)); 	
		// Return result  
		return do_mod(res, mod); 
	    } 
	  

string build_prof_string(int N, int A, int B, int C, int D, char s1, char s2) {
    string prof_string = "";
    prof_string += s1;
    prof_string += s2;
    int x1 = s1;
    int x2 = s2;
    for (int i = 2; i < N; i++) {
	//cout<<" A "<<A<<" x1 "<<x1<<" B "<<B<<" x2 "<<x2<<" C  "<<C<<" D "<<D<<endl;
	//int new_one = mod_operation(mod_operation((A*x2), D) + mod_operation(B*x1,D) + mod_operation(C, D), D);
	int new_one = do_mod(mulmod(A, x2, D) + mulmod(B, x1,D) + do_mod(C,D), D);
	//cout<<"Summation is this "<<mulmod(x2, A, D) <<" "<<mulmod(A, x2, D)<<endl;
	//cout<<"Without mod "<<new_one;
	//if (new_one < 0) new_one = new_one + D;
	//cout<<"new one "<<new_one<<endl;
	x1 = x2;
	x2 = new_one;
	prof_string += char(97 + (new_one %26));
    }
    return prof_string;
}

int main() {
int testcases;
int L,N,A,B,C,D;
char s1,s2;
cin>>testcases;
set<string> dictionary;
set<int>::iterator len_it;
unordered_map<string, int> oc_dictionary;
unordered_map<int, unordered_map<string, int>> length_container;
set<int> lengths;
	for (int i =0;i<testcases;i++) {
	    cin>>L;
	    length_container.clear();
	    //oc_dictionary.clear();
	    for (int j=0; j <L; j++) {
		    string new_word;
		    cin>>new_word;
		    int str_len = new_word.length();
		    char first = new_word[0];
		    char last = new_word[str_len-1];
		    int freq_vector[26] = {};
		    for (int i = 0; i< str_len; i++) {
			    freq_vector[new_word[i]-97] += 1;
		    }
		    string representation = get_freq_rep(freq_vector, 26) + first + last;
		    //cout<<"Input length"<< str_len<<" input represenation "<<representation<<" new word "<<new_word<<endl;
		    lengths.insert(str_len);
		    if (length_container.find(str_len) != length_container.end()) {
		        oc_dictionary = length_container[str_len];
		    } else {
			unordered_map<string, int> new_map;
			oc_dictionary = new_map;
		    }
		    dictionary.insert(representation);
		    if (oc_dictionary.find(representation) != oc_dictionary.end()) {
			    oc_dictionary[representation] += 1;
		    } else {
			    oc_dictionary[representation] = 1;
		    }
		    length_container[str_len] = oc_dictionary;

	    }
	    cin>>s1>>s2>>N>>A>>B>>C>>D;
	    string prof_string = build_prof_string(N, A, B, C, D, s1, s2);
	    //cout<<"Professor string "<<prof_string<<endl;
	    int found_elements = 0;
	//cout<<"Length container size"<<length_container.size()<<endl;
	for (len_it=lengths.begin(); len_it!=lengths.end(); ++len_it) {
	    int current_length = *len_it;
	    //cout<<"Current length "<<current_length<<endl;
	    int fvector[26] = {};
	    string freq_rep;
	    int run_max=N-current_length+1;
	   oc_dictionary = length_container[current_length];
	   //cout<<"This length dictionary size"<<oc_dictionary.size()<<endl;
	    for (int i=0; i <run_max; i++) {
		    if (i==0) {
		        string new_string = prof_string.substr(0, current_length);
		        int str_len = new_string.length();
		        char first = new_string[0];
		        char last = new_string[str_len-1];
		        for (int i = 0; i< str_len; i++) {
			    fvector[new_string[i]-97] += 1;
		        }
		    	freq_rep = get_freq_rep(fvector, 26) + first + last;
		    } else {
			int remove = prof_string.at(i-1) - 97;
			int add = prof_string.at(i+current_length-1) - 97;
			fvector[remove] -= 1;
			fvector[add] += 1;
			freq_rep = get_freq_rep(fvector,26) + prof_string.at(i) + prof_string.at(i+current_length-1);
		    }
		    auto elmfound = oc_dictionary.find(freq_rep);
		    //cout<<"Checkinf Represenation"<<freq_rep<<endl;
		    if (elmfound != oc_dictionary.end()) {
			found_elements += elmfound->second;
			//cout<<"Found representation "<<freq_rep <<" matched with "<<elmfound->first<<"  "<<found_elements<<endl;
			oc_dictionary.erase(freq_rep);
		    }
		    if (oc_dictionary.size() == 0) break;
	    }
	}
	cout<<"Case #"<<i+1<<": "<<found_elements<<endl;
	}
}


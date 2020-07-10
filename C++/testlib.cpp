#include <iostream>
#include <regex>
#include <string>

using namespace std;


extern "C" void hello_world() {
    cout << "Hello world!\n";
}


extern "C" int multiply_by_2(int n) {
    return n * 2;
}

extern "C" int add(int a, int b) {
    return a + b;
}

extern "C" char* get_string() {
    string s = "Test";
    return &s[0];
}

extern "C" char* get_obj_id(char* ss) {
    string s = ss;
    smatch matches;
    regex pattern {"\\d+"};
    if (regex_search(s, matches, pattern)) {
        string obj_id = matches[0];
        return &obj_id[0];
    }
    string output = "?";
    return &output[0];
}

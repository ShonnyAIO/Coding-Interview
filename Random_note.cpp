#include <iostream>

using namespace std;

bool canConstruct_bruteforce(std::string note, std::string magazine)
{
if(note.size() > magazine.size())
return false;
for (int i = 0; i < note.size(); i++)
{
if (0 == magazine.size())
return false;
std::size_t found = magazine.find(note[i]);
if (found == std::string::npos)
return false;
magazine.erase(found, 1);
}
return true;
}

bool canConstruct_map(std::string note, std::string magazine)
{
if(note.size() > magazine.size())
return false;
typedef std::map TypeDict;
TypeDict dict;

for (size_t i = 0; i < magazine.size(); i++)
{
TypeDict::iterator itDict = dict.find(magazine[i]);
if (itDict == dict.end())
dict.emplace(magazine[i], 1);
else
itDict->second++;
}

for (size_t i = 0; i < note.size(); i++)
{
TypeDict::iterator itDict = dict.find(note[i]);
if (itDict == dict.end())
return false;
else if(--itDict->second < 0)
return false;
}

return true;
}

int main()
{

std::string note = "aabac";
std::string magazine = "aabacd";
std::cout << canConstruct_bruteforce(note, magazine) << std::endl;
std::cout << canConstruct_map(note, magazine) << std::endl;

return 0;
}
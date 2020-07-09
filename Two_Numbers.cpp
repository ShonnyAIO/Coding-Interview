typedef std::pair myPair;
typedef std::map ma;

void myPrintPair(myPair indexes)
{
std::cout << "[ " << indexes.first << ", " << indexes.second << " ]\n";

}

void solution()
{
myPair indexes;

int a[4] = {2,7,11,15};
int target = 9;
ma mapIndexes;
for (size_t i = 0; i < 4; i++)
{
int val = a[i];
auto it = mapIndexes.find(target - val);
if (it != mapIndexes.end())
{

myPrintPair(myPair(it->second, i));
}
mapIndexes.insert(myPair(val, i));
}
}
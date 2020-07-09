typedef std::pair myPair;

void printResult(myPair p)
{
std::cout << "[ " << p.first << ", " << p.second << " ]\n";
}

myPair binarySearchIterative(const int* arr, const int target, int low, int high, int size)
{
int mid = 0;
myPair p(0, 0);
bool findlow = true;

while (true)
{
if (high < low)
{
return myPair(0, 0);
}

mid = low + (high - low) / 2;

if (findlow)
{
if ((mid == 0 || target != arr[mid - 1]) && target == arr[mid])
{
p.first = mid;
findlow = false;
low = mid;
high = size - 1;
}
else if (target > arr[mid])
low = mid + 1;
else
high = mid - 1;
}
else
{
if ((mid == size - 1 || target != arr[mid + 1]) && target == arr[mid])
{
p.second = mid;
break;
}
if (target < arr[mid])
high = mid - 1;
else
low = mid + 1;
}
}
return p;
}

void solutionFirstAndLastIndex()
{
const int size = 15;
const int arr[size]{ 1,3,3,5,7,8,9,9,9,10,11,12,13,14,15 };
int target = 15;

printResult(binarySearchIterative(arr, target, 0, size - 1, size));
}
#include <stdio.h>

using namespace std;

class TestTree
{
public:
TestTree(int v) : val(v), left(nullptr), right(nullptr) {};
int val;
TestTree* left;
TestTree* right;
};

bool isValidTree(TestTree* tr, int lover, int upper)
{
if (!tr)
return true;
int val = tr->val;
if (val <= lover || val >= upper)
return false;
if (!isValidTree(tr->right, val, upper))
return false;
if (!isValidTree(tr->left, lover, val))
return false;
return true;
}

int main()
{
TestTree testtree(5);
testtree.left = new TestTree(7);
testtree.right = new TestTree(4);
std::cout << isValidTree(&testtree,
std::numeric_limits::min(),
std::numeric_limits::max());

return 0;
}
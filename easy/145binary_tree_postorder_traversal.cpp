// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> postorderTraversal(TreeNode *root)
    {
        /*
                a
            b       c
        d     e   f    g

        postorder:
        left right root
        (d e b) (f g c) a

        preorder:
        root left right
        a (b d e) (c f g)

        inorder:
        left root right
        (d b e) a (f c g)
        */
        /*
        stack<int> st = [root]
        curr = root
        while(!st.empty()) {
            curr = st.pop() //what node we're processing *as* the root

        }*/

        if (root == nullptr)
        {
            return {};
        }
        else
        {
            vector<int> v1 = postorderTraversal(root->left);
            vector<int> v2 = postorderTraversal(root->right);
            v1.insert(v1.end(), v2.begin(), v2.end());
            v1.push_back(root->val);
            return v1;
        }
    }
};
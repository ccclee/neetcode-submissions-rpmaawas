/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    bool isValidHelper (TreeNode* node, int small, int big){
        if (node ==nullptr){
            return true;
        }
        if (node->val <=small || node->val >=big){
            return false;
        }
        return isValidHelper(node->left, small, node->val)&& isValidHelper(node->right, node->val, big);
    }
public:
    bool isValidBST(TreeNode* root) {

        return isValidHelper(root, -1001,1001);
        
    }
};

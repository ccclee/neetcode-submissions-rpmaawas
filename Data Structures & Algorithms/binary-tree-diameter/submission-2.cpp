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
    int maxdiameter =0;

    int diameter (TreeNode* node){
            if (node == nullptr){
                return 0;
            }
            int left = diameter(node->left);
            int right = diameter(node->right);
            maxdiameter = max(maxdiameter, left+right);
            return 1+ max(left,right);

        }

public:

    int diameterOfBinaryTree(TreeNode* root) {

        diameter(root);
        return maxdiameter; 
    }

    

};

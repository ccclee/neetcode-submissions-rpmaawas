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
public:
    int kthSmallest(TreeNode* root, int k) {
        TreeNode* curr = root;
        stack<TreeNode*> nodes;
        int count =0;
        while (curr!= nullptr || !nodes.empty()){
            while(curr!=nullptr){
                nodes.push(curr);
                curr = curr->left;
            }

            curr = nodes.top();
            nodes.pop();
            count+=1;
            if (count == k){
                return curr->val;
            }
            curr = curr->right;
        }
    }
};

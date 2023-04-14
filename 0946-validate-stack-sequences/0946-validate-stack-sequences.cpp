class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        stack < int > st;
        
        int popCounter = 0;
        
        int push_size = pushed.size();
        int pop_size = popped.size();
        
        for (int i = 0 ; i < push_size ; ++i)
        {
            st.push(pushed[i]);
            while(!st.empty() && popped[popCounter] == st.top() && popCounter < pop_size)
            {
                st.pop();
                popCounter++; 
            }
        }
        if (st.empty())
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
};
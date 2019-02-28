function [prob_val] = GetMarkovBlanketProbaility(node, node_val, parent_mat, child_mat, probabilities)
    node_val(node)=1;
    val = GetProbability(node, node_val, parent_mat, probabilities);
    if sum(parent_mat(node,:)==1)~=0
        for i=1:size(node_val)
            if child_mat(node,i)
                val = val*GetProbability(i, node_val, parent_mat, probabilities);
            end
        end
    end
    
    node_val(node)=2;
    neg_val = GetProbability(node, node_val, parent_mat, probabilities);
    if sum(parent_mat(node,:)==1)~=0
        for i=1:size(node_val)
            if child_mat(node,i)
                neg_val = neg_val*GetProbability(i, node_val, parent_mat, probabilities);
            end
        end
    end
    
    prob_val = val/(val+neg_val);
end
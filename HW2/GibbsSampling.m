function [prob_val] = GibbsSampling(iterations, x, node_val, node_given, parent_mat, child_mat, probabilities)
    NodeVals = [];
    for iter=1:iterations
        [node, node_given] = GetNode(node_val, node_given, parent_mat, "random");
        rand_num = rand();
        [prob_val] = GetMarkovBlanketProbaility(node, node_val, parent_mat, child_mat, probabilities);
        if rand_num>prob_val
            node_val(node) = 2;
        else
            node_val(node) = 1;
        end
        NodeVals = [NodeVals node_val];
    end
    prob_val = sum(NodeVals(x,:)==1)/size(NodeVals,2);
end
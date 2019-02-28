function [prob_val] = LikelihoodWeighting()
    Node_Vals = [];
    W = [];
    for iter=1:100
        node_val = zeros(Vertices,1);
        node_visited = zeros(Vertices,1);
        node_val(K)=1; node_val(B)=2; node_val(C)=1;
        w=1;
        for i=1:Vertices
            [node, node_visited] = GetNode(node_val, node_visited, parent_mat, "order");
            if node_val(node)
                prob_val = GetProbability(node, node_val, parent_mat, probabilities);
                w = w*prob_val;
            else
                rand_num = rand();
                prob_val = GetProbability(node, node_val, parent_mat, probabilities);
                if rand_num>prob_val
                    node_val(node)=2;
                else
                    node_val(node)=1;
                end
            end
        end
        Node_Vals = [node_val Node_Vals];
        W = [w W];
    end

    sum(Node_Vals(7,:)==1)
    sum(Node_Vals(7,:)==2)
    sum(Node_Vals(7,:)==0)
end
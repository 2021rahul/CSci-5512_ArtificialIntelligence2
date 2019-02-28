function [node, node_visited] = GetNode(node_val, node_visited, parent_mat, order)
    if order == "order"
        for i=1:size(node_val,1)
            if node_visited(i)==0
                if all(node_val(parent_mat(i,:)~=0))
                    node = i;
                    node_visited(i)=1;
                    break;
                end
            end
        end
    elseif order == "random"
        node = randi([1 11], 1);
        while (node_visited(node)==1)
            node = randi([1 10], 1);
        end
    end
end
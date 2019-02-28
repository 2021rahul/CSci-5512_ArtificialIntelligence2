function [prob_val] = GetProbability(node, node_val, parent_mat, probabilities)
    probability = probabilities(int2str(node));
    probability = probability(:);
    to_check = zeros(size(node_val,1),1);
    to_check(parent_mat(node,:)==1)=1;
    if node_val(node)==0
        if sum(to_check==1)==0
            prob_val = probability(1);
        else
            prob_val = probability(power2array([1 node_val(to_check==1)']));
        end
    else
        if sum(to_check==1)==0
            prob_val = probability(node_val(node));
        else
            prob_val = probability(power2array([node_val(node) node_val(to_check==1)']));
        end
    end
end

function [val] = power2array(array)
    val=1;
    for i=1:size(array,2)
        val = val + (pow2(i-1)*(array(i)-1));
    end
end

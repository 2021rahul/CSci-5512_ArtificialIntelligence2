Vertices = 11;
A=1; B=2; C=3; D=4; E=5; F=6; G=7; H=8; I=9; J=10; K=11;
[parent_mat, child_mat, probabilities] = BayNet();

Node_Vals = [];
W = [];
for iter=1:100000
    node_val = zeros(Vertices,1);
    node_visited = zeros(Vertices,1);
    node_val(K)=1; node_val(B)=2; node_val(C)=1;
    w=1;
    for i=1:Vertices
        [node, node_visited] = GetNode(node_val, node_visited, parent_mat);
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

prob_val = sum(W(Node_Vals(G,:)==1))/sum(W)

%%

function [node, node_visited] = GetNode(node_val, node_visited, parent_mat)
    for i=1:size(node_val,1)
        if node_visited(i)==0
            if all(node_val(parent_mat(i,:)~=0))
                node = i;
                node_visited(i)=1;
                break;
            end
        end
    end
end

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

function [parent_mat, child_mat, probabilities] = BayNet()
    Vertices=11;
    A=1; B=2; C=3; D=4; E=5; F=6; G=7; H=8; I=9; J=10; K=11;
    
    parent_mat = zeros(Vertices);
    parent_mat(C,A)=1;
    parent_mat(D,A)=1;
    parent_mat(E,B)=1;
    parent_mat(G,C)=1;parent_mat(G,D)=1;parent_mat(G,E)=1;
    parent_mat(H,E)=1;
    parent_mat(I,F)=1;parent_mat(I,G)=1;
    parent_mat(J,G)=1;parent_mat(J,H)=1;
    parent_mat(K,I)=1;
    
    child_mat = zeros(Vertices);
    child_mat(A,C)=1; child_mat(A,D)=1;
    child_mat(B,E)=1;
    child_mat(C,G)=1;
    child_mat(D,G)=1;
    child_mat(E,G)=1;child_mat(E,H)=1;
    child_mat(F,I)=1;
    child_mat(G,I)=1;child_mat(G,J)=1;
    child_mat(H,J)=1;
    child_mat(I,K)=1;
    
    probabilities = containers.Map;
    probabilities(int2str(A)) = [0.3 0.7];
    probabilities(int2str(B)) = [0.6 0.4];
    probabilities(int2str(C)) = [0.2 0.5; 0.8 0.5];
    probabilities(int2str(D)) = [0.8 0.4; 0.2 0.6];
    probabilities(int2str(E)) = [0.8 0.1; 0.2 0.9];
    probabilities(int2str(F)) = [0.5 0.5];
    p_var = zeros(2,2,2,2);
    p_var(1,1,1,1)=0.1;p_var(1,1,1,2)=0.2;p_var(1,1,2,1)=0.3;p_var(1,1,2,2)=0.4;
    p_var(1,2,1,1)=0.5;p_var(1,2,1,1)=0.6;p_var(1,2,2,1)=0.7;p_var(1,2,2,2)=0.8;
    p_var(2,1,1,1)=0.9;p_var(2,1,1,2)=0.8;p_var(2,1,2,1)=0.7;p_var(2,1,2,2)=0.6;
    p_var(2,2,1,1)=0.5;p_var(2,2,1,1)=0.4;p_var(2,2,2,1)=0.3;p_var(2,2,2,2)=0.2;
    probabilities(int2str(G)) = p_var;
    probabilities(int2str(H)) = [0.4 0.7; 0.6 0.3];
    p_var = zeros(2,2,2);
    p_var(1,1,1)=0.8;p_var(1,1,2)=0.6;p_var(1,2,1)=0.4;p_var(1,2,2)=0.2;
    p_var(2,1,1)=0.2;p_var(2,1,2)=0.4;p_var(2,2,1)=0.6;p_var(2,2,2)=0.8;
    probabilities(int2str(I)) = p_var;
    p_var = zeros(2,2,2);
    p_var(1,1,1)=0.2;p_var(1,1,2)=0.7;p_var(1,2,1)=0.9;p_var(1,2,2)=0.1;
    p_var(2,1,1)=0.8;p_var(2,1,2)=0.3;p_var(2,2,1)=0.1;p_var(2,2,2)=0.9;
    probabilities(int2str(J)) = p_var;
    probabilities(int2str(K)) = [0.3 0.7; 0.7 0.3];
end

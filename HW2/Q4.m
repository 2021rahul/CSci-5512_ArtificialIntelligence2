Vertices = 11;
A=1; B=2; C=3; D=4; E=5; F=6; G=7; H=8; I=9; J=10; K=11;
[parent_mat, child_mat, probabilities] = BayNet();

x = G;
evidence = [B C K];

node_val = randi([1 2], [Vertices 1]);
for i=1:size(evidence,2)
    node_val(evidence(i))=1;
end

node_given = zeros(Vertices,1);
for i=1:size(evidence,2)
    node_given(evidence(i))=1;
end

prob_val = GibbsSampling(100, x, node_val, node_given, parent_mat, child_mat, probabilities);

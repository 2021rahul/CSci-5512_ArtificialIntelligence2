Vertices = 11;
A=1; B=2; C=3; D=4; E=5; F=6; G=7; H=8; I=9; J=10; K=11;

[parent_mat, child_mat, probabilities] = BayNet();

%%
node=G;
node_val = ones(Vertices,1);
[value] = GetMarkovBlanketProbaility(node, node_val, parent_mat, child_mat, probabilities);
%%
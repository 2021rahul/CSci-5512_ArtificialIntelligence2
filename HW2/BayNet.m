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
A = imread("1.png");
B = A*0;
figure,imshow(A)
A2 = imnoise(A,'salt & pepper',0.1);
A3 = imresize(A2,0.5);

Ra = A3(:, :, 1);
Ga = A3(:, :, 2);
Ba = A3(:, :, 3);
[p,l] = size(Ra);

Rb = B(:, :, 1);
Gb = B(:, :, 2);
Bb = B(:, :, 3);
[p2,l2] = size(Rb);

rp = p2-p;
rl = l2-l;

startP = randi(rp);
startL = randi(rl);

for i=1:p
    for j=1:l
        Rb(startP+i,startL+j) = Ra(i,j);
        Gb(startP+i,startL+j) = Ga(i,j);
        Bb(startP+i,startL+j) = Ba(i,j);
    end    
end    

Bresult = cat(3,Rb,Gb,Bb);

%A4 = imrotate(A3,5);
figure,imshow(Bresult)

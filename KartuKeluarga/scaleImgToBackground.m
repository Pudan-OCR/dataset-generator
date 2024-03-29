function [result, startP, startL] = scaleImgToBackground(img,B,scaling)
    A3 = imresize(img,scaling);    
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
            if((Ra(i,j)~=122) || (Ga(i,j)~=122) ||(Ba(i,j)~=122))
                Rb(startP+i,startL+j) = Ra(i,j);
                Gb(startP+i,startL+j) = Ga(i,j);
                Bb(startP+i,startL+j) = Ba(i,j);
            end
        end    
    end    
    
    result = cat(3,Rb,Gb,Bb);
    %tempel hasil gambar ke background

end
function result = changBackground(img)
    Ra = img(:, :, 1);
    [p,l] = size(Ra);
    Ga = img(:, :, 2);
    Ba = img(:, :, 3);
    
    for i=1:p
        for j=1:l
            if (Ra(i,j)==0 && Ga(i,j)==0 && Ba(i,j)==0)
                Ra(i,j)=122;
                Ba(i,j)=122;
                Ga(i,j)=122;
            else
                break
            end
        end
    end
    
    for i=1:p
        for j=l:-1:1
            if (Ra(i,j)==0 && Ga(i,j)==0 && Ba(i,j)==0)
                Ra(i,j)=122;
                Ba(i,j)=122;
                Ga(i,j)=122;
            else
                break
            end
        end
    end
    
    result = cat(3,Ra,Ga,Ba);
    

end
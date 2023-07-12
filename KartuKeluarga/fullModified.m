function [scaling, startP, startL] = fullModified(imgPath,backgroundPath)
    img = imread(imgPath);
    imgBg = imread(backgroundPath);
    [pBg,lBg] = size(imgBg);
    imgTempered = changBackground(img);
    [p,l] = size(imgTempered);
    prob = (0.02 * randi(100) / 100);
    if(pBg/p < lBg/l)
        scaling = (pBg/p)-0.001-prob;
    else
        scaling = (lBg/l)-0.001-prob;
    end
    [resultImg, startP, startL] = scaleImgToBackground(imgTempered,imgBg,scaling);
    imwrite(resultImg,imgPath)
end
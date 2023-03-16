function result = fullModified(imgPath,backgroundPath,dense,angle)
    img = imread(imgPath);
    imgBg = imread(backgroundPath);
    [pBg,lBg] = size(imgBg);
    imgTempered = addNoise(img,dense);
    imgTempered = rotateImg(imgTempered,angle);
    imgTempered = changBackground(imgTempered);
    [p,l] = size(imgTempered);
    scaling = 0.0;
    prob = (0.02 * randi(100) / 100);
    if(pBg/p < lBg/l)
        scaling = (pBg/p)-0.001-prob;
    else
        scaling = (lBg/l)-0.001-prob;
    end

    result = scaleImgToBackground(imgTempered,imgBg,scaling);
    imwrite(result,imgPath)
end
function result = addNoise(img,dense)
    result = imnoise(img,'salt & pepper',dense);
end


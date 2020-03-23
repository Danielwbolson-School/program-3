
sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [1]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_1light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [2]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_2light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [4]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_4light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [8]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_8light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [16]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_16light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [32]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_32light_64pixel.exr'

sed -i "/.*AreaLightSource.*/c\AreaLightSource \"area\" \"color L\" [200 200 200] \"integer nsamples\" [64]" "manykilleroos.pbrt"
./../pbrt-v3/build/Release/pbrt.exe "manykilleroos.pbrt" --outfile 'Results/manykilleroos_ld_64light_64pixel.exr'
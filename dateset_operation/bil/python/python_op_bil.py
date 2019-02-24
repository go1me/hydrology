#可以使用rasterio 这个包
#安装方法
#pip3 install rasterio
#help doc
#https://rasterio.readthedocs.io/en/latest
#使用方法分为命令行和python脚本
##命令行使用
##https://rasterio.readthedocs.io/en/latest/cli.html
##举个例子，查看info 
'''
rio info HWSD_RASTER/hwsd.bil --indent 2 --verbose
{
  "bounds": [
    -180.0,
    -89.99999999999997,
    179.99999999985602,
    89.99999999992804
  ],
  "checksum": [
    40437
  ],
  "colorinterp": [
    "undefined"
  ],
  "count": 1,
  "crs": null,
  "descriptions": [
    null
  ],
  "driver": "EHdr",
  "dtype": "uint16",
  "height": 21600,
  "indexes": [
    1
  ],
  "mask_flags": [
    [
      "all_valid"
    ]
  ],
  "nodata": null,
  "res": [
    0.00833333333333,
    0.00833333333333
  ],
  "shape": [
    21600,
    43200
  ],
  "stats": [
    {
      "max": 32050.0,
      "mean": 2206.1819814461164,
      "min": 0.0
    }
  ],
  "tiled": false,
  "transform": [
    0.00833333333333,
    0.0,
    -180.0,
    0.0,
    -0.00833333333333,
    89.99999999992804,
    0.0,
    0.0,
    1.0
  ],
  "units": [
    null
  ],
  "width": 43200
}

'''
#脚本使用
import rasterio
tmean = rasterio.open('HWSD_RASTER/hwsd.bil')
print(tmean.crs)
print(tmean.width)
print(tmean.height)
print(tmean.bounds)
print(tmean.read().shape)
print(tmean.read())

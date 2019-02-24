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
rio info HWSD_RASTER/hwsd.bil --indent 2

'''
#脚本使用
import rasterio
tmean = rasterio.open('HWSD_RASTER/hwsd.bil')
print(tmean.width)
print(tmean.height)
print(tmean.read().shape)




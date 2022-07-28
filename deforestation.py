

#Import all python lib.
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import matplotlib
import matplotlib.pyplot as plt 
import folium
import plotly_express as px
import os
import warnings
import datetime
warnings.filterwarnings('ignore')

from sentinelhub import (
    MimeType,
    CRS,
    BBox,
    SentinelHubRequest,
    SentinelHubDownloadClient,
    DataCollection,
    bbox_to_dimensions,
    DownloadRequest
)

#Input instance id and client id from the sentinel hub
#input aws iAM keys for access to my aws account
from sentinelhub import SHConfig

config = SHConfig()

config.instance_id = '******-d42e-42aa-8bea-*******' #instance id
config.sh_client_id = '****-dd23-4b63-9c23-******'  #sentinel hub client id
config.sh_client_secret = '*****RGep}DcjC~P|,g!(V&o#u******'  #sentinel hub secret
config.aws_access_key_id = '*****X75NI*****'  #aws access key
config.aws_secret_access_key = '*****sJpJcMwDUg90A*****'  #aws secret key

#Save configuration 
config.save()

#Input WFS to allow us to perform some data manipulation on different geographical locations
from sentinelhub import WebFeatureService, BBox, CRS, DataCollection, SHConfig
if config.instance_id == '':
    print("Warning! To use WFS functionality, please configure the `instance_id`.")

#Use Bbox to specify the geographical, first location is Bole National Park https://molenationalpark.org/
search_bbox = BBox(bbox=[-1.275444,6.926086,-1.242142,6.950283], crs=CRS.WGS84)
search_time_interval = ("2021-01-10T00:00:00", "2022-12-10T23:59:59")


wfs_iterator = WebFeatureService(
    search_bbox, search_time_interval, data_collection=DataCollection.SENTINEL2_L1C, maxcc=1.0, config=config
)

for tile_info in wfs_iterator:
    print(tile_info)

from sentinelhub import AwsTile

tile_id = 'S2A_OPER_MSI_L1C_TL_VGS2_20210126T123719_A029234_T30NXN_N02.09'
tile_name, time, aws_index = AwsTile.tile_id_to_tile(tile_id)
tile_name, time, aws_index




tile_id2 = 'S2B_OPER_MSI_L1C_TL_VGS2_20220106T122407_A025259_T30NXN_N03.01'
tile_name2, time2, aws_index2 = AwsTile.tile_id_to_tile(tile_id2)
tile_name2, time2, aws_index2



tile_id3 = 'S2B_OPER_MSI_L1C_TL_VGS2_20210121T122917_A020254_T30NXN_N02.09'
tile_name3, time3, aws_index3 = AwsTile.tile_id_to_tile(tile_id3)
tile_name3, time3, aws_index3


tile_id4 = 'S2B_OPER_MSI_L1C_TL_VGS2_20210121T122917_A020254_T30NXN_N02.09'
tile_name4, time4, aws_index4 = AwsTile.tile_id_to_tile(tile_id4)
tile_name4, time4, aws_index4

from sentinelhub import CRS, BBox, DataCollection, SHConfig, WebFeatureService

config = SHConfig()

if config.instance_id == "":
    print("Warning! To use WFS functionality, please configure the `instance_id`.")

#Import the type of bands needed and specify our folder Data to store the data
warnings.simplefilter("ignore", UserWarning)
from sentinelhub import AwsTileRequest

bands = ['B01','B02','B03','B04','B07','B08','B8A', 'B10','B11','B12']
metafiles = ['tileInfo', 'preview', 'qi/MSK_CLOUDS_B00']
data_folder = './Data'

#Trigger the download to create the folder Data
request = AwsTileRequest(
    tile=tile_name,
    time=time,
    aws_index=aws_index,
    bands=bands,
    metafiles=metafiles,
    data_folder=data_folder,
    data_collection=DataCollection.SENTINEL2_L1C
)

request.save_data()


request2 = AwsTileRequest(
    tile=tile_name2,
    time=time2,
    aws_index=aws_index2,
    bands=bands,
    metafiles=metafiles,
    data_folder=data_folder,
    data_collection=DataCollection.SENTINEL2_L1C
)

request2.save_data()


request3 = AwsTileRequest(
    tile=tile_name3,
    time=time3,
    aws_index=aws_index3,
    bands=bands,
    metafiles=metafiles,
    data_folder=data_folder,
    data_collection=DataCollection.SENTINEL2_L1C
)

request3.save_data()


request4 = AwsTileRequest(
    tile=tile_name4,
    time=time4,
    aws_index=aws_index4,
    bands=bands,
    metafiles=metafiles,
    data_folder=data_folder,
    data_collection=DataCollection.SENTINEL2_L1C
)

request4.save_data()

#Download data one
data_list = request.get_data(redownload=True)

p_b01,p_b02,p_b03,p_b04,p_b07,p_b08,p_b8a,p_b10,p_b11,p_b12,p_tile_info, p_preview, p_cloud_mask = data_list

#Download data two
data_list2 = request2.get_data(redownload=True)

p_b01_2,p_b02_2,p_b03_2,p_b04_2,p_b07_2,p_b08_2,p_b8a_2,p_b10_2,p_b11_2,p_b12_2,p_tile_info_2, p_preview_2, p_cloud_mask_2 = data_list2

#Download data three
#data_list3 = request3.get_data(redownload=True)

#p_b01_3,p_b02_3,p_b03_3,p_b04_3,p_b07_3,p_b08_3,p_b8a_3,p_b10_3,p_b11_3,p_b12_3,p_tile_info_3, p_preview_3, p_cloud_mask_3 = data_list3

#Download data four
#data_list4 = request4.get_data(redownload=True)

#p_b01_4,p_b02_4,p_b03_4,p_b04_4,p_b07_4,p_b08_4,p_b8a_4,p_b10_4,p_b11_4,p_b12_4,p_tile_info_4, p_preview_4, p_cloud_mask_4 = data_list4

#Plot image
plt.figure(figsize = (58,12))
f, axarr = plt.subplots(1,2,figsize = (42,12));
axarr[0].imshow(p_preview,aspect='auto');
axarr[1].imshow(p_preview_2,aspect='auto');
#axarr[2].imshow(p_preview_3,aspect='auto');
#axarr[3].imshow(p_preview_4,aspect='auto');

#Plot image
plt.figure(figsize = (58,12))
f, axarr = plt.subplots(1,2,figsize = (42,12));
axarr[0].imshow(p_preview,aspect='auto');
axarr[1].imshow(p_preview_2,aspect='auto');
#axarr[2].imshow(p_preview_3,aspect='auto');
#axarr[3].imshow(p_preview_4,aspect='auto');

import rasterio
from rasterio import plot

#changing the time variable to two digit of month and day due to folder creation accordigly 
timesplit = time.split("-")
newtime=''
for splitedval in timesplit:
    if len(newtime) > 0:
        newtime += "-"
    if len(splitedval) == 1:
        splitedval = '%02d' % int(splitedval)
        #print(splitedval)
        newtime += splitedval
    else:
        newtime += splitedval

timesplit = time2.split("-")
newtime2=''
for splitedval in timesplit:
    if len(newtime2) > 0:
        newtime2 += "-"
    if len(splitedval) == 1:
        splitedval = '%02d' % int(splitedval)
        #print(splitedval)
        newtime2 += splitedval
    else:
        newtime2 += splitedval

localpath = './Data/'+tile_name+','+newtime+','+str(aws_index)
localpath2 = './Data/'+tile_name2+','+newtime2+','+str(aws_index2)

#image 1

b4 = rasterio.open(localpath+'/B04.jp2')
b8 = rasterio.open(localpath+'/B08.jp2')

# read Red(b4) and NIR(b8) as arrays
red = b4.read()
nir = b8.read()
ndvi = (nir.astype(float)-red.astype(float))/(nir.astype(float)+red.astype(float))

#image 2

b4_2 = rasterio.open(localpath2+'/B04.jp2')
b8_2 = rasterio.open(localpath2+'/B08.jp2')

# read Red(b4) and NIR(b8) as arrays
red_2 = b4_2.read()
nir_2 = b8_2.read()
ndvi_2 = (nir_2.astype(float)-red_2.astype(float))/(nir_2.astype(float)+red_2.astype(float))

!pip install earthpy

import earthpy.spatial as es
import earthpy.plot as ep

# Create figure with one plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(48, 24))
title = "Normalized Difference Vegetation Index (NDVI) Image 1 Time 1"
title2 = "Normalized Difference Vegetation Index (NDVI) Image 2 - Time 2"
ep.plot_bands(ndvi, cmap="PiYG", cols=2, title=title, vmin=-1, vmax=1,ax=ax1);
ep.plot_bands(ndvi_2, cmap="PiYG", cols=2, title=title2, vmin=-1, vmax=1,ax=ax2);
plt.show()

# Create classes and apply to NDVI results
ndvi_class_bins = [-np.inf, 0, 0.1, 0.25, 0.4, np.inf]
ndvi_density_class = np.digitize(ndvi, ndvi_class_bins)

# Apply the nodata mask to the newly classified NDVI data
ndvi_density_class = np.ma.masked_where(
    np.ma.getmask(ndvi), ndvi_density_class
)
np.unique(ndvi_density_class)

# Create classes and apply to NDVI results
ndvi_density_class_2 = np.digitize(ndvi_2, ndvi_class_bins)

# Apply the nodata mask to the newly classified NDVI data
ndvi_density_class_2 = np.ma.masked_where(
    np.ma.getmask(ndvi_2), ndvi_density_class_2
)
np.unique(ndvi_density_class_2)

from matplotlib.colors import ListedColormap
# Define color map
nbr_colors = ["khaki", "y", "yellowgreen", "g", "darkgreen"]
nbr_cmap = ListedColormap(nbr_colors)

# Define class names
ndvi_cat_names = [
    "Dead forest",
    "Scrub",
    "Open Forest",
    "Moderately Dense Forest",
    "Very Dense Forest",
]

# Get list of classes
classes = np.unique(ndvi_density_class)
classes = classes.tolist()
# The mask returns a value of none in the classes. remove that
classes = classes[0:5]

# Plot your data
#fig, ax = plt.subplots(figsize=(12, 12))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12))
im1 = ax1.imshow(np.squeeze(ndvi_density_class), cmap=nbr_cmap)
ep.draw_legend(im_ax=im1, classes=classes, titles=ndvi_cat_names)
ax1.set_title(
    "Sentinel2L1C - Normalized Difference Vegetation Index (NDVI) Classes",
    fontsize=14,
)

im2 = ax2.imshow(np.squeeze(ndvi_density_class_2), cmap=nbr_cmap)
ep.draw_legend(im_ax=im2, classes=classes, titles=ndvi_cat_names)
ax2.set_title(
    "Sentinel2L1C - Normalized Difference Vegetation Index (NDVI) Classes",
    fontsize=14,
)
ax1.set_axis_off()
ax2.set_axis_off()
plt.tight_layout()


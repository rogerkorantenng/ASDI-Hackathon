# ASDI-Hackathon

#Steps Used
## How we built it(Steps)
1: We use Bbox to get co-ordinates of the Mole National Park and Ankasa Game Reserves from **http://bboxfinder.com**, once we get the **xMin, yMin and xMax, yMax** we can then pass it in the **search_bbox** function 

2. We use the **search_time_interval** python function to determine the time length
 
3. To get the **tile_info** for the specified period of time we use **wfs_iterator** to extract unique tile info for each tile
 
4. Next, we will convert each **tile_id** obtained to a **tile_name** to be accessed from the s3 bucket
 
5. For clear results we choose the **tile_id** with the least cloud cover
 
6. Next we select bands **'B01','B02','B03','B04','B07','B08','B8A', 'B10','B11','B12'** 
 
7. We will determine the download folders for both Mole National Park(**mole_data**) and Ankasa Game Reserves(**ankasa_data**)
 
8. We will request for the data using the **request.save_data** function
 
9. Next, we will trigger the download and specify the bands we want to download
 
10. After downloading images to our folder we can then use **matplotlib** to plot out image
 
11. To check for deforestation we will import **rasterio** and use the GeoTIFF feature to check the vegetation of the selected area
 
12. Because we were checking for the vegetation view, we used band 4 and band 8 
 
13. Finally we plot the image 

### ASDI-Hackathon: Deforestation Analysis

The `deforestation_asdi.ipynb` file contains all the code used in this Hackathon to analyze deforestation using satellite imagery. Here is a detailed breakdown of the steps followed:

#### Steps Followed

**1. Download and Import Libraries**
   - First, we need to ensure all required Python libraries are downloaded and imported. These libraries include tools for geospatial data analysis and image processing such as `matplotlib`, `rasterio`, and other relevant libraries.

**2. Obtain Coordinates**
   - Using [BBox Finder](http://bboxfinder.com), we get the geographical coordinates (xMin, yMin, xMax, yMax) for the areas of interest: Mole National Park and Ankasa Game Reserves.
   - These coordinates define a bounding box around the regions we want to analyze. We pass these coordinates to the `search_bbox` function, which helps us locate the specific tiles in the satellite imagery.

**3. Determine Time Interval**
   - The `search_time_interval` function is used to specify the time period we are interested in. This period could span multiple years to observe changes over time or could be focused on a specific timeframe to analyze recent changes.

**4. Extract Tile Information**
   - The `wfs_iterator` function is then used to extract unique tile information for each tile within the specified bounding box and time interval. Each tile represents a segment of the satellite imagery covering our areas of interest.
   - This function iterates through the available tiles and collects metadata, such as tile IDs and the date of acquisition.

**5. Convert Tile IDs to Tile Names**
   - With the tile IDs obtained from the previous step, we convert these IDs to tile names that correspond to files stored in an S3 bucket. This allows us to access and download the specific images we need.

**6. Select Tiles with Least Cloud Cover**
   - To ensure clear and usable images, we select tiles with the least amount of cloud cover. Cloud cover can obscure the ground and hinder the analysis of deforestation.

**7. Select Spectral Bands**
   - For the analysis, we choose specific spectral bands that are useful for vegetation and land cover analysis. The selected bands are 'B01', 'B02', 'B03', 'B04', 'B07', 'B08', 'B8A', 'B10', 'B11', and 'B12'. These bands capture different wavelengths of light, providing various perspectives of the land.

**8. Determine Download Folders**
   - We create separate folders to store the downloaded data for Mole National Park (`Mole_Data`) and Ankasa Game Reserves (`Ankasa_Data`).

**9. Request and Save Data**
   - Using the `request.save_data` function, we send requests to download the selected tiles. We specify the bands we want to download and the folders where the data will be saved.

**10. Download Images**
   - The data download is triggered, and the specified bands are saved to our local folders. This step involves fetching the satellite images from the S3 bucket and storing them for further analysis.

**11. Plot Images Using Matplotlib**
   - After downloading the images, we use the `matplotlib` library to plot the images. This helps visualize the satellite imagery and inspect the quality and coverage of the data.

**12. Check for Deforestation Using Rasterio**
   - To analyze deforestation, we import the `rasterio` library and utilize the GeoTIFF feature to examine the vegetation in the selected areas. The GeoTIFF format allows us to handle georeferenced raster data efficiently.
   - For vegetation analysis, we focus on specific bands that are sensitive to vegetation cover, such as band 4 (red) and band 8 (near-infrared).

**13. Plot the Final Image**
   - Finally, we plot the processed image to visualize the vegetation status and detect any signs of deforestation in Mole National Park and Ankasa Game Reserves.

By following these steps, we can effectively analyze deforestation trends and changes in vegetation cover over time, providing valuable insights for conservation efforts.

## Images and Code Snippets

<img src="/images/Capture.PNG" width="700" length="900"/>
<img src="/images/Capture1.PNG" width="700" length="900"/>
<img src="/images/Capture2.PNG" width="700" length="900"/>
<img src="/images/Capture3.PNG" width="700" length="900"/>
<img src="/images/Capture4.PNG" width="700" length="900"/>
<img src="/images/Capture5.PNG" width="700" length="900"/>
<img src="/images/Capture6.PNG" width="700" length="900"/>


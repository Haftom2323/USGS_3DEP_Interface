# USGS_3DEP INTERFACE
Python module that enables domain experts and data scientists  to fetch, 
visualise, and transform publicly available satellite and LIDAR data from USGS 3DEP so 
that they can easily perform modeling and further processing on the LIDAR data 

### This package will be used to
- fetch data from the USGS 3DEP using their API(built using pdal pipeline)
- visualize the data
- transform the data
     - topographic wetness index (TWI) - as an additional column returned with geopandas dataframe
     - Standardized grid - A python code that takes elevation points output from the USGS LIDAR tool and   interpolates them to a grid.
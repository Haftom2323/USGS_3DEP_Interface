import pdal
import json

PUBLIC_DATA_PATH="https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
PIPELINE_PATH='./get_data.json'

def get_raster_terrain(bounds:str,region:str,PIPELINE_PATH:str=PIPELINE_PATH)->None:
    PUBLIC_ACCESS_PATH=PUBLIC_DATA_PATH + region + "/ept.json"
    OUTPUT_FILENAME_LAZ='../data/laz/'+region+'.laz'
    OUTPUT_FILENAME_TIF='../data/tif/'+region+'.tif'


    with open(PIPELINE_PATH) as json_file:
        the_json= json.load(json_file)
    
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=PUBLIC_ACCESS_PATH
    the_json['pipeline'][3]['filename']=OUTPUT_FILENAME_LAZ
    the_json['pipeline'][4]['filename']=OUTPUT_FILENAME_TIF
   
    pipeline=pdal.Pipeline(json.dumps(the_json))
    
    try:
        pipe_exec=pipeline.execute()
    except RuntimeError as er:
        print(er)
        print('Runtime error, writing 0s and moving to next bounds')
        pass





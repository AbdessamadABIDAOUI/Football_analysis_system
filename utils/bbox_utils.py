def get_center_of_bbox(bbox):
    x1,y1,x2,y2 = bbox
    return int((int(x1) + int(x2)) / 2), int((int(y1) + int(y2))/ 2)

def get_bbox_width(bbox):
    return int(bbox[2]-bbox[0])
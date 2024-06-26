from ultralytics import YOLO
import supervision as sv
class tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()


    def detect_frames(self, frames):
        batchsize = 20
        detections = []
        for i in range(0, len(frames), batchsize):
            detections_batch = self.model.predict(frames[i:i+batchsize],conf=0.1)
            detections += detections_batch
            break
        return detections
    
    def get_object_tracks(self, frames):
        
        detections = self.detect_frames(frames)

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v:k for k,v in cls_names.items()}
            print(cls_names)
            #convert to supervision Detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)
            print(detection_supervision)
            break


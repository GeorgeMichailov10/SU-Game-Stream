## Yolo Setup Instructions

1. Install yolov7 from repo: https://github.com/WongKinYiu/yolov7
2. Install requirements: pip install -r requirements.txt
3. Download weights: curl -L https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt -o yolov7.pt
   and move to yolov7 folder (not necessary to put them there, just way more convenient).
4. Python will look for the model in its own bin, so you need to add the path to the model to the python path using sys.path.append('path/to/model')

## Yolo Use Advice

1. Run the model with no grad for better performance
2. Use a stream size that is divisible by a higher power of 2 for better performance (It's a GPU calculation thing)
3. Use torch.\_dynamo eager mode with torch.compile for better performance.
4. Don't even bother trying to run this on CPU, it's not worth it. Our specs are 16 GB of RAM, and RTX 4060 with 8 GB of VRAM. We needed the optimization above to be able to run the model on a webcam at a satisfactory frame rate.

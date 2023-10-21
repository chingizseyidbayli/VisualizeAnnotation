
# Visualize Image Annotation 

This study is concerned with obtaining images annotated with XML files containing bounding box coordinate data of images and objects on them.


## Installation


```bash
pip install argparse
pip install tqdm
pip install opencv-python
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/chingizseyidbayli/VisualizeAnnotation.git

```

Go to the project directory

```bash
  cd VisualizeAnnotation
```


Run the script

```bash
  python annotate_images.py --annotation_files_path ANNOTATION_FILES_PATH --image_files_path IMAGE_FILES_PATH --output_path OUTPUT_PATH
```

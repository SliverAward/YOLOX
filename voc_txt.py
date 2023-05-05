from glob import glob
import os
import random
import shutil

# 경로 설정
original_path = os.path.abspath('C:\\YOLOX\\datasets\\mpv\\train\\')
VOC_devkit = os.path.abspath('C:\\YOLOX\\datasets\\VOCdevkit')
img_files = glob(os.path.join(original_path, '*.jpg'))
ann_files = glob(os.path.join(original_path, '*.xml'))



# 복사해서 붙여넣을 디렉토리 경로 설정
img_save_path = os.path.join(VOC_devkit, 'VOC2007', 'JPEGImages')
ann_save_path = os.path.join(VOC_devkit, 'VOC2007', 'Annotations')

# 디렉토리 생성
os.makedirs(img_save_path, exist_ok=True)
os.makedirs(ann_save_path, exist_ok=True)

# 이미지와 어노테이션 파일을 해당 디렉토리로 복사
for img_file in img_files:
    shutil.copy(img_file, img_save_path)

for ann_file in ann_files:
    shutil.copy(ann_file, ann_save_path)

# 이미지 파일 경로를 저장할 txt 파일 경로 설정
txt_save_path = os.path.join(VOC_devkit, 'VOC2007', 'ImageSets', 'Main')
os.makedirs(txt_save_path, exist_ok=True)

# train, val, trainval, test 데이터셋 생성을 위한 인덱스 리스트 생성
total_xml = os.listdir(ann_save_path)
num = len(total_xml)
lst = range(num)
tv = int(num * 0.9)
tr = int(tv * 0.8)
trainval = random.sample(lst, tv)
train = random.sample(trainval, tr)

print("train and val size:", tv)
print("train size:", tr)

# txt 파일에 이미지 파일 경로 및 xml 파일 경로 저장
with open(os.path.join(txt_save_path, 'trainval.txt'), 'w') as ftrainval, \
     open(os.path.join(txt_save_path, 'train.txt'), 'w') as ftrain, \
     open(os.path.join(txt_save_path, 'val.txt'), 'w') as fval, \
     open(os.path.join(txt_save_path, 'test.txt'), 'w') as ftest:

    for i in lst:
        name = os.path.splitext(total_xml[i])[0]
        fxml = os.path.join(ann_save_path, name + '.xml')
        if i in trainval:
            ftrainval.write(name + '\n')
            ftrainval.write(fxml + '\n')
            if i in train:
                ftrain.write(name + '\n')
            else:
                fval.write(name + '\n')
        else:
            ftest.write(name + '\n')
            ftest.write(fxml + '\n')
# VOC2007 디렉토리 내용물을 VOC2012 폴더에 복사
voc2007_path = os.path.join(VOC_devkit, 'VOC2007')
voc2012_path = os.path.join(VOC_devkit, 'VOC2012')
if os.path.exists(voc2012_path):
  shutil.rmtree(voc2012_path) # 이미 존재하면 폴더 삭제 후 복사
shutil.copytree(voc2007_path, voc2012_path)

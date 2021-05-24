# 데이터 관련 최종

# 모듈
from urllib.request import Request, urlopen
import json
import os
import face_recognition
from PIL import Image
import numpy as np

# 다운로드 기능 (without_mask, with_mask, mask)
def download_image(kind):
    if kind == 'without_mask':
        api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'
        hds = {'User-Agent': 'Mozilla/5.0'}
        request = Request(api_url, headers=hds)
        response = urlopen(request)
        directory_bytes = response.read()
        directory_str = directory_bytes.decode('utf-8')
        contents = json.loads(directory_str)
        for i in range (len(contents)):
            content = contents[i]
            request = Request(content['download_url'])
            response = urlopen(request)
            image_data = response.read()
            if not os.path.exists('data'):
                os.mkdir('data')
            if not os.path.exists('data/without_mask'):
                os.mkdir('data/without_mask')
            image_file = open('data/without_mask'+content['name'], 'w')
            image_file.write(image_data)
            image_file.close()
            print(kind,'이미지 다운로드 중... ('+str(i+1)+'/'+str(len(contents))+'): '+content['name'])

    elif kind == 'with_mask':
        if kind == 'with_mask':
            api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/with_mask?ref=master'
            hds = {'User-Agent': 'Mozilla/5.0'}
            request = Request(api_url, headers=hds)
            response = urlopen(request)
            directory_bytes = response.read()
            directory_str = directory_bytes.decode('utf-8')
            contents = json.loads(directory_str)
            for i in range(len(contents)):
                content = contents[i]
                request = Request(content['download_url'])
                response = urlopen(request)
                image_data = response.read()
                if not os.path.exists('data'):
                    os.mkdir('data')
                if not os.path.exists('data/with_mask'):
                    os.mkdir('data/with_mask')
                image_file = open('data/with_mask' + content['name'], 'w')
                image_file.write(image_data)
                image_file.close()
                print(kind, '이미지 다운로드 중... (' + str(i + 1) + '/' + str(len(contents)) + '): ' + content['name'])

    elif kind == 'mask':
        mask_image_download_url = 'https://github.com/prajnasb/observations/raw/master/mask_classifier/Data_Generator/images/blue-mask.png'
        request = Request(mask_image_download_url)
        response = urlopen(request)
        image_data = response.read()
        if not os.path.exists('data'):
            os.mkdir('data')
        image_file = open('data/mask.png', 'w')
        image_file.write(image_data)
        image_file.close()
        print(kind,'이미지 다운로드 완료')

# 점 간의 거리 계산
def calcDistance(a, b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# 마스크 합성
def mask_process(face_image_file_name):
    # 이미지 경로 생성
    face_image_path = 'data/without_mask/'+face_image_file_name
    mask_image_path = 'data/mask.png'

    # 얼굴 영역 추출, 얼굴 랜드마크 추출
    face_image_np = face_recognition.load_image_file(face_image_path)
    face_locations = face_recognition.face_locations(face_image_np)
    face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

    # 결과 이미지 생성
    face_image = Image.fromarray(face_image_np)
    mask_image = Image.open(mask_image_path)
    face_count = 0

    # 마스크 합성
    for face_landmark in face_landmarks:
        if ('nose_bridge' not in face_landmark) or ('chin' not in face_landmark):
            continue
        # 마스크 너비 보정값(1.2)
        mask_width_ratio = 1.2

        # 마스크 높이 계산 (nose_bridge 2번째 점 & chin 9번째 점 간의 길이)
        mask_height = round(calcDistance(face_landmark['nose_bridge'][1], face_landmark['chin'][8]))

        # 마스크 좌/우 분할
        mask_left = mask_image.crop((0, 0, round(mask_image.width/2), mask_image.height))
        mask_right = mask_image.crop((round(mask_image.width/2), 0, mask_image.width, mask_image.height))

        # 왼쪽 얼굴 너비 계산

        
        # 왼쪽 마스크 크기 조절

        # 오른쪽 얼굴 너비 계산

        # 오른쪽 마스크 크기 조절

        # 좌/우 마스크 연결결

        # 얼굴 회전 각도 계산

        # 마스크 회전

        #


    # 결과 이미지 반환
    return face_image, face_count

# 이터 생성


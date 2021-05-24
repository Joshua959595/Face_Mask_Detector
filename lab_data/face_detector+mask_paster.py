# 얼굴 인식 스크립트

import face_recognition
from PIL import Image, ImageDraw
import numpy as np

mask_image_path = '../data/mask.png'
i = 0
target = 10

while i != target:
    try:
        # <<face_detector>>
        face_image_path = 'data/without_mask/' + str(i) + '.jpg'
        face_image_np = face_recognition.load_image_file(face_image_path)
        face_locations = face_recognition.face_locations(face_image_np)
        face_image = Image.fromarray(face_image_np)
        # face_image는 얼굴 좌표를 나타내는 배열값이 필요해서 fromarray로 중간 작업을 거침
        #draw = ImageDraw.Draw(face_image)
        # face_image.show()
        face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

        # 얼굴이 두개 이상일 수도
        for p in  range (len(face_landmarks)):

            # x값
            maskLeft = face_landmarks[p]['chin'][1][0]
            maskRight = face_landmarks[p]['chin'][15][0]
            mask_xsize = abs(maskRight-maskLeft)
            maskCenterX = (maskLeft+maskRight)//2
            maskPositionX = maskCenterX-mask_xsize//2

            # y값
            maskUp = face_landmarks[p]['nose_bridge'][0][1]
            maskDown = face_landmarks[p]['chin'][9][1]
            mask_ysize = abs(maskUp-maskDown)
            maskCenterY = (maskUp+maskDown)//2
            maskPositionY = maskCenterY-mask_ysize//2

            # 얼굴의 기울기 (y증가량/x증가량)
            top_standard = face_landmarks[p]['nose_bridge'][0]
            bottom_standard = face_landmarks[p]['chin'][8]

            dx = bottom_standard[0] - top_standard[0]
            dy = bottom_standard[1] - top_standard[1]
            angleRadian = np.arctan2(dy,dx)
            angleDegree = np.rad2deg(angleRadian)

            Angle = 90-angleDegree

            '''
            # <<mask_paster>>
            for face_location in face_locations:
                top = face_location[0]
                right = face_location[1]
                bottom = face_location[2]
                left = face_location[3]
                #draw.rectangle(((left, top), (right, bottom)), outrline=(255, 255, 0), width=4)  # outline=(R,G,B)
            '''
            # mask_image는 바로 붙이니까 open으로 바로
            mask_image = Image.open(mask_image_path)
            mask_image = mask_image.resize((round(mask_xsize*1.2), mask_ysize))
            mask_image = mask_image.rotate(round(Angle), expand=True)

            face_image.paste(mask_image, (maskPositionX,maskPositionY), mask_image) # paste 인자 마지막에 이미지를 한번 더 넣어줌으로써, 이미지 배경 투명화
            face_image.show()
        i += 1

    except:
        i += 1
        target += 1
        continue


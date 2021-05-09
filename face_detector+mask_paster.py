# 얼굴 인식 스크립트

import face_recognition
from PIL import Image, ImageDraw

mask_image_path = 'data/mask.png'
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
        draw = ImageDraw.Draw(face_image)
        # face_image.show()
        face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)
        y = face_landmarks[0]['nose_bridge'][1][1]

        # <<mask_paster>>
        for face_location in face_locations:
            top = face_location[0]
            right = face_location[1]
            bottom = face_location[2]
            left = face_location[3]
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)  # outline=(R,G,B)
            if i==0 :
                fir_height = abs(round(top - bottom))
                fir_length = abs(round(right - left))
            height = y #abs(round(top - bottom))
            length = abs(round(right - left))

        # mask_image는 바로 붙이니까 open으로 바로
        mask_image = Image.open(mask_image_path)
        if i == 0:
            mask_image = mask_image.resize((65,40))
        else:
            mask_image = mask_image.resize((round(65*length/fir_length), round(40*height/fir_height)))
        face_image.paste(mask_image, (left,height), mask_image) # paste 인자 마지막에 이미지를 한번 더 넣어줌으로써, 이미지 배경 투명화
        face_image.show()
        i += 1

    except:
        i += 1
        target += 1
        continue
# 메시만 유독 안맞는데
# resize x,y값을 변수로 (face_landmarks)점간의 차이로?

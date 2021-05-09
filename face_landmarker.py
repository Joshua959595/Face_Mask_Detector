# 얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

face_image_path = 'data/without_mask/0.jpg'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

print(face_landmarks[0]['nose_bridge'][round(len(face_landmarks[0]['nose_bridge'])/2)][1])
#print(round(len(face_landmarks[0]['nose_bridge'])/2))
'''
face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_landmark in face_landmarks:
    for feature_name, points in face_landmark.items():
        for point in points:
            draw.point(point)

# draw.point((10, 10))

face_landmark_image.show()
'''
# 'nose_bridge': [(80, 61), (80, 66), (80, 72), (80, 77)]
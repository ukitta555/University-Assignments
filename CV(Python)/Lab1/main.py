import cv2

if __name__=="__main__":
    modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
    configFile = "deploy.prototxt"
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    j = 0
    for sampleImage, frameOpencvDnn in zip(
            [cv2.imread("sample0.jpg"), cv2.imread("sample1.jpg")],
            [cv2.imread("sample0.jpg"), cv2.imread("sample1.jpg")]
    ):
        grayscaleSample = cv2.cvtColor(sampleImage, cv2.COLOR_BGR2GRAY)
        dimensions = frameOpencvDnn.shape
        height = dimensions[0]
        width = dimensions[1]

        blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123],
                                     False, False)
        net.setInput(blob)
        # print(blob)
        detections = net.forward()
        bboxes = []
        conf_threshold = 0.95
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * width)

                y1 = int(detections[0, 0, i, 4] * height)
                x2 = int(detections[0, 0, i, 5] * width)
                y2 = int(detections[0, 0, i, 6] * height)
                w = x2 - x1
                h = y2 - y1
                roi_grayscale = grayscaleSample[y1:y2, x1:x2]
                roi_colored = sampleImage[y1:y2, x1:x2]
                scale = 1.01 + 0.1 * int((x2 - x1) / 200)
                eyes = eye_cascade.detectMultiScale(roi_grayscale, scale, 10,
                                                    minSize=(int(w / 6), int(h / 8)),
                                                    maxSize=(int(w / 2), int(h / 2.2)))
                for (eyes_x, eyes_y, eyes_w, eyes_h) in eyes:
                    cv2.rectangle(frameOpencvDnn, (x1 + eyes_x, y1 + eyes_y), (x1 + eyes_x +
                                                                               eyes_w, y1 + eyes_y + eyes_h), (0, 255, 0), 2)

                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.imwrite(f"jp{j}.jpg", frameOpencvDnn)
        j+=1
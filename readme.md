basically im just

1. -  setting path (you should set ur own path)

2. -  img -> grey
3. -  grey -> blur (for noise)
4. -  blur -> edge

5. -  (2 - 4) black magic aka just change thresholds low & high and sometimes "GB = cv2.GaussianBlur(gray, (x, x), 0)" if the noise is still coming thru
6. -  enyoy

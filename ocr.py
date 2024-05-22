from ocrmac import ocrmac
annotations = ocrmac.OCR('pri.png').recognize()
st=""
for i in annotations:
    st+=i[0] + "\n"
    print(i[0])
print(st)


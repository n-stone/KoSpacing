from pykospacing import Spacing

while 1:
    sent = input("입력하고 싶은 문장을 적어주세요(종료: 0 입력): ")
    if sent == "0":
        break
    new_sent = sent.replace(" ", '')
    spacing = Spacing()
    kospacing_sent = spacing(new_sent) 

    print("띄어쓰기 제거 후 데이터:",new_sent)
    print("변형된 데이터:",kospacing_sent)
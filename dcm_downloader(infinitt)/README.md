### INFINITT 프로그램에서 많은 환자들의 CT사진을 자동으로 받게끔 하는 매크로입니다.

순서대로  


1.다운로드할 환자를 INFINITT에서 export합니다.(id와 date가 포함되어야함)  


2.export한 csv에서 id만 BRCL_PNG_ID_LIST에 복사붙여넣기합니다.  


3.date도 마찬가지로 합니다.  


4.INFINITT 들어가시고 로그인합니다.  


5.BRCL_dicom.py에 들어갑니다.  


6.이후 주석 설명대로 경로설정,좌표설정,이미지캡처를 실행합니다.  
참고)현재 마우스의 좌표를 아는방법은 아래와 같습니다.  
  cmd  
  python  
  import pyautogui  
  pyautogui.position()  
  
  
7.준비가 완료되었으면 INFINITT프로그램을 활성화하고 CMD에 아래와 같이 입력합니다.  
  python BRCL_dicom.py  
  

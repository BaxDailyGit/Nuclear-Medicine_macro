## main study  
### [dcm파일 다운로더](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/dcm_downloader(infinitt))  
> 1. 다운로드할 환자를 INFINITT에서 export합니다.(id와 date가 포함되어야함)  
> 2. export한 csv에서 id만 BRCL_PNG_ID_LIST에 복사붙여넣기합니다.  
> 3. date도 마찬가지로 합니다.  
> 4. INFINITT 들어가시고 로그인합니다.  
> 5. BRCL_dicom.py에 들어갑니다.  
> 6. 이후 주석 설명대로 경로설정,좌표설정,이미지캡처를 실행합니다.  
>   참고)현재 마우스의 좌표를 아는방법은 아래와 같습니다.  
> ```cmd
> python
> import pyautogui
> pyautogui.position()
> ```
> 7. 준비가 완료되었으면 INFINITT프로그램을 활성화하고 cmd관리자 모드에서 아래와 같이 입력합니다.
> ```cmd
> python BRCL_dicom.py
> ```

### [exported환자정보arrange](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/arrange_exported_patient_info)  

> 엑셀의 VBA코드입니다.  
> 1. 엑셀파일에 들어가셔서 Alt+f11을 누르시면 vba코드가 나옵니다.
> 2. 주석 설명에 맞게 설정후 실행하시면 됩니다.
> 
> - 정리본 양식 :
>   - sheet1: INFINITT에서 CSV파일로 export한 환자를 전처리합니다. (전처리: 환자 id 맨앞에 0 없어짐 해결, 기계별 이름 변경)  
>   - 모듈1: 측정 FTTR TXT파일 데이터를 자동 입력합니다.
> 
> - 기계별 정리본 :
>   위 정리본 양식들을 취합후 전체 통계를 냅니다.
> 
> - 총정리본 for_study_data :
>   스터디 환자만 따로 모아놓은 파일입니다.  
>   INCREMENT열에 빨간 셀이 나오면 수치가 잘못된것입니다. 다시 측정해야 합니다.




### [Image Quality Evaluation 영상품질비교지표](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/Image_Quality_Evaluation)  

> 영상품질비교지표를 측정하는 매크로입니다.
> ssimm, psnr, mse, rmse를 측정합니다.
> icy프로그램 위에서 파이썬이 실행되는 형태입니다.  
> 
> 1. ipynd파일에 들어가서 비교할 영상들이 있는 위치를 path폴더 안의 txt파일로 저장하는 작업을 합니다.
> 
> 2. comparator.py에 들어가서 경로,좌표를 재설정합니다.
> 
> 3. icy프로그램에 들어갑니다.
> 
> 4. comparator 탭에 들어가서 최대창으로 한다음 아래로 내려놓고 파일열기가 보이는 탭을 활성화합니다.
> 
> 5. 준비를 마쳤으면 cmd 관리자모드로 들어가 아래와같은 코드를 입력합니다.
> ```cmd
> python comparator.py
> ```

### [thigh-femur 측정(반자동화)](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/thigh-femur%20measurement)  


## sub study  
>
> 
### [판독문 추출](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/extract%20readings)  
>
> 
### [L3-upper thigh 근육량 측정(반자동화)](https://github.com/ajoumax/Nuclear-Medicine_macro/tree/main/L3-upper%20thigh%20muscle%20measurement)  
> ASANj 프로그램 위해서 실행된다.
> 
> ASANj는 https://datasharing.aim-aicro.com/morphometry 에서 다운받을수있다.
> 
> 이후 자세한 설명은 추후에 작성한다.


<hr/>  
---

###### 자신의 컴퓨터 환경에 맞게 세팅해주셔야 합니다.  

###### 세부설명을 추가해 놓겠습니다.  


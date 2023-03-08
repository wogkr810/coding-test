-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, LEFT(START_DATE,10) AS START_DATE, LEFT(END_DATE,10) AS END_DATE, 
IF (DATEDIFF(END_DATE,START_DATE)>=29,'장기 대여','단기 대여')AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC
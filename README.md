# WEB_HW11
WEB_HW 11

1. docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=8811550 -d postgres

2. poetry update package

3. uvicorn main:app --host localhost --port 8000 --reload

4. після першого запуску треба виконати

           HTTP метод: DELETE
           URL: /api/reset_base (Reset Database)
   так, це тимчасова милиця, яку буде прибрано

![image](https://github.com/KyryloChalov/WEB_HW11/assets/140982410/40d989a2-cfc5-4ecc-8369-5a6d94fa87dc)


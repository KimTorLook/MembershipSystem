這是跟着一本書來做的一個會員系統  
你能在這個網頁版會員系統進行登入登出，登入後在首面能連結到僱員列表  
僱員列表會詳細列出每位員工的個人資料  
在僱員列表網頁中，你可以新增員工/編輯員工/刪除員工/登出  

功能︰  
1.登入員工帳戶時系統會驗證登入帳戶，未能驗證則會登入失敗  
2.資料大多會用POST方式傳送資料  
3.表格資料均使用CSRF TOKEN作資訊防護  
4.編輯一/二頁面會自動將該員工資料顯示在適當的地方/欄位  
5.員工資料會儲存到Django內置使用的資料庫SQlite  
6.不同的員工資料有不同的資料格式限制，盡量減少輸入格式錯誤  

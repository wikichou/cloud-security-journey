![[Pasted image 20260511212419.png]]


HTTP是web server跟browser之間溝通用的協議，也就是網頁資料傳輸使用的protocol，建立在L7之上
HTTPs則是HTTP的安全強化版，利用TLS做傳輸加密，server 驗證等等功能

URL:網路上資源的存放地，結構就像上圖

Http method是使用RESTful API風格寫出來的標準化溝通方式，分成以下幾種
1.GET:純拿資料
2.POST:新增一筆到server
3.PUT:更新server
4.DELETE:刪除server一筆

Http status code是用來讓server表達request的處理狀況的數值，範圍大致上是
100~199:info
200~299:sucess
300~399:redirection
400~499:client error
500~599:server error
常用的有
200:success
400:bad request，表示路徑不存在
401:not authorized，表示尚未登入
403:forbidden，表示使用的http method有誤
404:not found，表示資源不存在
500:internal error，表示server內部錯誤
503:service unavailble

Header:r的時候加入的額外資訊
cookies:儲存可以放在瀏覽器的小資料，例如說登入資訊
當server回傳的header帶著set-cookis的時候把這個標籤的內容存起來
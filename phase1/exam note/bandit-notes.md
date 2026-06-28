### L0
cat直接看readme
### L1
因為密碼的檔名叫做-是特殊符號，可以用./- 也就是路徑的方式去看到密碼
### L2
檔名叫做--spaces in this filename--
嘗試過用雙引號包起來，./配合cat，目前想法是要想辦法跳脫空格符號， cat -- '--spaces in this filename--'最後這樣打開了
### L3
密碼被藏在inhere資料夾裡面，cd進去之後用ls -al 就可以看到了
### L4
同樣是inhere資料夾，但是裡面有很多檔案，其中只有一個是可讀的，並且檔案名稱開頭都是-號
我是用file一個一個檢查，並且因為開頭是符號，所以用L2的方式看，但我想應該有一次看完整個資料夾內部的方法
### L5
- human-readable
- 1033 bytes in size
- not executable
這是這題的說明，有點複雜，並且inhere裡面有很多資料夾，每個資料夾裡面還有很多檔案，總之我要找到ASCII格式的檔案，並且大小要對，我決定先用大小判斷，ls -al列出每一個資料夾內容看大小跟類型
-rw-r-----  1 root bandit5 1033 Jun 24 14:59 .file2
找到這個，並且他是ASCII，權限也是不可執行，所以就是他
### L6
The password for the next level is stored **somewhere on the server** and has all of the following properties:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size
要求是這樣，並且說是在server上?我其實不確定這題怎麼做，但我直接去root(/)找了bandit_pass裡面找，看了bandit6內容，顯然不對
顯然重點是在擁有者這點 find可以加上group跟username來找， find -group bandit6 -user bandit7 | grep 2>dev/null我試著這樣找但內容好多，後來發現是我下錯指令了，find -group bandit6 -user bandit7 2>/dev/null這樣才對

### L7
The password for the next level is stored in the file **data.txt** next to the word **millionth**
這題的重點就是從檔案裡面找出特定的內容，直接cat搭配grep -a就好

### L8
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once
這題要看內容不重複的那行，我在grep的help裡面有看到這個 -R --exclude-from=FILE   skip files that match any file pattern from FILE看可不可以用，但沒有結果
接著看了 sort的help有看到-u，但輸出也有很多，接著看uniq有甚麼可以用的
cat data.txt | uniq -c，用這樣看會有很多組，查之後是因為uniq只看相鄰的行數，所以要先用sort把一樣的排在一起，cat data.txt | sort | uniq -u，後面再用-u找出來

### L9
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.
要找出只有人類能讀的內容，並且前面會有=符號，我想可以用grep或是find起手
-q, --quiet, --silent     suppress all normal output
 --binary-files=TYPE   assume that binary files are TYPE;
這個應該是可以用的
  直接用cat看了之後發現內容是亂碼，試試看用base64讀，顯然也不對，要用strings讀才對
  strings data.txt | grep -a "="像這樣，然後找出類似的答案就好
### L10
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data
送分題，應該直接用base64解碼出來就好 base64 -d data.txt
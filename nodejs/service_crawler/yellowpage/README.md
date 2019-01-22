this file helps crawl the information of all categories in Ontario from yellowpage
requires: cheerio and json2xls
generate json using:(it requires a folder called 'data' in the same working directory) 
	node index.js 1
if want the spreadsheet, after already run node music.js 1, run the program again using:
	node index.js
(it requires a folder called 'spreadsheet' in the same working directory) 
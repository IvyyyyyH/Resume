this file helps crawl the information from rcmusic to get info about music teachers
requires: cheerio and json2xls
generate json using:(it requires a folder called 'data' in the same working directory) 
	node music.js 1
if want the spreadsheet, after already run node music.js 1, run the program again using:
	node music.js
(it requires a folder called 'spreadsheet' in the same working directory) 
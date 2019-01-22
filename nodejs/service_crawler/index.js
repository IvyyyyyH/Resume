var fs = require('fs')
var json2xls = require('json2xls')
function toexcel(){
    fs.readdirSync('./data/').forEach(file => {
        var obj;
        var xls;
        if(file.substring(file.length-4, file.length) == 'json'){
            console.log(file)
            obj = JSON.parse(fs.readFileSync('./data/'+ file, 'utf8'))
            xls = json2xls(obj.table)
            fs.writeFileSync('./spreadsheet/'+file.substring(0, file.length-5)+'.xlsx', xls, 'binary')
        }
    })
}


if(process.argv[2] == '1')
{
	if(process.argv[3] == 'rcmusic')
		var music = require('./rcmusic/music.js')
	else if(process.argv[3] == 'yellowpage')
		var yellowpage = require('./yellowpage/index.js')
	else{
		var music = require('./rcmusic/music.js')
		var yellowpage = require('./yellowpage/index.js')
	}
} else {
    toexcel()
}


//music parts of web scrapping
var http = require('http');
var json2xls = require('json2xls')
var fs = require('fs');
var cheerio = require('cheerio');
var request = require('request');

var seenNames = {};
//
music_cat = [ 'Euphonium', 'Flute', 'Guitar', 'Organ', 'Piano', 'Saxophone',
'Speech+%26+Drama', 'Violin', 'Voice', 'Accordion', 'Clarinet'];
//keep going until the first name from this page exists(based on the website, when there's no more new pages,
// it goes back to page 1)


//generate the url with the instrument and page number
function generateUrl(instrument, page){
    var fixed = "http://www.rcmusic.ca/teacher-directory?distance[postal_code]=M5H2N2&distance[search_distance]=100";
    fixed = fixed + "&view_name=location&view_display_id=page_1&view_args=&view_path=teacher-directory";
    fixed = fixed + "&view_base_path=teacher-directory&view_dom_id=1&pager_element=0";
    fixed = fixed + "&page=" + page;
    fixed = fixed + "&distance[instrument]=" + instrument;
    return fixed;
}

//request to grab info from url x, into filename
function startRequest(instr, x, filename) {
    var result = 0;
    request(x, function(error, response, html){
        if(!error && response.statusCode == 200){
            var $ = cheerio.load(html);
            var name = [];
            var contact = [];
            var street = [];
            var locality = [];
            var region = [];
            var postalcode = [];
            $('.views-field.views-field-name').each(function(i, elm){
                var temp = $(this).text().trim();
                temp = temp.substring(0, temp.length - 7);
                name.push(temp);
            })
            $('.views-field.views-field-name a').each(function(i, elm){
                contact.push($(this).attr('href'))
            })
            $('.street-address').each(function(i, elm){
                street.push($(this).text().trim())
            })
            $('.locality').each(function(i, elm){
                locality.push($(this).text().trim())
            })
            $('.location.vcard .region').each(function(i, elm){
                region.push($(this).text().trim())
            })
            $('.postal-code').each(function(i, elm){
                postalcode.push($(this).text().trim())
            })
            name = name.splice(1, name.length)
            if(instr == music_cat[0]){
                instr = 'euphonium teacher'
            } else if(instr == music_cat[1]){
                instr = 'flute teacher'
            } else if(instr == music_cat[2]){
                instr = 'guitar teacher'
            } else if(instr == 'Organ'){
                instr = 'organ teacher'
            } else if(instr == 'Saxophone'){
                instr = 'saxophone teacher'
            } else if(instr == 'Piano'){
                instr = 'piano teacher'
            } else if(instr == 'Speech+%26+Drama'){
                instr = 'drama teacher'
            } else if(instr == 'Voilin'){
                instr = 'violin teacher'
            } else if(instr == 'Voice'){
                instr = 'vocal teacher'
            } else if(instr == 'Accordion'){
                instr = 'accordion teacher'
            } else if(instr == 'Clarinet'){
                instr = 'clarinet teacher'
            }
            for(var i = 0; i < name.length; i++){
                var teacher_info = {
                    source: 'rcmusic',
                    service_name: name[i],
                    category: instr,
                    phone: "http://www.rcmusic.ca" + contact[i],
                    address: street[i] + ", " + locality[i] + ", " + region[i] + ", " + postalcode[i],
                    postalcode: postalcode[i],
                    website: '',
                    working_hour: '',
                    latitude: '',
                    longitude: ''
                }
                if([teacher_info.phone, teacher_info.category] in seenNames){

                }else{
                    seenNames[[teacher_info.phone, teacher_info.category]] = true;
                    var content = JSON.parse(fs.readFileSync(filename));
                    content.table.push(teacher_info);
                    content = fs.writeFileSync(filename, JSON.stringify(content));
                }
            }
        }
    })
}

//get for num of pages
function singleInstr(instr, filename, num){
    console.log('now getting category: ' + instr+'...')
    for(var i = 1; i <= num; i++){
        var url = generateUrl(instr, i);
        fs.open(filename,'r',function(err, fd){
            if(err){
                fs.writeFile(filename, '{"table": []}', function(err) {
                    if(err) throw err;
                });
            }
        })
        startRequest(instr, url, filename)
    }
}

function together(num){
    for(var i = 0; i < music_cat.length; i++){
        singleInstr(music_cat[i], './data/'+music_cat[i]+'.json', num);
    }
}

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
    together(20)
} else {
    toexcel()
}

module.exports = {together}
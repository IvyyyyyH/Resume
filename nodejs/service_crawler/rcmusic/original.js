//music parts of web scrapping
var http = require('http');
var fs = require('fs');
var cheerio = require('cheerio');
var request = require('request');

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
            for(var i = 0; i < name.length; i++){
            	var teacher_info = {
            	    source: 'rcmusic',
            		name: name[i],
            		contact: "http://www.rcmusic.ca" + contact[i],
            	    location: street[i] + ", " + locality[i] + ", " + region[i] + ", " + postalcode[i],
            	    postalcode: postalcode[i],
            	    instrument: instr,
            	}
            	var content = JSON.parse(fs.readFileSync(filename));
                content.table.push(teacher_info);
                content = fs.writeFileSync(filename, JSON.stringify(content));
            }
        }
    })
}


function singleInstr(instr, filename){
	for(var i = 1; i <= 10; i++){
		var url = generateUrl(instr, i);
        fs.open(filename,'r',function(err, fd){
            if(err){
                fs.writeFile(filename, '{"table": []}', function(err) {
                    if(err) throw err;
                });
            }
        }
		startRequest(instr, url, filename)
	}
}

function together(){
	for(var i = 0; i < music_cat.length; i++){
		singleInstr(music_cat[i], './data/'+music_cat[i]+'.json');
	}
}

//together();

function fixJson(inputfilename, outputfilename){
    var content = JSON.parse(fs.readFileSync(inputfilename)).table;
    var seenContact = {};

    content = content.filter(function(currentObject) {
        
        if (currentObject.contact in seenContact) {
            return false;
        } else {
            seenContact[currentObject.contact] = true;
            return true;
        }        
    });
    fs.writeFileSync(outputfilename, JSON.stringify(content));

}

function cleanup(){
    for(var i = 0; i < music_cat.length; i++){
        fixJson('./data/'+music_cat[i]+'.json', './cleanup/'+music_cat[i]+'.json')
    }
}
cleanup()
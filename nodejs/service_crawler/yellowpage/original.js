//extracting info from yellowpage
var http = require('http');
var fs = require('fs');
var cheerio = require('cheerio');
var request = require('request');


const categories = ['beauty salon', 'dry cleaning', 'hair stylist', 'manicure and pedicure', 
'massage', 'moving', 'tanning', 'travel agency', 'wedding planning', 'garage sales', 
'car accessories', 'car wash', 'car body shop', 'car detailing', 'car mechanic', 
'tire repair', 'car windshield', 'architect design', 'cabinet', 'flooring', 'renovation',
'glass and mirror', 'home inspection', 'insulation', 'interior design', 'roofing', 'wall painting',
'waste disposal', 'windows and doors', 'cleaning', 'electrician', 'garden maintainance',
'handyman', 'air conditioning', 'locksmith', 'pest control', 'plumbing', 'security alarm',
'snow plowing', 'storage rental', 'accounting', 'dental', 'financial services', 'IT services',
'legal services', 'mortgage specialist', 'real estate agent', 'translation', 'immigration',
'college courses tutoring', 'driving tutoring', 'early education tutoring', 'elementary school tutoring',
'language tutoring', 'professional designation tutoring', 'trade and technical skills tutoring',
'badminton training', 'baseball training', 'basketball training', 'boxing training', 'cycling training',
'fitness training', 'golf club', 'gymnastics', 'Hockey Lesson & School', 'ping pong training',
'running training', 'soccer training', 'Swimming Lesson', 'tennis club', 'volleyball training',
'accordion teacher', 'clarinet teacher', 'cooking teacher', 'dancing teacher', 'drawing courses', 'euphonium teacher',
'flute teacher', 'guitar teacher', 'organ teacher', 'piano teacher', 'saxophone teacher',
'drama teacher', 'violin teacher', 'vocal teacher'];


const postcodes = [
'K0A', 'K0B', 'K0C', 'K0E', 'K0G', 'K0H', 'K0J', 'K0K', 'K0L', 'K0M', 
'K1A', 'K1B', 'K1C', 'K1E', 'K1G', 'K1H', 'K1J', 'K1K', 'K1L', 'K1M', 'K1N', 'K1P', 'K1R', 'K1S', 'K1T', 'K1V', 'K1W', 'K1X', 'K1Y', 'K1Z',
'K2A', 'K2B', 'K2C', 'K2E', 'K2G', 'K2H', 'K2J', 'K2K', 'K2L', 'K2M', 'K2P', 'K2R', 'K2S', 'K2T', 'K2V', 'K2W',
'K4A', 'K4B', 'K4C', 'K4K', 'K4M', 'K4P', 'K4R',
'K6A', 'K6H', 'K6J', 'K6K', 'K6T', 'K6V',
'K7A', 'K7C', 'K7G', 'K7H', 'K7K', 'K7L', 'K7M', 'K7N', 'K7P', 'K7R', 'K7S', 'K7V',
'K8A', 'K8B', 'K8H', 'K8N', 'K8P', 'K8R', 'K8V',
'K9A', 'K9H', 'K9J', 'K9K', 'K9L', 'K9V',

'L0A', 'L0B', 'L0C', 'L0E', 'L0G', 'L0H', 'L0J', 'L0K', 'L0L', 'L0M', 'L0N', 'L0P', 'L0R', 'L0S',
'L1A', 'L1B', 'L1C', 'L1E', 'L1G', 'L1H', 'L1J', 'L1K', 'L1L', 'L1M', 'L1N', 'L1P', 'L1R', 'L1S', 'L1T', 'L1V', 'L1W', 'L1X', 'L1Y', 'L1Z', 
'L2A', 'L2E', 'L2G', 'L2H', 'L2J', 'L2M', 'L2N', 'L2P', 'L2R', 'L2S', 'L2T', 'L2V', 'L2W', 
'L3C', 'L3B', 'L3K', 'L3M', 'L3P', 'L3R', 'L3S', 'L3T', 'L3V', 'L3X', 'L3Y', 'L3Z', 
'L4A', 'L4B', 'L4C', 'L4E', 'L4G', 'L4H', 'L4J', 'L4K', 'L4L', 'L4M', 'L4N', 'L4P', 'L4R', 'L4S', 'L4T', 'L4V', 'L4W', 'L4X', 'L4Y', 'L4Z', 
'L5A', 'L5B', 'L5C', 'L5E', 'L5G', 'L5H', 'L5J', 'L5K', 'L5L', 'L5M', 'L5N', 'L5P', 'L5R', 'L5S', 'L5T', 'L5V', 'L5W',
'L6A', 'L6B', 'L6C', 'L6E', 'L6G', 'L6H', 'L6J', 'L6K', 'L6L', 'L6M', 'L6P', 'L6R', 'L6S', 'L6T', 'L6V', 'L6W', 'L6X', 'L6Y', 'L6Z', 
'L7A', 'L7B', 'L7C', 'L7E', 'L7G', 'L7J', 'L7K', 'L7L', 'L7M', 'L7N', 'L7P', 'L7R', 'L7S', 'L7T', 
'L8B', 'L8E', 'L8G', 'L8H', 'L8J', 'L8K', 'L8L', 'L8M', 'L8N', 'L8P', 'L8R', 'L8S', 'L8T', 'L8V', 'L8W', 
'L9A', 'L9B', 'L9C', 'L9E', 'L9G', 'L9H', 'L9J', 'L9K', 'L9L', 'L9M', 'L9N', 'L9P', 'L9R', 'L9S', 'L9T', 'L9V', 'L9W', 'L9X', 'L9Y', 'L9Z',


'M1B', 'M1C', 'M1E', 'M1G', 'M1H', 'M1J', 'M1K', 'M1L', 'M1M', 'M1N', 'M1P', 'M1R', 'M1S', 'M1T', 'M1V', 'M1W', 'M1X',
'M2H', 'M2J', 'M2K', 'M2L', 'M2M', 'M2N', 'M2P', 'M2R', 
'M3A', 'M3B', 'M3C', 'M3H', 'M3J', 'M3K', 'M3L', 'M3M', 'M3N', 
'M4A', 'M4B', 'M4C', 'M4E', 'M4G', 'M4H', 'M4J', 'M4K', 'M4L', 'M4M', 'M4N', 'M4P', 'M4R', 'M4S','M4T', 'M4V', 'M4W', 'M4X', 'M4Y', 
'M5A', 'M5B', 'M5C', 'M5E', 'M5G', 'M5H', 'M5J', 'M5K', 'M5L', 'M5M', 'M5N', 'M5P', 'M5R', 'M5S', 'M5T', 'M5V', 'M5W', 'M5X', 
'M6A', 'M6B', 'M6C', 'M6E', 'M6G', 'M6H', 'M6J', 'M6K', 'M6L', 'M6M', 'M6N', 'M6P', 'M6R', 'M6S', 
'M7A', 'M7R', 'M7Y', 
'M8V', 'M8W', 'M8X', 'M8Y', 'M8Z', 
'M9A', 'M9B', 'M9C', 'M9L', 'M9M', 'M9N', 'M9P', 'M9R', 'M9V', 'M9W', 

'N0A', 'N0B', 'N0C', 'N0E', 'N0G', 'N0H', 'N0J', 'N0K', 'N0L', 'N0M', 'N0N', 'N0P', 'N0R', 
'N1A', 'N1C', 'N1E', 'N1G', 'N1H', 'N1K', 'N1L', 'N1M', 'N1P', 'N1R', 'N1S', 'N1T', 
'N2A', 'N2B', 'N2C', 'N2E', 'N2G', 'N2H', 'N2J', 'N2K', 'N2L', 'N2M', 'N2N', 'N2P', 'N2R', 'N2T', 'N2V', 'N2Z',
'N3A', 'N3B', 'N3C', 'N3E', 'N3H', 'N3L', 'N3P', 'N3R', 'N3T', 'N3V', 'N3W', 'N3Y', 
'N4B', 'N4G', 'N4G', 'N4K', 'N4L', 'N4N', 'N4S', 'N4T', 'N4W', 'N4X', 'N4Z',
'N5A', 'N5C', 'N5H', 'N5L', 'N5P', 'N5R', 'N5V', 'N5W', 'N5X', 'N5Y', 'N5Z',
'N6A', 'N6B', 'N6C', 'N6E', 'N6G', 'N6H', 'N6J', 'N6K', 'N6L', 'N6M', 'N6N', 'N6P', 
'N7A', 'N7G', 'N7L', 'N7M', 'N7S', 'N7T', 'N7V', 'N7W', 'N7X',
'N8A', 'N8H', 'N8M', 'N8N', 'N8P', 'N8R', 'N8W', 'N8X', 'N8Y',
'N9A', 'N9B', 'N9C', 'N9E', 'N9G', 'N9H', 'N9J', 'N9K', 'N9V', 'N9Y',


'P0A', 'P0B', 'P0C', 'P0E', 'P0G', 'P0H', 'P0J', 'P0K', 'P0L', 'P0M', 'P0N', 'P0P', 'P0R', 'P0S', 'P0T', 'P0V', 'P0W', 'P0X', 'P0Y',
'P1A', 'P1B', 'P1C', 'P1H', 'P1L', 'P1P', 
'P2A', 'P2B', 'P2N',
'P3A', 'P3B', 'P3C', 'P3E', 'P3G', 'P3L', 'P3N', 'P3P', 'P3Y',
'P4N', 'P4P', 'P4R', 
'P5A', 'P5E', 'P5N', 
'P6A', 'P6B', 'P6C', 
'P7A', 'P7B', 'P7C', 'P7E', 'P7G', 'P7J', 'P7K', 'P7L',
'P8N', 'P8T', 
'P9A', 'P9N'
];

function grablat(x) {
    var result;
    result = x.substring(x.indexOf("latitude") + 12, x.indexOf("longitude") - 4);
    return result;
}

function grablon(x) {
    var result;
    result = x.substring(x.indexOf("longitude") + 13, x.indexOf("isMerchantSensitive") - 7);
    return result;
}

function removen(x) {
    var result = x;
    while(result.indexOf("\n") != -1)
        result = result.replace("\n", " ");
    return result;
}

var seenNames = {}; 

function cleanupurl(x){
    var result = ' ';
    if(x)
        result = x.substring(x.indexOf("?") + 1);
    return result;
}

//x would be the name of the categroy
function generateUrl(x, location){
    var category = encodeURIComponent(x.trim())
    var location = encodeURIComponent(location.trim())
    var result = "http://www.yellowpages.ca/search/si/1/"+category+"/"+location;
    return result;
}

//write num number of service from url x
function startRequest(cat, x, filename, num) {
    var result = 0;
    request(x, function(error, response, html){
        if(!error && response.statusCode == 200){
            var websites = cheerio.load(html);
            var j = 0;
            websites('.listing__name--link.jsListingName').each(function(i, elm) {
                if(j < num){
                    var temp = "http://www.yellowpages.ca" + websites(this).attr('href');
                    request(temp, function(err, resp, html2) {
                        if(!err && resp.statusCode == 200){
                            var $ = cheerio.load(html2);
                            var website;
                            var address;
                            var phone = '';
                            address = $('.merchant__item.merchant__address').text().trim();
                            phone = $('.mlr__sub-text').first().text();
                            if(address){
                                //main page already have address
                                var service_info = {
                                    source: 'yellow page',
                                    service_name: $('.merchant-title__name.jsShowCTA').text().trim(), 
                                    category: cat,
                                    phone: phone,
                                    address: address,
                                    postalcode: $('.merchant__item.merchant__address').find('span[itemprop="postalCode"]').text().trim(),
                                    website: decodeURIComponent(cleanupurl($('.mlr__item__cta.hide-print').attr('href'))),
                                    //description: $('.merchant__item.merchant__teaser').text().trim(),
                                    working_hour: removen($('.openHours-table').text().trim()),
                                    latitude:grablat($('#reviews-config').text()),
                                    longitude:grablon($('#reviews-config').text()),
                                };
                                if ([service_info.service_name, service_info.postalcode, service_info.cat] in seenNames) {
                                    ;//do nothing
                                } else {
                                    seenNames[[service_info.service_name, service_info.postalcode, service_info.cat]] = true;
                                    var content = JSON.parse(fs.readFileSync(filename));
                                    content.table.push(service_info);
                                    content = fs.writeFileSync(filename, JSON.stringify(content));
                                }
                                
                            }
                            else{
                                var multiple = $('.merchant__item.merchant__item--multi.hide-print a').attr('href');
                                if(!multiple){
                                    //does not have multiple locations, also does not have location to begin with
                                    phone = $('.mlr__sub-text').first().text();
                                    var service_info = {
                                        source: 'yellow page',
                                        service_name: $('.merchant-title__name.jsShowCTA').text().trim(), 
                                        category: cat,
                                        phone: phone,
                                        address: '',
                                        postalcode: '',
                                        website: decodeURIComponent(cleanupurl($('.mlr__item__cta.hide-print').attr('href'))),
                                        //description: $('.merchant__item.merchant__teaser').text().trim(),
                                        working_hour: removen($('.openHours-table').text().trim()),
                                        latitude:grablat($('#reviews-config').text()),
                                        longitude:grablon($('#reviews-config').text()),
                                    };
                                    if ([service_info.service_name, service_info.postalcode, service_info.cat] in seenNames) {
                                        ;//do nothing
                                    } else {
                                        seenNames[[service_info.service_name, service_info.postalcode, service_info.cat]] = true;
                                        var content = JSON.parse(fs.readFileSync(filename));
                                        content.table.push(service_info);
                                        content = fs.writeFileSync(filename, JSON.stringify(content));
                                    }
                                }
                                else{
                                    //have multiple locations, only add the 1st one
                                    multiple = 'http://www.yellowpages.ca'+multiple;
                                    request(multiple, function(err2, resp2, html3) {
                                        var multihtml = cheerio.load(html3);
                                        address = multihtml('.listing__address--full').first().text().trim();
                                        phone = multihtml('.mlr__submenu__item').first().text().trim();
                                        phone = phone.substring(0,phone.indexOf('P'))
                                        if(!address)
                                            address = '';
                                        if(!phone)
                                            phone = '';
                                        var service_info = {
                                            source: 'yellow page',
                                            service_name: $('.merchant-title__name.jsShowCTA').text().trim(), 
                                            category: cat,
                                            phone: phone,
                                            address: address,
                                            postalcode: multihtml('.listing__address--full').first().find('span[itemprop="postalCode"]').text().trim(),
                                            website: decodeURIComponent(cleanupurl($('.mlr__item__cta.hide-print').attr('href'))),
                                            //description: $('.merchant__item.merchant__teaser').text().trim(),
                                            working_hour: removen($('.openHours-table').text().trim()),
                                            latitude:grablat($('#reviews-config').text()),
                                            longitude:grablon($('#reviews-config').text()),
                                        };
                                        if ([service_info.service_name, service_info.postalcode, service_info.cat] in seenNames) {
                                            ;//do nothing
                                        } else {
                                            seenNames[[service_info.service_name, service_info.postalcode, service_info.cat]] = true;
                                            var content = JSON.parse(fs.readFileSync(filename));
                                            content.table.push(service_info);
                                            content = fs.writeFileSync(filename, JSON.stringify(content));
                                        }
                                    })
                                }
                                
                            }
                        }
                    })
                    j = j + 1
                }
            })
        }
    })
}

function oneCat(catNum){
    for(var j = 0; j < postcodes.length; j++){
            var tempWeb = generateUrl(categories[catNum], postcodes[j]);
            //startRequest(categories[catNum], tempWeb, 'result.json', 2);
            startRequest(categories[catNum], tempWeb, './data/'+ categories[catNum] + '.json', 20);
        }
}

// the file with filename needs to contain a 
    //{"table":[]}
//number of categories, filename as well as max number of services each category

function together(numofCat){
    if(numofCat <= 85) new Promise(resolve =>{
        console.log('now getting category: '+ categories[numofCat] + '...');
        oneCat(numofCat);
        setTimeout(resolve, 60 * 1000);
        numofCat = numofCat+1;
    }).then(together.bind(null, numofCat+1));
    else process.exit();
}

together(0)

//fixJson need to be called after the file is already loaded, it will filter out the 
//services with the same name and the phone number
function fixJson(inputfilename, outputfilename){
    var content = JSON.parse(fs.readFileSync(inputfilename)).table;
    var seenNames = {};

    content = content.filter(function(currentObject) {
        
        if ([currentObject.service_name, currentObject.postalcode, currentObject.cat] in seenNames) {
            return false;
        } else {
            seenNames[[currentObject.service_name, currentObject.postalcode, currentObject.cat]] = true;
            return true;
        }        
    });
     fs.writeFileSync(outputfilename, JSON.stringify(content));

}
//fixJson('result.json', 'result2.json');


import re
import sys 

startScript=b"""
window.oldLocation = location.href;
var parameterOld = new URLSearchParams(location.search);

function main(){
  if (!parameterOld.get('Done')){
    function updateURLParameter(wordlist) {
      var currrentURL = oldLocation;
      var newURLSearch = "";
      var newURLHash = "";

      for (i=0;i < wordlist.length;i++){
        param = wordlist[i];
        if (!parameterOld.get(param)){
          payload = "1HeWkAJ3<\'"1HeWkAJ3" + param;
          if (oldLocation.indexOf("?") < 0 && newURLSearch.indexOf("?") < 0){
            newURLSearch = newURLSearch + "?" + param + "=" + payload + "s";
          } else {
            newURLSearch = newURLSearch + "&" + param + "=" + payload + "s";
          }

          if (currrentURL.indexOf("#") < 0 && newURLHash.indexOf("#") < 0){
            newURLHash = newURLHash + "#" + param + "=" + payload + "h";
          } else {
            newURLHash = newURLHash + "&" + param + "=" + payload + "h";
          }
        }
      }
      return oldLocation + newURLSearch + newURLHash;
    }

    function run(wordlist){
      return updateURLParameter(wordlist);
    }

    function loadWordlist(url){
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            output=run(xhttp.responseText.split('\\n'));
            window.history.pushState({},"",output);
          }
      };
      xhttp.open("GET", url, false);
      xhttp.send();
    }
    loadWordlist('""" + sys.argv[6].encode('utf-8')  + b"""');
  }
}
main();"""

endScript=b"""
if (!parameterOld.get('Done')){
        if (oldLocation.indexOf("?") < 0){
        oldLocation = oldLocation + "?Done=Done1";
} else {
        oldLocation = oldLocation + "&Done=Done1";
}
        setTimeout(function(){
                window.history.pushState({},"",oldLocation);
        },3000);
}"""

def response(flow):
    content = flow.response.content  # <-- remove the decode() method
    if b'<head' in content:
        MathHtml = re.findall(b'(<head.*?>)',content)[0]
        content = content.replace(MathHtml,MathHtml + b'1<script>' + startScript + b'</script>')
        content = content.replace(b'</body>', b'<script>' + endScript + b'</script></body>')
    elif b'<body' in content:
        MathHtml = re.findall(b'(<body.*?>)',content)[0]
        content = content.replace(MathHtml,MathHtml + b'2<script>' + startScript + b'</script>')
        content = content.replace(b'</body>', b'<script>' + endScript + b'</script></body>')
    else:
       with open('fail_proxy.txt','a+') as f:
            f.write("[Not_html]: " + flow.request.url + '\n')

    flow.response.content = content  # <-- update the response with bytes
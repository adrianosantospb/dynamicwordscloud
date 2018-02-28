// Words list
// TODO: In the next version, maybe it's necessary to take this words by database.
// Use the space to delimite the words
var foo;

var words_list = function (){
    var url = 'http://127.0.0.1:5000/summary';

    var json = (function () {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': url,
        'dataType': "json",
        'success': function (data) {
            json = data;
        }
    });

    return json;
})();
    var stringf= "";
    for (var i = 0; i < json.words.length; i++) {
            stringf= stringf + " "+ json.words[i].word;

    }
    console.log (stringf);
  return [stringf];
};

function update (foo){
    console.log ("Entrou");
    foo = "aaa"
}

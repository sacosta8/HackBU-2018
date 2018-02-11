var elements = document.getElementsByTagName('*');
var words = ["SquadFam","Hackermen","Slim-Jims","Wookies","Hire Me (Please)"]

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            var randomNumber = Math.floor(Math.random() * 5);
            var text = node.nodeValue;
            var replacedText = text.replace(/people/ig,words[randomNumber]);

            if (replacedText !== text) {
                element.replaceChild(document.createTextNode(replacedText), node);
            }
        }
    }
}

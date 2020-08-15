(function() {
    var width, height, largeHeader;
    function initHeader() {
        width = window.innerWidth;
        height = window.innerHeight;
        largeHeader = document.getElementById('large-header');
        largeHeader.style.height = height+'px';
    }
    initHeader();
    function HighLight(nWord){ 
        if(nWord!=''){ 
            var keyword = document.body.createTextRange(); 
            while(keyword.findText(nWord)){ 
                keyword.pasteHTML("<span style='color:red;'>" + keyword.text + "</span>"); 
                keyword.moveStart('character',1); 
            } 
        }
    }
})();
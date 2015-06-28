!(function(self) {
    self.timeparse = function(s, format) {
        if(typeof format == 'undefined')
            format = "MMM D, YYYY, h:mm a";
        if (s.startsWith("2015"))  // #TODO wtf
            return moment(s, "YYYY-MM-DD")
        else return moment(s.replace(".", ""), format)
    }
    self.relativise_timestamps = function() {
        $(".human-timestamp").each(function(idx, el) {
            el = $(el)
            el.attr("title", el.text())
            el.html(self.timeparse(el.text()).fromNow())
        })
    }
})(window.codex = window.codex || {})

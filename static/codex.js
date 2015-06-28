!(function(self) {
    self.relativise_timestamps = function() {
        $(".human-timestamp").each(function(idx, el) {
            el = $(el)
            el.attr("title", el.text())
            el.html(moment(el).fromNow())
        })
    }
})(window.codex = window.codex || {})

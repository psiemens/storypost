var BASE_URL = 'http://localhost:8000/';


var PromptReply = React.createClass({displayName: "PromptReply",
    getInitialState: function(){
        var timestamp = codex.timeparse(this.props.timestamp, 'YYYY-MM-DDTHH:mm:ssZ');
        return {
            points: this.props.points,
            timestamp: timestamp,
            fromNow: timestamp.fromNow()
        }
    },
    tick: function(){
        this.setState({
            fromNow: this.state.timestamp.fromNow()
        });
    },
    componentDidMount: function(){
        this.interval = setInterval(this.tick, 1000);
    },
    upvote: function(event){
        event.preventDefault();
        $.get(BASE_URL + 'api/reply/' + this.props.id + '/upvote/', function(data){
            if(data.success){
                this.setState({ points: this.state.points + 1});
            }
        }.bind(this));
    },
    render: function(){
        return (
            React.createElement("li", null, 
                React.createElement("div", {className: "content"}, 
                    React.createElement("p", null,  this.props.content)
                ), 
                React.createElement("div", {className: "meta u-cf"}, 
                    React.createElement("div", {className: "u-pull-left"}, 
                        React.createElement("span", null,  this.state.points, " points  ·  ", React.createElement("a", {href: "#", onClick: this.upvote}, "upvote"))
                    ), 
                    React.createElement("div", {className: "u-pull-right"}, 
                        React.createElement("span", null,  this.props.email, "  ·  ", React.createElement("span", {className: "human-timestamp"},  this.state.fromNow))
                    )
                )
            )
            );
    }
});

var Prompt = React.createClass({displayName: "Prompt",
    getInitialState: function(){
        return {
            tab: 'recent',
            replies: [],
        }
    },
    syncReplies: function(){
        $.get(BASE_URL + 'api/prompt/' + this.props.id + '/?sort=' + this.state.tab, function(data){
            this.setState({
                replies: data.replies
            });
        }.bind(this));
    },
    componentDidMount: function() {
        this.syncReplies();
        this.interval = setInterval(this.syncReplies, 10000);
    },
    changeTab: function(tab, event){
        event.preventDefault();
        this.setState({ tab: tab }, this.syncReplies);
    },
    render: function(){

        var replies = this.state.replies.map(function(reply, i){
            return (React.createElement(PromptReply, {key: reply.id, id: reply.id, content: reply.content, points: reply.points, email: reply.email, timestamp: reply.timestamp}));
        }.bind(this));
        return (
            React.createElement("div", null, 
                React.createElement("ul", {className: "reply-tabs"}, 
                    React.createElement("li", null, React.createElement("a", {href: "#", className:  this.state.tab == 'recent' ? 'active' : '', onClick: this.changeTab.bind(this, 'recent')}, "Recent replies")), 
                    React.createElement("li", null, React.createElement("a", {href: "#", className:  this.state.tab == 'top' ? 'active' : '', onClick: this.changeTab.bind(this, 'top')}, "Top replies"))
                ), 
                React.createElement("ul", {className: "replies"}, replies)
            )
        );
    }
});

var id = $('#prompt').data('id');

React.render(
  React.createElement(Prompt, {id: id}),
  document.getElementById('prompt')
);
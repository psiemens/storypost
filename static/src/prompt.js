var BASE_URL = '/';

var PromptReply = React.createClass({
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
            <li>
                <div className="content">
                    <p>{ this.props.content }</p>
                </div>
                <div className="meta u-cf">
                    <div className="u-pull-left">
                        <span>{ this.state.points } points &nbsp;&middot;&nbsp; <a href="#" onClick={this.upvote}>upvote</a></span>
                    </div>
                    <div className="u-pull-right">
                        <span>{ this.props.email } &nbsp;&middot;&nbsp; <span className="human-timestamp">{ this.state.fromNow }</span></span>
                    </div>
                </div>
            </li>
            );
    }
});

var Prompt = React.createClass({
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
            return (<PromptReply key={reply.id} id={reply.id} content={reply.content} points={reply.points} email={reply.email} timestamp={reply.timestamp} />);
        }.bind(this));
        return (
            <div>
                <ul className="reply-tabs">
                    <li><a href="#" className={ this.state.tab == 'recent' ? 'active' : '' } onClick={this.changeTab.bind(this, 'recent')}>Recent replies</a></li>
                    <li><a href="#" className={ this.state.tab == 'top' ? 'active' : '' } onClick={this.changeTab.bind(this, 'top')}>Top replies</a></li>
                </ul>
                <ul className="replies">{replies}</ul>
            </div>
        );
    }
});

var id = $('#prompt').data('id');

React.render(
  <Prompt id={id} />,
  document.getElementById('prompt')
);
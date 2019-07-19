function ThumbsAside(runtime, element, block_element, init_args) {
    return new ThumbsBlock(runtime, element, init_args);
  }
  
  function MyXBlock(runtime, element, init_args) {
    function updateVotes(votes) {
      $('.upvote .count', element).text(votes.up);
      $('.downvote .count', element).text(votes.down);
    }
  
    var handlerUrl = runtime.handlerUrl(element, 'increment_count');
  
    $('.upvote', element).click(function(eventObject) {
      $.ajax({
          type: "POST",
          url: handlerUrl,
          data: JSON.stringify({voteType: 'up'}),
          success: updateVotes
      });
    });
  
    $('.downvote', element).click(function(eventObject) {
      $.ajax({
          type: "POST",
          url: handlerUrl,
          data: JSON.stringify({voteType: 'down'}),
          success: updateVotes
      });
    });
    return {};
  };
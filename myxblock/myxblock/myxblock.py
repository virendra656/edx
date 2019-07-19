"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer,Boolean, Scope
from xblock.fragment import Fragment


class MyXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    upvotes = Integer(help="Number of up votes", default=0,
        scope=Scope.user_state_summary)

    downvotes = Integer(help="Number of down votes", default=0,
        scope=Scope.user_state_summary)

    voted = Boolean(help="Has this student voted?", default=False,
        scope=Scope.user_state)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/myxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/myxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/myxblock.js"))
        frag.initialize_js('MyXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        if data['voteType'] not in ('up', 'down'):
            log.error('error!')
            return

        if data['voteType'] == 'up':
            self.upvotes += 1
        else:
            self.downvotes += 1

        self.voted = True

        return {'up': self.upvotes, 'down': self.downvotes}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MyXBlock",
             """<myxblock/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]
